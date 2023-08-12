# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2023 Michał Góral.

from typing import Optional, TypeVar, Callable, List

import importlib.resources
from enum import Enum
from dataclasses import dataclass, field
from pathlib import Path


class _Dialect(Enum):
    sqlite = "sqlite"
    postgres = "postgres"


VERSION_SPLIT_CH = ":"
DIALECTS = {
    _Dialect.sqlite: ":{}",
    _Dialect.postgres: "%({})s",
}


class Query:
    """An object which holds and modifies a query that is being built.
    Modifications are in-place and can be chained as in the builder pattern.

    Usage:
        add_article = query_loader.add_article(title="My article", text="Lorem Ipsum")
        add_article.on_conflict_update()

        cursor.execute(add_article.sql(), add_article.params)
    """

    def __init__(self, script, dialect, **initial_params):
        self._script = script
        self._dialect = dialect

        self.params = {}
        self._fmt = _MissingFormatDict()
        self._bindfmt = DIALECTS[self._dialect]
        self._i = 0

        self.update_params(**initial_params)

    def copy(self) -> "Query":
        new = Query(self._script, self._dialect)  # script is shallow-copied
        new.params = self.params.copy()
        new._i = self._i

        new_fmt = _MissingFormatDict()
        for key, val in self._fmt.items():
            if isinstance(val, _SubQuery):
                new_fmt[key] = val.copy(new)
            elif isinstance(val, _Placeholders):
                new_fmt[key] = val.copy()
            else:
                raise RuntimeError(f"unexpected type: {type(val)}")  # pragma: nocover

        new._fmt = new_fmt
        return new

    def sql(self, simplify=False) -> str:
        contents = self._script.contents

        if simplify:
            contents = self._script.contents.splitlines()
            contents = " ".join(
                [l.strip() for l in contents if not l.strip().startswith("--")]
            )

        return contents.format_map(self._fmt)

    def update_params(self, **params):
        for name, val in params.items():
            ph = self._fmt.setdefault(name, _Placeholders(parens=False))

            if isinstance(val, _Another):
                self._i += 1

                group = _Placeholders(parens=val.group)
                for j, elem in enumerate(val.args):
                    pname = f"{name}_p{self._i}_{j}"
                    bindname = self._bindfmt.format(pname)
                    group.add(bindname)
                    self.params[pname] = elem
                ph.add(group)
            else:
                ph.reset(self._bindfmt.format(name))
                self.params[name] = val
        return self

    def __getattr__(self, name: str) -> Callable[[str, str], None]:
        def _fn(**params):
            self._ensure_subquery(name)
            self.update_params(**params)
            return self

        return _fn

    def __repr__(self) -> str:
        return f"Query(script={self._script.name}.sql, dialect={self._dialect})"  # pragma: nocover

    def _ensure_subquery(self, subname: str):
        sub = self._fmt.get(subname)
        if sub is None:
            sub = self._script.find_substitution(subname)

            if sub is None:
                raise KeyError(f"substitution {subname} not found")

            sub = _SubQuery(self, subname, sub)
            self._fmt[subname] = sub


class QueryLoader:
    """Main class from which all queries are created. It keeps a list of
    available SQL scripts.

    Usage:
        ql = QueryLoader(package="package_name.scripts")
        add_user = ql.add_user()
        delete_user = ql.delete_user()
    """

    def __init__(
        self,
        *,
        package: Optional[str] = None,
        path: Optional[str] = None,
        dialect: str = "sqlite",
    ):
        if package and path:
            raise ValueError("can't initialize from both package and path")

        if not package and not path:
            raise ValueError("path or package required for initialization")

        if package:
            self.package = package
            self.scripts = _get_scripts(self.package, is_package=True)
        else:
            self.package = path
            self.scripts = _get_scripts(self.package, is_package=False)
        self._dialect = _Dialect(dialect)
        self._map = {s.name: s for s in self.scripts}

    def __getattr__(self, name: str) -> Query:
        def _fn(*a, **kw):
            try:
                return Query(self._map[name], self._dialect, *a, **kw)
            except KeyError as e:
                raise AttributeError(f"{name}.sql not found in {self.package}") from e

        return _fn

    def __repr__(self) -> str:
        return f"QueryLoader({self._dialect.value})"  # pragma: nocover


@dataclass
class Script:
    """Proxy to the script loaded by QueryLoader"""

    package: str
    script: Path
    name: str = field(default="", init=False)
    version: Optional[str] = field(default=None, init=False)
    from_package: bool = False
    _contents: Optional[str] = field(
        default=None, compare=False, repr=False, init=False
    )
    _subs: Optional[dict] = field(default=None, compare=False, repr=False, init=False)

    def __post_init__(self):
        self.version, _, self.name = self.script.stem.partition(VERSION_SPLIT_CH)
        if not self.name:
            self.name = self.version
            self.version = None

    @property
    def contents(self):
        if not self._contents:
            self._init_contents()
        return self._contents

    def find_substitution(self, name: str) -> Optional[str]:
        if self._subs is None:
            self._init_subs()

        return self._subs.get(name)

    def _init_contents(self):
        if self.from_package:
            # former importlib.resources.open_text
            self._contents = (
                importlib.resources.files(self.package)
                .joinpath(self.script)
                .open("r", encoding="utf-8")
                .read()
            )
        else:
            with open(Path(self.package) / self.script, encoding="utf-8") as sql:
                self._contents = sql.read()

    def _init_subs(self):
        self._subs = {}
        substart = "-- sub"
        for line in self.contents.splitlines():
            line = line.strip()
            if line.startswith(substart):
                key, _, expr = line.partition(":")
                key = key.strip()[len(substart) + 1 :]
                self._subs[key] = expr.strip()

    def __lt__(self, other):
        return self.script < other.script

    def __repr__(self) -> str:
        return f"Script({self.package}, {self.name}.sql, v={self.version})"  # pragma: nocover


def Another(*values):
    """When you wrap a value passed to you query with Another(), it won't
    replace previously given value, but instead it'll create a comma-separated
    list of all values passed wrapped with Another()."""
    return _Another(*values, group=False)


def AnotherGroup(*values):
    """Same as Another(), but additionally all values inside a single
    AnotherGroup() will be enclosed in parentheses. It is useful e.g. for bulk
    INSERTs."""
    return _Another(*values, group=True)


class _SubQuery:
    def __init__(self, parent: "Query", name: str, sub: str):
        self.parent = parent
        self.name = name
        self.sub = sub

    def copy(self, new_parent: "Query") -> "_SubQuery":
        return _SubQuery(new_parent, self.name, self.sub)

    def __format__(self, spec) -> str:
        return self.sub.format_map(self.parent._fmt)

    def __repr__(self) -> str:
        return f"SubQuery(name={self.name})"  # pragma: nocover


class _Placeholders:
    """A group of named placeholders which is conditionally formatted with or
    without parentheses around it."""

    def __init__(self, parens=False):
        self.args = []
        self.parens = parens

    def add(self, val):
        self.args.append(val)

    def reset(self, val):
        self.args = [val]

    def copy(self) -> "_Placeholders":
        new = _Placeholders(self.parens)
        new.args = self.args[:]
        return new

    def __format__(self, spec) -> str:
        inside = ", ".join(format(a) for a in self.args)
        if self.parens:
            return f"({inside})"
        return inside

    def __repr__(self) -> str:
        return f"<Placeholders with {len(self.args)} params>"  # pragma: nocover


class _Another:
    def __init__(self, *args, group=False):
        self.args = args
        self.group = group

    def __repr__(self):
        en = "enabled" if self.group else "disabled"  # pragma: nocover
        return f"<Another {len(self.args)} params, grouping {en}>"  # pragma: nocover


# we need a dictionary which returns empty strings for missing format keys,
# doesn't store them, because query._ensure_subquery would detect it and return
# that default empty string instead of a subquery (e.g. after q.sql();
# q.copy().subquery())
class _MissingFormatDict(dict):
    def __missing__(self, key):
        return ""


def _get_scripts(package: str, is_package: bool) -> List[Script]:
    scripts = []
    if is_package:
        contents = (
            resource.name
            for resource in importlib.resources.files(package).iterdir()
            if resource.is_file()
        )
    else:
        package = Path(package).absolute()
        contents = package.iterdir()

    for res in contents:
        path = Path(res)
        if path.suffix != ".sql":
            continue

        scripts.append(Script(package, Path(path.name), from_package=is_package))

    scripts.sort()
    return scripts

# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2023 Michał Góral.

from pathlib import Path

import pytest

from sqlcomposer import (
    QueryLoader,
    Another,
    AnotherGroup,
)


def pytest_generate_tests(metafunc):
    if "ql" in metafunc.fixturenames:
        metafunc.parametrize(
            "ql",
            [
                QueryLoader(package="testscripts"),
                QueryLoader(path="test/testscripts"),
                QueryLoader(path=Path(__file__).absolute().parent / "testscripts"),
            ],
            indirect=True,
        )


@pytest.fixture
def ql(request):
    return request.param


def read(script: str):
    testdir = Path(__file__).absolute().parent
    with open(testdir / "testscripts" / script, encoding="utf-8") as f:
        return f.read()


def test_no_package_or_path():
    with pytest.raises(ValueError):
        QueryLoader()


def test_both_package_and_path():
    with pytest.raises(ValueError):
        QueryLoader(
            package="testscripts", path=Path(__file__).absolute().parent / "testscripts"
        )


def test_query_list(ql):
    paths = [s.script for s in ql.scripts]
    names = [s.name for s in ql.scripts]
    versions = [s.version for s in ql.scripts]
    assert paths == [Path("0:s3.sql"), Path("s1.sql"), Path("s2.sql"), Path("s4.sql")]
    assert names == ["s3", "s1", "s2", "s4"]
    assert versions == ["0", None, None, None]


def test_query_build_default_empty_string(ql):
    expect = read("s1.sql").format(feeds="")
    q = ql.s1(username="foo", device="bar", deleted=1)
    assert q.sql() == expect
    assert q.params == {"username": "foo", "device": "bar", "deleted": 1}


def test_simplify(ql):
    expect = (
        "INSERT INTO podcasts(user, name, rss, summary, cover_url) "
        "VALUES :binds "
        "RETURNING name, rss, summary, cover_url, id, user"
    )

    q = ql.s4().values(binds=1)
    assert q.sql(simplify=True) == expect


def test_query_build_with_subquery(ql):
    expect = read("s1.sql").format(feeds="I am default")
    q = ql.s1(username="foo", device="bar", deleted=1)
    q.feeds(param=123)
    assert q.sql() == expect
    assert q.params == {"username": "foo", "device": "bar", "deleted": 1, "param": 123}


def test_query_chain(ql):
    expect = read("s2.sql").format(
        device="AND vds.device = :dev",
        not_deleted="AND s.deleted IS NULL",
        since="AND s.created > :created",
    )
    q = ql.s2()
    q.device().not_deleted().since()
    assert q.sql() == expect


def test_query_chain_same(ql):
    expect = read("s2.sql").format(
        device="AND vds.device = :dev", not_deleted="", since="AND s.created > :created"
    )
    q = ql.s2()
    q.device(p1=1, p2=2).since().device(p1=3, p3=4)
    assert q.sql() == expect
    assert q.params == {"p1": 3, "p2": 2, "p3": 4}


def test_query_copy(ql):
    q = ql.s2().device(p1="foo")
    expect_q = read("s2.sql").format(
        device="AND vds.device = :dev", not_deleted="", since=""
    )
    assert q.sql() == expect_q
    assert q.params == {"p1": "foo"}

    qc = q.copy()
    qc.not_deleted(p1="bar", p2="baz")
    expect_qc = read("s2.sql").format(
        device="AND vds.device = :dev", not_deleted="AND s.deleted IS NULL", since=""
    )
    assert qc.sql() == expect_qc
    assert qc.params == {"p1": "bar", "p2": "baz"}
    assert q.sql() == expect_q
    assert q.params == {"p1": "foo"}

    qcc = qc.copy()
    qcc.not_deleted(p2="bazbaz")
    expect_qcc = read("s2.sql").format(
        device="AND vds.device = :dev", not_deleted="AND s.deleted IS NULL", since=""
    )
    assert qcc.sql() == expect_qcc
    assert qcc.params == {"p1": "bar", "p2": "bazbaz"}
    assert qc.sql() == expect_qc
    assert qc.params == {"p1": "bar", "p2": "baz"}
    assert q.sql() == expect_q
    assert q.params == {"p1": "foo"}


def test_query_copy_another(ql):
    q = ql.s4()
    q.values(binds=1)

    qc = q.copy().values(binds=Another(3))
    qcc = qc.copy().values(binds=Another(4))
    qg = q.copy().values(binds=AnotherGroup(5, 6))
    qgg = qg.copy().values(binds=AnotherGroup(7, 8))

    q_exp_binds = ":binds"
    qc_exp_binds = ":binds, :binds_p1_0"
    qcc_exp_binds = ":binds, :binds_p1_0, :binds_p2_0"
    qg_exp_binds = ":binds, (:binds_p1_0, :binds_p1_1)"
    qgg_exp_binds = ":binds, (:binds_p1_0, :binds_p1_1), (:binds_p2_0, :binds_p2_1)"

    expect_q = read("s4.sql").format(values=q_exp_binds, binds=q_exp_binds)
    expect_qc = read("s4.sql").format(values=qc_exp_binds, binds=qc_exp_binds)
    expect_qcc = read("s4.sql").format(values=qcc_exp_binds, binds=qcc_exp_binds)
    expect_qg = read("s4.sql").format(values=qg_exp_binds, binds=qg_exp_binds)
    expect_qgg = read("s4.sql").format(values=qgg_exp_binds, binds=qgg_exp_binds)

    assert q.sql() == expect_q
    assert qc.sql() == expect_qc
    assert qcc.sql() == expect_qcc
    assert qg.sql() == expect_qg
    assert qgg.sql() == expect_qgg

    assert q.params == {"binds": 1}
    assert qc.params == {"binds": 1, "binds_p1_0": 3}
    assert qcc.params == {"binds": 1, "binds_p1_0": 3, "binds_p2_0": 4}
    assert qg.params == {"binds": 1, "binds_p1_0": 5, "binds_p1_1": 6}
    assert qgg.params == {
        "binds": 1,
        "binds_p1_0": 5,
        "binds_p1_1": 6,
        "binds_p2_0": 7,
        "binds_p2_1": 8,
    }


def test_appending_and_resetting_parameters(ql):
    q = ql.s4()
    q.values(binds=Another(1))
    q.values(binds=Another(2))

    exp_binds = ":binds_p1_0, :binds_p2_0"
    expect_qcc = read("s4.sql").format(values=exp_binds, binds=exp_binds)
    assert q.sql() == expect_qcc
    assert q.params == {"binds_p1_0": 1, "binds_p2_0": 2}

    q.values(binds="foo")
    exp_binds = ":binds"
    expect_qcc = read("s4.sql").format(values=exp_binds, binds=exp_binds)
    assert q.sql() == expect_qcc
    assert q.params == {"binds_p1_0": 1, "binds_p2_0": 2, "binds": "foo"}


def test_appending_groups(ql):
    q = ql.s4()

    q.values(binds=Another(1))
    q.values(binds=AnotherGroup(2, 3))
    q.values(binds=AnotherGroup(7, 8))
    q.values(binds=Another(4, 5))
    q.values(binds=Another(6))

    exp_binds = [
        ":binds_p1_0",
        "(:binds_p2_0, :binds_p2_1)",
        "(:binds_p3_0, :binds_p3_1)",
        ":binds_p4_0",
        ":binds_p4_1",
        ":binds_p5_0",
    ]
    exp_binds = ", ".join(exp_binds)
    expect_q = read("s4.sql").format(values=exp_binds, binds=exp_binds)
    assert q.sql() == expect_q
    assert q.params == {
        "binds_p1_0": 1,
        "binds_p2_0": 2,
        "binds_p2_1": 3,
        "binds_p3_0": 7,
        "binds_p3_1": 8,
        "binds_p4_0": 4,
        "binds_p4_1": 5,
        "binds_p5_0": 6,
    }


def test_postgres_dialect():
    ql = QueryLoader(package="testscripts", dialect="postgres")
    q = ql.s4()

    q.values(binds=Another(1))
    q.values(binds=AnotherGroup(2, 3))
    q.values(binds=AnotherGroup(7, 8))
    q.values(binds=Another(4, 5))
    q.values(binds=Another(6))

    exp_binds = [
        "%(binds_p1_0)s",
        "(%(binds_p2_0)s, %(binds_p2_1)s)",
        "(%(binds_p3_0)s, %(binds_p3_1)s)",
        "%(binds_p4_0)s",
        "%(binds_p4_1)s",
        "%(binds_p5_0)s",
    ]
    exp_binds = ", ".join(exp_binds)
    expect_q = read("s4.sql").format(values=exp_binds, binds=exp_binds)
    assert q.sql() == expect_q
    assert q.params == {
        "binds_p1_0": 1,
        "binds_p2_0": 2,
        "binds_p2_1": 3,
        "binds_p3_0": 7,
        "binds_p3_1": 8,
        "binds_p4_0": 4,
        "binds_p4_1": 5,
        "binds_p5_0": 6,
    }


def test_dialect_copy():
    ql = QueryLoader(package="testscripts", dialect="postgres")
    q = ql.s4()
    q.values(binds=1)

    exp_binds = "%(binds)s"
    expect_q = read("s4.sql").format(values=exp_binds, binds=exp_binds)
    assert q.sql() == expect_q
    assert q.params == {"binds": 1}

    qc = q.copy()
    qc.values(binds=2)
    exp_binds = "%(binds)s"
    expect_qc = read("s4.sql").format(values=exp_binds, binds=exp_binds)
    assert qc.sql() == expect_qc
    assert qc.params == {"binds": 2}
    assert q.sql() == expect_q
    assert q.params == {"binds": 1}


def test_missing_script(ql):
    with pytest.raises(AttributeError):
        q = ql.foobar()


def test_missing_subquery(ql):
    q = ql.s4()

    with pytest.raises(KeyError):
        q.foobar()


def test_wrong_dialect():
    with pytest.raises(ValueError):
        QueryLoader(package="testscripts", dialect="foobar")

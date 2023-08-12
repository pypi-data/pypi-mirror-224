-- sub values: {binds}
INSERT INTO podcasts(user, name, rss, summary, cover_url)
VALUES {values}
RETURNING name, rss, summary, cover_url, id, user

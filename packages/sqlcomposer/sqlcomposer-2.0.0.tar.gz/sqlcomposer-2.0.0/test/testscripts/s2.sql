-- sub device: AND vds.device = :dev
-- sub not_deleted: AND s.deleted IS NULL
-- sub since: AND s.created > :created
SELECT DISTINCT p.name, p.rss, p.summary, p.cover_url, p.id, vds.uid
FROM view_dev_subs vds
INNER JOIN podcasts p ON p.id = vds.podid
INNER JOIN subscriptions s ON s.id = vds.subid
WHERE
    vds.username = :username
    {device}
    {not_deleted}
    {since}


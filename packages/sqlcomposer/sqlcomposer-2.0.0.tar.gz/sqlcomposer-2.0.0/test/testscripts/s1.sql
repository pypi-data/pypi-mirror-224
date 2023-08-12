-- sub feeds: I am default
UPDATE subscriptions
SET deleted = :deleted
FROM(SELECT username, device, subid, rss FROM view_dev_subs) AS vds
WHERE
    subscriptions.id=vds.subid
    AND vds.username = :username
    AND vds.device = :device
    AND vds.rss IN({feeds})

#!/bin/bash
docker volume create grafana-storage
docker rm -f grafana
docker run -d -p 3000:3000 --name=grafana -v grafana-storage:/var/lib/grafana grafana/grafana

You can reach it on your servers' IP and port 3000, for example: http://192.168.0.120:3000/

In grafana, set up a datasource pointing to your mysql database.

And create a dashboard with this query (note, I just added 4* to the queries [Nov 1, 2020], as they were per 15 minutes, instead of per hour):

SELECT
  TIMESTAMP AS "time",
  4*GAS_DM3 as GAS_DM3h,
  4*(DELIVERY_LOW_WH + DELIVERY_HIGH_WH) as DELIVERY_WH,
  4*(BACKDELIVERY_LOW_WH + BACKDELIVERY_HIGH_WH) as BACKDELIVERY_WH
FROM METER_VIEW
WHERE
  $__timeFilter(TIMESTAMP)
ORDER BY TIMESTAMP

Set timeline to 24 HR's to see your last day usage.

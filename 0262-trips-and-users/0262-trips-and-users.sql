SELECT
    request_at as "Day",
    ROUND(SUM(CASE WHEN status IN ('cancelled_by_driver', 'cancelled_by_client') THEN 1 ELSE 0 END)/ COUNT(*), 2) as "Cancellation Rate"
FROM
    Trips
WHERE
    request_at BETWEEN '2013-10-01' AND '2013-10-03' AND
    client_id NOT IN (SELECT users_id FROM Users WHERE role = 'client' AND banned = 'Yes') AND
    driver_id NOT IN (SELECT users_id FROM Users WHERE role = 'driver' AND banned = 'Yes')
GROUP BY
    1
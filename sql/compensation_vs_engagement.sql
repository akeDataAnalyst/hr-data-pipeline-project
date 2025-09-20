SELECT
    department,
    ROUND(AVG(compensation), 2) AS avg_compensation,
    ROUND(AVG(engagement_score), 2) AS avg_engagement_score,
    COUNT(*) AS employee_count
FROM
	`your_gcp_project_id.your_bigquery_dataset_id.your_bigquery_table_id`
WHERE
    engagement_score IS NOT NULL
GROUP BY
    department
ORDER BY
    avg_engagement_score DESC;
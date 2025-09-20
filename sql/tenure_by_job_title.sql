SELECT
    job_title,
    AVG(tenure_days) AS avg_tenure_days,
    COUNT(*) AS employee_count
FROM
	`your_gcp_project_id.your_bigquery_dataset_id.your_bigquery_table_id`
GROUP BY
    job_title
ORDER BY
    avg_tenure_days DESC;
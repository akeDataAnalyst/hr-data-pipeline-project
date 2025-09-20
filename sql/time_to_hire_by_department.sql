SELECT
    department,
    AVG(time_to_hire_days) AS avg_time_to_hire_days
FROM
    `your_gcp_project_id.your_gcp_bigquery_dataset_id.your_gcp_bigquery_table_id`
WHERE
    hiring_outcome = 'Hired'
GROUP BY
    department
ORDER BY
    avg_time_to_hire_days DESC;
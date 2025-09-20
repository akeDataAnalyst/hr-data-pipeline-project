# Automated HR Data Pipeline for People Analytics

This project demonstrates the development of an automated ETL (Extract, Transform, Load) pipeline for HR data. 
It's designed to solve the problem of fragmented data from multiple sources, providing a single, clean source of truth for people analytics. 

***

### **Problem Statement**

HR data is often scattered across multiple systems (e.g., ATS, HRIS, and survey tools), making it difficult to perform consistent reporting and strategic analysis. 
Manual data pulls and reporting are time-consuming and prone to human error. This project creates a solution to automate data collection, ensure data quality through standardized processing, and provide a reliable foundation for data-driven decision-making.

***

### **Architecture & Workflow**

The pipeline follows a classic ETL workflow to process data from source to a unified data warehouse. 




1.  **Extract:** Raw data is pulled from three simulated sources: an Applicant Tracking System (ATS), a Human Resources Information System (HRIS), and an Employee Engagement Survey tool.
2.  **Transform:** A Python script cleans the data, handles missing values, and enriches it by calculating valuable new metrics like **employee tenure** and **time-to-hire**.
3.  **Load:** The transformed, unified dataset is loaded into a table in **Google BigQuery**, where it is ready for analysis and reporting.

The entire process is automated and can be scheduled to run on a daily or weekly basis.

***

### **Technologies Used**

* **Python:** For scripting the core ETL process.
* **Pandas:** A powerful Python library used for data manipulation, cleaning, and transformation.
* **Google Cloud BigQuery:** Serves as the data warehouse for storing the clean data.
* **Google Cloud SDK:** Used for authentication and seamless API interaction with BigQuery.
* **Windows Task Scheduler:** Utilized for automating the pipeline to run on a set schedule.

***

### **Key Insights & Analytics**

The unified dataset enables powerful analytics that would otherwise be difficult or impossible to perform. Some key analyses made possible by this pipeline include:

* **Hiring Metrics:** Calculating average **time-to-hire** by department to identify bottlenecks in the recruiting process.
* **Employee Trends:** Analyzing **employee tenure** and its relationship with performance to understand retention patterns.
* **Engagement Analysis:** Exploring the correlation between **engagement survey scores** and key outcomes like **attrition rates** or promotions.

***

### **Key Visualizations & Insights**

The unified dataset was used to build an interactive dashboard in Looker Studio, bringing key HR metrics to life. This dashboard provides a clear, accessible view of the data, enabling stakeholders to quickly identify trends and make data-driven decisions.

Explore the live dashboard and interact with the data here:

[https://lookerstudio.google.com/reporting/b5003a8f-feee-47d6-bbdf-89e96c54f95f]

The dashboard’s visualizations reveal key insights, including:

* **Hiring Trends:** The People Tech department has the longest time-to-hire, while Engineering has the shortest, indicating a need for process optimization in the People Tech team.

* **Employee Retention:** HR Generalists and Data Analysts have the longest average tenure, suggesting high retention in these roles.

* **Compensation vs. Engagement:** The Product department has the highest engagement score, while Engineering has the lowest despite having the highest average compensation. This suggests that compensation alone is not a primary driver of engagement.


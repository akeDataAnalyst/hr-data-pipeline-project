import pandas as pd
from google.cloud import bigquery
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the IDs from the environment variables
PROJECT_ID = os.getenv('GCP_PROJECT_ID')
DATASET_ID = os.getenv('BIGQUERY_DATASET_ID')
TABLE_ID = os.getenv('BIGQUERY_TABLE_ID')

# Set the project ID for the BigQuery client
os.environ['GOOGLE_CLOUD_PROJECT'] = PROJECT_ID

def extract_data():
    """Reads data from CSV files and returns pandas DataFrames."""
    print("Extracting data from CSV files...")
    ats_df = pd.read_csv('ats_data.csv')
    hris_df = pd.read_csv('hris_data.csv')
    survey_df = pd.read_csv('survey_data.csv')
    print("Data extraction complete.")
    return ats_df, hris_df, survey_df

def transform_data(ats_df, hris_df, survey_df):
    """Cleans, transforms, and merges the datasets."""
    print("Transforming data...")

    # Data Cleaning and Type Conversion
    # Convert date columns to datetime objects for accurate calculations
    ats_df['application_date'] = pd.to_datetime(ats_df['application_date'])
    ats_df['hired_date'] = pd.to_datetime(ats_df['hired_date'])
    hris_df['start_date'] = pd.to_datetime(hris_df['start_date'])
    survey_df['survey_date'] = pd.to_datetime(survey_df['survey_date'])

    # Feature Engineering 
    # 1. Calculate time-to-hire from ATS data for successful hires
    ats_hired_df = ats_df[ats_df['hiring_outcome'] == 'Hired'].copy()
    ats_hired_df['time_to_hire_days'] = (ats_hired_df['hired_date'] - ats_hired_df['application_date']).dt.days

    # 2. Calculate employee tenure from HRIS data
    hris_df['tenure_days'] = (pd.to_datetime('today') - hris_df['start_date']).dt.days

    # Data Merging 
    # Merge HRIS and Survey data on employee_id
    unified_df = pd.merge(hris_df, survey_df, on='employee_id', how='left')
    
    # Now, join the HRIS and ATS data using the shared employee_id
    unified_df = pd.merge(unified_df, ats_hired_df[['candidate_id', 'hiring_outcome', 'time_to_hire_days']].rename(columns={'candidate_id': 'employee_id'}), on='employee_id', how='left')

    # Handle missing values after merge
    unified_df['engagement_score'].fillna(-1, inplace=True)
    unified_df['time_to_hire_days'].fillna(-1, inplace=True)
    unified_df['hiring_outcome'].fillna('Not Applicable', inplace=True)
    
    print("Data transformation complete. Unified dataset shape:", unified_df.shape)
    return unified_df


def load_data(df, dataset_id, table_id):
    """Loads the DataFrame into a Google BigQuery table."""
    print(f"Loading data into BigQuery table {dataset_id}.{table_id}...")
    client = bigquery.Client()

    # Configure the table schema to ensure correct data types in BigQuery
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE") # WRITE_TRUNCATE overwrites the table

    # Load the DataFrame to BigQuery
    job = client.load_table_from_dataframe(df, f"{dataset_id}.{table_id}", job_config=job_config)
    job.result()  # Wait for the job to complete
    print("Data loaded successfully into BigQuery.")

# Main Execution Block
if __name__ == '__main__':
    ats_data, hris_data, survey_data = extract_data()
    unified_data = transform_data(ats_data, hris_data, survey_data)

    # Pass the variables to the load function
    load_data(unified_data, DATASET_ID, TABLE_ID)
    print("\nETL Pipeline execution finished successfully!")


from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import etl_pipeline

def run_etl():
    etl_pipeline.clean_data("data/raw_data.csv", "data/cleaned_data.csv")

def upload_cleaned_data():
    os.system("python upload_to_s3.py")

def load_into_snowflake():
    """Placeholder for Snowflake loading step."""
    print("Data loaded into Snowflake")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG(
    'softball_etl_dag',
    default_args=default_args,
    schedule_interval='@daily'
)

etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl,
    dag=dag
)

upload_task = PythonOperator(
    task_id='upload_cleaned_data',
    python_callable=upload_cleaned_data,
    dag=dag
)

snowflake_task = PythonOperator(
    task_id='load_into_snowflake',
    python_callable=load_into_snowflake,
    dag=dag
)

etl_task >> upload_task >> snowflake_task

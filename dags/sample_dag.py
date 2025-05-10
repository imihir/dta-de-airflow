from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
#abcd
# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id='simple_python_dag',
    default_args=default_args,
    description='A simple DAG with Python functions',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['example']
) as dag:

    def start_task():
        print("Starting the DAG")

    def process_task():
        print("Processing data...")

    def end_task():
        print("Ending the DAG")

    start = PythonOperator(
        task_id='start_task',
        python_callable=start_task
    )

    process = PythonOperator(
        task_id='process_task',
        python_callable=process_task
    )

    end = PythonOperator(
        task_id='end_task',
        python_callable=end_task
    )

    # Set task dependencies
    start >> process >> end

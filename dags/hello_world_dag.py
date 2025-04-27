from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
}

with DAG(
    dag_id="hello_world",
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval="@once",  # run once
    catchup=False,
    tags=["example"],
) as dag:

    say_hello = BashOperator(
        task_id="say_hello", bash_command='/bin/bash -c "echo Hello, Airflow!"'
    )

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
}

with DAG(
    dag_id="hello_tasks_dag",
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval="@once",
    catchup=False,
    tags=["example"],
) as dag:

    task1 = BashOperator(
        task_id="task_1",
        bash_command='/bin/bash -c "sleep 10 && echo Task 1 completed!"',
    )

    task2 = BashOperator(
        task_id="task_2",
        bash_command='/bin/bash -c "sleep 10 && echo Task 2 completed!"',
    )

    task3 = BashOperator(
        task_id="task_3",
        bash_command='/bin/bash -c "sleep 10 && echo Task 3 completed!"',
    )

    # No dependencies between tasks: they run IN PARALLEL

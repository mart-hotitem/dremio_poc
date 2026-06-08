from __future__ import annotations
import pendulum
from airflow.decorators import dag, task

# 1. The @dag decorator defines the DAG
@dag(
    dag_id="hello_world_taskflow",
    start_date=pendulum.datetime(2025, 1, 1, tz="Europe/Berlin"),
    schedule=None,
    catchup=False,
    tags=["example", "taskflow"],
)
def hello_world_dag():
    # 2. The @task decorator turns a function into a task
    @task
    def say_hello():
        print("Hello from a TaskFlow task!")
        return "Hello World"

    @task
    def say_world(message: str):
        print(f"The first task says: {message}")
        print("Workflows make orchestration easy!")

    # 3. Dependencies are inferred from function calls
    message_from_hello = say_hello()
    say_world(message_from_hello)

# This line is needed to make the DAG visible to Airflow
hello_world_dag()
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

def print_hello():
    print("Hello people!")

with DAG(dag_id="pythonoperator",
         description="Our first DAG with PythonOperator",
         schedule_interval="@once",
         start_date=datetime(2022, 8, 1)) as dag:
    
    t1 = PythonOperator(task_id="hello_with_python",
                        python_callable=print_hello)
    t1
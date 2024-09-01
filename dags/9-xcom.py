from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = { "depends_on_past": True }

def myfunction(**context):
    print(context["ti"].xcom_pull(task_ids='task2'))
    task2 = context["ti"].xcom_pull(task_ids='task2')
    print(int(task2) - 24)

with DAG(dag_id="9-xcom",
         description="Testing Xcom",
         schedule_interval="@once",
         start_date=datetime(2024, 5, 1),
         end_date=datetime(2024, 8, 1),
         default_args=default_args,
         max_active_runs=1) as dag:
    
    t1 = BashOperator(task_id="task1",
                      bash_command="sleep 2 && echo $((3 * 4))")
    
    t2 = BashOperator(task_id="task2",
                      bash_command="sleep 3 && echo {{ ti.xcom_pull(task_ids='task1') }}")
    
    t3 = PythonOperator(task_id="task3",
                        python_callable=myfunction)
    
    t1 >> t2 >> t3
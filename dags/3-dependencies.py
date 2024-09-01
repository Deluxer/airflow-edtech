from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def print_hello():
    print("Hello people!")

with DAG(dag_id="dependencies",
         description="Our first DAG creating dependencies between taks",
         schedule_interval="@once",
         start_date=datetime(2022, 8, 1)) as dag:
    
    t1 = PythonOperator(task_id="task1",
                        python_callable=print_hello)
    
    t2 = BashOperator(task_id="task2",
                      bash_command="echo task 2")
    
    t3 = BashOperator(task_id="task3",
                     bash_command="echo task 3")

    t4 = BashOperator(task_id="task4",
                     bash_command="echo task 4")
    
    # t1.set_downstream(t2)
    # t2.set_downstream([t3, t4])

    t1 >> t2 >> [t3, t4]
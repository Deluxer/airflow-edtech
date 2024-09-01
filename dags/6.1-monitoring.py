from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def myfunction():
    pass

with DAG(dag_id="6.1-monitoring",
         description="Monitorig the execution of task",
         schedule_interval="@daily",
         start_date=datetime(2024, 1, 1),
         end_date=datetime(2024, 2, 1)) as dag:
    
    t1 = BashOperator(task_id="task1",
                      bash_command="sleep 2 && echo 'first task'")
    
    t2 = BashOperator(task_id="task2",
                      bash_command="sleep 2 && echo 'second task'")
    
    t3 = BashOperator(task_id="task3",
                      bash_command="sleep 2 && echo 'third task'")
    
    t4 = PythonOperator(task_id="task4",
                        python_callable=myfunction)
    
    t5 = BashOperator(task_id="task5",
                      bash_command="sleep 2 && echo 'five task'")

t1 >> t2 >> t3 >> t4
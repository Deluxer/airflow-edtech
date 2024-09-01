from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(dag_id="5.3-orquestation",
         description="Testing the orquestation of tasks",
         schedule_interval="@monthly",
         start_date=datetime(2024, 1, 1),
         end_date=datetime(2024, 10, 1)) as dag:
    
    t1 = EmptyOperator(task_id="task1")
    
    t2 = EmptyOperator(task_id="task2")

    t3 = EmptyOperator(task_id="task3")
    
    t4 = EmptyOperator(task_id="task4")
    
    t1 >> t2 >> t3 >> t4
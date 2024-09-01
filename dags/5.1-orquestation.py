from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="orquestation",
         description="Testing the orquestation of tasks",
         schedule_interval="@daily",
         start_date=datetime(2024, 8, 1),
         end_date=datetime(2024, 9, 1),
         default_args={"depends_on_past": True},
         max_active_runs=1) as dag:
    
    t1 = BashOperator(task_id="task1",
                      bash_command="echo task 1")
    
    t2 = BashOperator(task_id="task2",
                      bash_command="echo task 2")

    t3 = BashOperator(task_id="task3",
                      bash_command="echo task 3")
    
    t4 = BashOperator(task_id="task4",
                      bash_command="echo task 4")
    
    t1 >> t2 >> [t3, t4]
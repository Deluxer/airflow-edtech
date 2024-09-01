from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="7.1-ExternalTaskSensor",
         description="External Task Sensor",
         schedule_interval="@daily",
         start_date=datetime(2024, 5, 1),
         end_date=datetime(2024, 8, 1)) as dag:
    
    t1 = BashOperator(task_id="task1",
                      bash_command="sleep 10 && echo 'first task finished'",
                      depends_on_past=True)
    
    t1
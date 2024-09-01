from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

with DAG(dag_id="7.3-FileSensor",
         description="File Sensor",
         schedule_interval="@daily",
         start_date=datetime(2024, 5, 1),
         end_date=datetime(2024, 8, 1)) as dag:
    
    t1 = BashOperator(task_id="creating_file",
                      bash_command="sleep 10 && touch /tmp/airflow-file-sensor.txt",
                      depends_on_past=True)
    
    t2 = FileSensor(task_id="waiting_file",
                    filepath="/tmp/airflow-file-sensor.txt",
                    depends_on_past=True)
    
    t3 = BashOperator(task_id="end_task",
                      bash_command="echo 'processed file successfuly'")
    
    t1 >> t2 >> t3
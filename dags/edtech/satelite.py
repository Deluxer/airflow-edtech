from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 5, 1),
    'end_date': datetime(2024, 6, 1)
}

with DAG(dag_id="EdTech-Satellite",
         description="Satellite Data collect",
         schedule_interval="0 7 * * 1",
         default_args=default_args) as dag:
    
    SatelliteData = BashOperator(task_id="satellite_data",
                                     bash_command="sleep 5 && echo 'Satellite data available'")

    SatelliteData
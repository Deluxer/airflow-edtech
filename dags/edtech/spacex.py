from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

default_args = {
    'start_date': datetime(2024, 5, 1),
    'end_date': datetime(2024,6, 1)
}

with DAG(dag_id="EdTech-SpaceX-API",
         description="Space X data",
         schedule_interval="0 7 * * 1",
         default_args=default_args) as dag:
    
    SpaceXData = BashOperator(task_id="space_x_data",
                            bash_command="sleep 5 && echo 'Space X data Available'")

    SpaceXData
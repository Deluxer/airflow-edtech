from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.python import PythonOperator
from time import sleep

default_args = {
    'start_date': datetime(2024, 5, 1),
    'end_date': datetime(2024, 6, 1)
}

def nasa_authorization():
    sleep(5)

    return True

with DAG(dag_id="EdTech-Nasa",
         description="Nasa authorization message",
         schedule_interval="0 7 * * 1",
         default_args=default_args) as dag:
    
    Authorization = PythonOperator(task_id="authorization",
                                   python_callable=nasa_authorization)

    AuthorizationMessage = BashOperator(task_id="nasa_authorization",
                                        bash_command="sleep 3 && echo 'NASA Authorization successful'")
    
    Authorization >> AuthorizationMessage
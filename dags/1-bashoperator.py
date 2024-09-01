from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="bashoperator",
        description="Bash operator",
        start_date=datetime(2022, 8, 1)) as dag:
    
    t1 = BashOperator(task_id="hello_with_bash",
                      bash_command="echo 'Hello world'")
    t1
from airflow import DAG
from datetime import datetime
from hellooperator import HelloOperator

with DAG(dag_id="customoperator",
         description="Our first customn operator",
         start_date=datetime(2024, 8, 1)) as dag:
    
    t1 = HelloOperator(task_id="hello",
                       name="fredy")
    t1
from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

def myfunction():
    raise Exception

default_args = {}

with DAG(dag_id="6.2-monitoring",
         description="Monitorig the execution of task",
         schedule_interval="@daily",
         start_date=datetime(2024, 1, 1),
         end_date=datetime(2024, 6, 1),
         default_args=default_args,
         max_active_runs=1) as dag:
    
    t1 = BashOperator(task_id="task1",
                      bash_command="sleep 2 && echo 'first task'",
                      trigger_rule=TriggerRule.ALL_SUCCESS,
                      retries=2,
                      retry_delay=5,
                      depends_on_past=False)
    
    t2 = BashOperator(task_id="task2",
                      bash_command="sleep 2 && echo 'second task'",
                      trigger_rule=TriggerRule.ALL_SUCCESS,
                      retries=2,
                      retry_delay=5,
                      depends_on_past=True)
    
    t3 = BashOperator(task_id="task3",
                      bash_command="sleep 2 && echo 'third task'",
                      trigger_rule=TriggerRule.ALWAYS,
                      retries=2,
                      retry_delay=5,
                      depends_on_past=True)
    
    t4 = PythonOperator(task_id="task4",
                        python_callable=myfunction,
                        trigger_rule=TriggerRule.ALL_SUCCESS,
                        retries=2,
                        retry_delay=5,
                        depends_on_past=True)
    
    t5 = BashOperator(task_id="task5",
                      bash_command="sleep 2 && echo 'five task'",
                      trigger_rule=TriggerRule.ALL_SUCCESS,
                      retries=2,
                      retry_delay=5,
                      depends_on_past=True)

t1 >> t2 >> t3 >> t4 >> t5
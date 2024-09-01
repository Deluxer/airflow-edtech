from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

template_command = """
{% for file in params.filenames %}
    echo "{{ ds }}"
    echo "{{ file }}"
{% endfor %}
"""

with DAG(dag_id="8-Template",
         description="DAG Template",
         schedule_interval="@daily",
         start_date=datetime(2024, 5, 1),
         end_date=datetime(2024, 8, 1),
         max_active_runs=2) as dag:
    
    t1 = BashOperator(task_id="task1",
                      bash_command=template_command,
                      params={"filenames": ["file1.txt", "file2.txt"]},
                      depends_on_past=True)
    
    t1
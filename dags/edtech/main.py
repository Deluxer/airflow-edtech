from airflow import DAG
from datetime import datetime
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.trigger_rule import TriggerRule

default_args = {
    'start_date': datetime(2024, 5, 1),
    'end_date': datetime(2024, 6, 1),
    'max_active_runs':1
}

def send_notification():
    return ['SendNotificationMarketingTeam', 'SendNotificationAnalysisTeam']

with DAG(dag_id="EdTech",
         description="EdTech Collect information",
         schedule_interval="0 7 * * 1",
         default_args=default_args,) as dag:
    
    AuthorizationNASARetrieved = ExternalTaskSensor(task_id="AuthorizationNASARetrieved",
                                     external_dag_id="EdTech-Nasa",
                                     external_task_id="nasa_authorization",
                                     trigger_rule= TriggerRule.ALL_SUCCESS,
                                     poke_interval=10,
                                     depends_on_past=True)
    
    SatelliteDataRetrieved = ExternalTaskSensor(task_id="SatelliteDataRetrieved",
                                     external_dag_id="EdTech-Satellite",
                                     external_task_id="satellite_data",
                                     trigger_rule= TriggerRule.ALL_SUCCESS,
                                     poke_interval=10,
                                     depends_on_past=True)
    
    CreateSatelliteFilesReport = BashOperator(task_id="CreatingSatelliteFilesReport",
                                bash_command="sleep 5 && touch /tmp/satellite_data_report.txt",
                                trigger_rule= TriggerRule.ALL_SUCCESS,
                                depends_on_past=True)
    
    SpaceXDataRetrieved = ExternalTaskSensor(task_id="SpaceXDataRetrieved",
                                    external_dag_id="EdTech-SpaceX-API",
                                    external_task_id="space_x_data",
                                    trigger_rule= TriggerRule.ALL_SUCCESS,
                                    poke_interval=10,
                                    depends_on_past=True)
    
    CreateSpaceXFilesReport = BashOperator(task_id="CreatingSpaceXFilesReport",
                            bash_command="sleep 5 && touch /tmp/space_x_data_report.txt",
                            trigger_rule= TriggerRule.ALL_SUCCESS,
                            depends_on_past=True)
    
    SendNotification = BranchPythonOperator(task_id="SendNotification",
                                            trigger_rule= TriggerRule.ALL_SUCCESS,
                                            python_callable=send_notification)
    
    SendNotificationMarketingTeam = BashOperator(task_id="SendNotificationMarketingTeam",
                                        bash_command="sleep 4 && echo 'Marketing: Data information is available'")
    
    SendNotificationAnalysisTeam = BashOperator(task_id="SendNotificationAnalysisTeam",
                                    bash_command="sleep 4 && echo 'Analysis: Data information is available'")
     
    AuthorizationNASARetrieved >> SatelliteDataRetrieved  >> CreateSatelliteFilesReport >> SpaceXDataRetrieved >> CreateSpaceXFilesReport >> SendNotification >> [SendNotificationMarketingTeam, SendNotificationAnalysisTeam]
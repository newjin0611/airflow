from airflow.sdk import DAG
import datetime
import pendulum

from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_operator",  # airflow 에서 보이는 값. 왠만하면 파일명이랑 일치 시키는게 좋다
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False, # 그러나 과거 실행 시, 순차적으로 x
) as dag:
    
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOST",
    )

    bash_t1 >> bash_t2
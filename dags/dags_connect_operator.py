from airflow.sdk import DAG
import datetime
import pendulum

from airflow.providers.standard.operators.empty import EmptyOperator


with DAG(
    dag_id="dags_connect_operator",  # airflow 에서 보이는 값. 왠만하면 파일명이랑 일치 시키는게 좋다
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False, # 그러나 과거 실행 시, 순차적으로 x
) as dag:
    t1 = EmptyOperator(
        task_id="t1"
    )

    t2 = EmptyOperator(
        task_id="t2"
    )

    t3 = EmptyOperator(
        task_id="t3"
    )    

    t4 = EmptyOperator(
        task_id="t4"
    )  

    t5 = EmptyOperator(
        task_id="t5"
    )

    t6 = EmptyOperator(
        task_id="t6"
    )

    t7 = EmptyOperator(
        task_id="t7"
    )

    t8 = EmptyOperator(
        task_id="t8"
    )

    t1 >> [t2, t3] >> t4
    t5 >> t4
    [t4, t7] >> t6 >> t8
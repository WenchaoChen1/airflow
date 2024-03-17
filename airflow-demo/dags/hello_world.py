from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
# 这里导入业务逻辑模块
from business_logic import process_business_logic, process_business_a

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'hello_world',
    default_args=default_args,
    description='A simple DAG to print "Hello, World!"',
    schedule_interval='@once',
)

t1 = BashOperator(
    task_id='print_hello_world',
    bash_command='echo "Hello, World!"',
    dag=dag,
)

def process_business_a1():
    file_name = process_business_a()
    return file_name

t2 = PythonOperator(
    task_id='process_business_a',
    python_callable=process_business_a1,
    dag=dag,
)
t1 >> t2
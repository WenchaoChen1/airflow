from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# 定义默认参数
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 15),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# 定义 DAG
dag = DAG(
    'multi_task_demo',
    default_args=default_args,
    description='A simple DAG with multiple tasks',
    schedule_interval=timedelta(days=1)
)

# 定义任务1
task1 = BashOperator(
    task_id='task1',
    bash_command='echo "Executing Task 1"',
    dag=dag
)

# 定义任务2
task2 = BashOperator(
    task_id='task2',
    bash_command='echo "Executing Task 2"',
    dag=dag
)

# 定义任务3
task3 = BashOperator(
    task_id='task3',
    bash_command='echo "Executing Task 3"',
    dag=dag
)

# 定义任务4
task4 = BashOperator(
    task_id='task4',
    bash_command='echo "Executing Task 4"',
    dag=dag
)

# 定义任务5
task5 = BashOperator(
    task_id='task5',
    bash_command='echo "Executing Task 5"',
    dag=dag
)

# 定义任务之间的依赖关系
task1 >> [task2, task3]
task2 >> task4
task3 >> task4
[task4, task5]

if __name__ == "__main__":
    dag.cli()

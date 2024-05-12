from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd
import subprocess

# Extraction function
def extract():
    print("-----------Extracting data------------")
    sources = ['https://www.dawn.com/', 'https://www.bbc.com/']
    articles = []
    for source in sources:
        response = requests.get(source)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            if link.text:
                articles.append({
                    'source': source,
                    'title': link.text.strip(),
                    'url': link['href']
                })
    df = pd.DataFrame(articles)
    df.to_csv('/tmp/extracted_articles.csv', index=False)
    return '/tmp/extracted_articles.csv'

# Transformation function
def transform():
    print("-----------Transforming data------------")
    df = pd.read_csv('/tmp/extracted_articles.csv')
    df.drop_duplicates(subset=['url'], inplace=True)
    df.dropna(subset=['title'], inplace=True)
    df.to_csv('/tmp/transformed_articles.csv', index=False)
    return '/tmp/transformed_articles.csv'

# Load function
def load():
    print("-----------Storing data------------")
    try:
        # Add the transformed file to DVC
        subprocess.run(['dvc', 'add', 'transformed_articles.csv'], check=True)
        # Push the data to the remote DVC storage
        subprocess.run(['dvc', 'push', '-r', 'myremote'], check=True)
        print("Data stored successfully!")
    except Exception as e:
        print(f"Error storing data: {str(e)}")


# Airflow DAG definitions
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'simple_mlops_dag',
    default_args=default_args,
    description='A simple DAG for data processing with DVC',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

task1 = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag
)

task2 = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag
)

task3 = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag
)

# Setting up dependencies
task1 >> task2 >> task3

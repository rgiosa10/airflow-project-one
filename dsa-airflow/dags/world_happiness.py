from datetime import timedelta, datetime

from airflow import DAG

from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago # handy scheduling tool
import pandas as pd
import os
import sys
import json
import random

default_args = {
    'start_date': days_ago(1), # The start date for DAG running. This function allows us to set the start date to two days ago
    'schedule_interval': timedelta(days=1), # How often our DAG will run. After the start_date, airflow waits for the schedule_interval to pass then triggers the DAG run
    'retries': 1, # How many times to retry in case of failure
    'retry_delay': timedelta(seconds=15), # How long to wait before retrying
}


def extract_transform():
    #path = os.path.abspath(__file__)
    #dir_name = os.path.dirname(path)

    #df = pd.read_csv(f"{dir_name}/data/2019.csv", index_col='Overall rank',header=0)

    df = pd.read_csv(f"/opt/airflow/dags/data/2019.csv", header=0)

    country = list(df['Country or region'])
    rank = list(df['Overall rank'])

    country_rank_dict = dict(zip(country,rank))
    
    counter = 1
    for item in range(3):
        choice_key = random.choice(list(country_rank_dict))
        choice_value = country_rank_dict[choice_key]
        choice_dict = dict(zip(choice_key,choice_value))

        with open(f"/opt/airflow/dags/data/country_rank_choice_{counter}.json", 'w') as outfile:
            json.dump(choice_dict, outfile)
        counter += 1
        del country_rank_dict[choice_key]

def first_choice():
    choice = pd.read_json("/opt/airflow/dags/data/country_rank_choice_1.json")
    for key, value in choice.items():
        print(f"{key} has an overall rank of {value} ")

def second_choice():
    choice = pd.read_json("/opt/airflow/dags/data/country_rank_choice_2.json")
    for key, value in choice.items():
        print(f"{key} has an overall rank of {value} ")

def third_choice():
    choice = pd.read_json("/opt/airflow/dags/data/country_rank_choice_3.json")
    for key, value in choice.items():
        print(f"{key} has an overall rank of {value} ")

    #first_choice = random.choice(list(country_rank_dict))
    #second_choice = random.choice(list(country_rank_dict))
    #third_choice = random.choice(list(country_rank_dict))







with DAG(
    'world_happiness_index', # a unique name for our DAG
    description='ETL DAG for world_happiness_index csv to json', # a description of our DAG
    default_args=default_args, # pass in the default args.
) as dag:
    et_task = PythonOperator(
        task_id = 'extract_transform',
        python_callable= extract_transform
    )

    first_choice_task = PythonOperator(
        task_id = 'first_choice',
        python_callable= first_choice,
    )

    second_choice_task = PythonOperator(
        task_id = 'second_choice',
        python_callable= second_choice,
    )

    third_choice_task = PythonOperator(
        task_id = 'third_choice',
        python_callable= third_choice,
    )

    et_task >> [first_choice_task, second_choice_task, third_choice_task]
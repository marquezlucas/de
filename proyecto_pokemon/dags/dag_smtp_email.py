from datetime import datetime
from email import message
from airflow.models import DAG, Variable
from airflow.operators.python_operator import PythonOperator



# Importa las bibliotecas necesarias
from datetime import datetime, timedelta
from email import message
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator  # Importa DummyOperator

# Importa la función desde el otro DAG
from scripts.conexion_carga_datos_tabla import cargar_datos_pokemon_to_redshift


import smtplib

def enviar():
    try:
        x=smtplib.SMTP('smtp.gmail.com',587)
        x.starttls()
        x.login('marquezlucasa@gmail.com','')
        subject='Ganaste un premio'
        body_text='Has ganado un premio fantastico!!!!'
        message='Subject: {}\n\n{}'.format(subject,body_text)
        x.sendmail('marquezlucasa@gmail.com','marquezlucas1511@gmail.com',message)
        print('Exito')
    except Exception as exception:
        print(exception)
        print('Failure')

default_args_email={
    'owner': 'tuki',
    'start_date': datetime(2023,12,24)
}

with DAG(
    dag_id='dag_smtp_email',
    default_args=default_args_email,
    schedule_interval='@daily',
    default_view='tree'  # o 'graph', 'duration', 'gantt', 'landing_times'
)as dag:

# Definir tarea para enviar el correo
    tarea_envio = PythonOperator(
        task_id='dag_envio',
        python_callable=enviar,
    )

# Usar DummyOperator como punto de conexión entre ambos DAGs
    dummy_operator = DummyOperator(
        task_id='dummy_operator'
    )

# Establecer la relación de dependencia entre las tareas
    dummy_operator >> tarea_envio
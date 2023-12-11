import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
# Importar funciones desde el script de conexión y carga de datos
from scripts.conexion_carga_datos_tabla import cargar_datos_pokemon_to_redshift

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

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
    'pokemon_dag',
    default_args=default_args,
    description='DAG para obtener y cargar datos de Pokémon en Redshift',
    schedule_interval=timedelta(days=1),
)

# Definir tarea para obtener datos de Pokémon
task_obtener_datos = PythonOperator(
    task_id='obtener_datos_pokemon',
    python_callable=cargar_datos_pokemon_to_redshift,
    provide_context=True,
    op_args=[],  # No necesitas proporcionar conn y cur aquí
    dag=dag,
)
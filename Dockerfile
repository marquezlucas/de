FROM python:3.8

# Instalar dependencias
RUN pip install pandas requests psycopg2-binary apache-airflow

# Establecer el directorio de trabajo
WORKDIR /

# Copiar scripts y archivos SQL al contenedor
COPY scripts/ /scripts/
COPY sql/ /sql/
COPY dags/ /opt/airflow/dags/

# Configurar variables de entorno Airflow
ENV AIRFLOW_HOME /airflow

# Inicializar Airflow
RUN airflow initdb

# Exponer el puerto 8080 para la interfaz web de Airflow
EXPOSE 8080

# Comando para iniciar Airflow
CMD ["airflow", "webserver", "--host", "0.0.0.0", "--port", "8080"]
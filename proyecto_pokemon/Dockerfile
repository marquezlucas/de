FROM apache/airflow:2.3.3-python3.8

ADD webserver_config.py /opt/airflow/webserver_config.py

# Configurar variables de entorno Airflow
ENV AIRFLOW_HOME /airflow

# Copiar la carpeta dags al contenedor
COPY dags/ /opt/airflow/dags/

# Exponer el puerto 8080 para la interfaz web de Airflow
EXPOSE 8080

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow

RUN pip install yfinance
RUN pip install psycopg2-binary
RUN pip install sendgrid

# Comando para iniciar Airflow
CMD ["airflow", "webserver", "--host", "0.0.0.0", "--port", "8080"]
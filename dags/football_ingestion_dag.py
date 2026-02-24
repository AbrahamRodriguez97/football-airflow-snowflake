from airflow.decorators import dag, task
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime
from include.extract_data import get_football_data 

# Define temporary path within the Airflow container
TMP_FILE = '/usr/local/airflow/include/football_data_upload.csv'

@dag(
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=['portfolio', 'data-engineering', 'snowflake'],
    description='ETL pipeline to ingest soccer data into Snowflake using Airflow'
)
def football_data_pipeline():

    @task
    def extract():
        """Task to extract data using Python and Pandas."""
        get_football_data(TMP_FILE)
        return TMP_FILE

    # Upload local file to Snowflake Internal Stage
    upload_to_stage = SQLExecuteQueryOperator(
        task_id='upload_to_stage',
        conn_id='snowflake_conn',
        sql=f"PUT file://{TMP_FILE} @futbol_db.raw.futbol_stage AUTO_COMPRESS=TRUE;"
    )

    # Copy data from Stage to the final Raw table
    load_to_table = SQLExecuteQueryOperator(
        task_id='load_to_table',
        conn_id='snowflake_conn',
        sql="""
            COPY INTO futbol_data (league_name, country, season)
            FROM @futbol_stage
            FILE_FORMAT = (TYPE = 'CSV' FIELD_DELIMITER = ',')
            FORCE = TRUE;
        """
    )

    # Set task dependencies
    extract() >> upload_to_stage >> load_to_table

football_data_pipeline()
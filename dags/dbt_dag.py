from datetime import datetime
# pyrefly: ignore [missing-import]
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
# pyrefly: ignore [missing-import]
from cosmos.profiles import SnowflakeUserPasswordProfileMapping


conn_id = "snowflake-conn"
account = "YSYDFOC-DV76763"
warehouse = "DBT_WH"
database = "DBT_DB"
schema = "DBT_SCHEMA"




profile_config = ProfileConfig(
    profile_name="airflow",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id=conn_id,
        profile_args={
            "account": account,
            "database": database,
            "schema": schema,
            "warehouse": warehouse,
        },
    ),
)

dbt_snowflake= DbtDag(
    project_config= ProjectConfig('/usr/local/airflow/data_pipeline'),
    operator_args={'install_deps':True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path='/usr/local/airflow/dbt_venv/bin/dbt',dbt_project_dir='/usr/local/airflow/data_pipeline'),
    schedule=None,
    start_date=datetime(2026, 6, 4),
    catchup=False,
    dag_id="dbt_dag",
)

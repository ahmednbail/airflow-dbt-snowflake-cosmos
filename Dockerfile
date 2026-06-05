FROM astrocrpublic.azurecr.io/runtime:3.2-5

RUN pip install --no-cache-dir uv

COPY dbt-requirements.txt .

RUN uv venv dbt_venv && \
    uv pip install --no-cache-dir --python dbt_venv/bin/python -r dbt-requirements.txt


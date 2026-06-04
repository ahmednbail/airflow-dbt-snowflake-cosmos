FROM astrocrpublic.azurecr.io/runtime:3.2-5

RUN pip install --no-cache-dir uv

COPY dbt-requirements.txt .

RUN uv venv dbt_venv && \
    . dbt_venv/bin/activate && \
    uv pip install --no-cache-dir -r dbt-requirements.txt


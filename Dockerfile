FROM python:3.8

ENV JSONPATH=/app/cfg/config.json
ENV SQLPATH=

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY sql /app/sql

ENTRYPOINT [ "python" ]
CMD /app/sql/admin.py ${JSONPATH} ${SQLPATH}

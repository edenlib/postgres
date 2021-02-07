FROM python:3.8

ENV JSONPATH=/app/cfg/config.json

COPY sql /app/sql

ENTRYPOINT [ "python" ]
CMD /app/sql/admin.py ${JSONPATH}

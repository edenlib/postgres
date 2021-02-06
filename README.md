## Postgres Configuration
Create a database instance called `postgres-test`.
```shell
$ podman pull postgres:latest
$ podman run --name postgres-test -e POSTGRES_PASSWORD=password -d -p 192.168.0.20:5432:5432 postgres:latest
```

Set up the back-end for Airflow using `postgres/sql/create_database_airflow.sql`.

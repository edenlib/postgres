# Postgres Configuration
Contains database configuration files, SQL, and an admin tool for Airflow.

## Create Eden database
Create a PostgreSQL instance called `postgres-test`.
```shell
$ podman pull postgres:latest
$ podman run --name postgres-test -e POSTGRES_PASSWORD=password -d -p 192.168.0.20:5432:5432 postgres:latest
```

Or, use `launch_postgres.sh` to run the container instead.
```shell
$ ./launch_postgres.sh
```

## Quickstart: SQL admin tool
First, clone and enter into this repository.
```shell
$ cd ~/github/edenlib
$ git clone git@github.com:edenlib/postgres.git
$ cd postgres
```

### Docker
Next, build and run the container image.
```shell
$ podman build --tag db_admin:1.0 .
$ podman run -it --rm -e \
    JSONPATH=/home/adam/cfg/postgres-test.json \
    SQLPATH=/app/sql/database_airflow.sql \
    db_admin:1.0
```

### Bare-metal
Or, use `admin.py` to establish a database connection and execute sql.
```shell
(env)$ python sql/admin.py /home/adam/cfg/postgres-test.json sql/database_airflow.sql
```

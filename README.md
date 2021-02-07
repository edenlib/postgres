# Postgres Configuration
Contains configuration files and object mapping for Eden databases.

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

## Quickstart: Management tool
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
$ podman run -it --rm -e JSONPATH=/home/adam/cfg/postgres-test.json db_admin:1.0
```

### Bare-metal
Or, use `admin.py` to establish a database connection.
```shell
(env)$ python sql/connect.py /home/adam/cfg/postgres-test.json
```

### `admin.py`
You are now in editing environment. Feel feel to make any changes.
```shell
-> print("COMMITTING...")
(Pdb) update_yahoo_finance(curs)
```

At any time, exit and discard any changes with `q`.
```shell
(Pdb) q
Traceback (most recent call last):
...
```

Commit your changes with `continue`.
```shell
(Pdb) continue
COMMIT
...
```

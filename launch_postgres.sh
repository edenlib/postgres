# sets the default user to `postgres` and password to `password`
podman run --name postgres-test -e POSTGRES_PASSWORD=password -d -p 192.168.0.20:5432 postgres:latest
podman ps 

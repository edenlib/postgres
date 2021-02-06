-- creates the db back-end for airflow
create database airflow;
create user airflow with password 'airflow';
grant all privileges on database airflow to airflow;

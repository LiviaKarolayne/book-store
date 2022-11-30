FROM mysql:5.7
EXPOSE 3306
ADD ./db/db.sql /docker-entrypoint-initdb.d
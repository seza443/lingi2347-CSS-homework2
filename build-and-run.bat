

echo "Building and starting Postgresql with our SQL dump"
cd postgresql
docker build -t my-postgresql .
cd ..
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d my-postgresql

echo "Building docker image called my-apache2"
docker build -t my-apache2 .

echo "Starting my-apache2"
docker run -i -t --rm -p 80:80 --link some-postgres:postgres --name my-running-app my-apache2

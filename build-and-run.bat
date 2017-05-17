echo "Building docker image called my-apache2"
docker build -t my-apache2 .

echo "Starting my-apache2"
docker run -i -t --rm -p 80:80 --name my-running-app my-apache2

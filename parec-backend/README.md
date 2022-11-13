##  Dockerfile

## Build Docker Image

$ docker build -t myimage .

## Start Docker Container

$ docker run -d --name mycontainer -p 8080:8000 myimage
--or with random Containername
$ docker run -d -p 8080:8000 myimage
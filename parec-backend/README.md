##  Dockerfile

## Build Docker Image

$ docker build -t myimage .

## Start Docker Container

$ docker run -d --name mycontainer -p 8080:80 myimage
--or with random Containername
$ docker run -d -p 8080:80 myimage
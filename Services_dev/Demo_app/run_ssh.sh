#!/bin/bash

# -d Run container in background and print container ID
# -p Publish a container's port(s) to the host. http-8080:80 ssh-8022:22
# -v /etc/localtime:/etc/localtime:ro make sure docker's time syncs with that of the host
# --name=@ specify the name of the container(opencv_base); the image you want to run the container from (here opencv_baseimage); 

IMAGE_NAME="demo_node"
CONTAINER_NAME="demo-service"

OPERATION=$1

# List container
if  [ "list" == "$OPERATION" ] ; then
	echo "List all containers!"
	docker container ls

# Start container
elif [ "start" == "$OPERATION" ] ; then
	docker run -d --rm \
		-p 8080:80 \
		-p 8022:22 \
		-v /etc/localtime:/etc/localtime:ro \
		--name=$CONTAINER_NAME $IMAGE_NAME 
# Stop container		
elif [ "stop" == "$OPERATION" ] ; then
	docker container stop $CONTAINER_NAME
else
	echo "Usage $0 list|start|stop|!"
fi

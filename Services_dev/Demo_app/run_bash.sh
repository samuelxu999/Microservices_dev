#!/bin/bash

# -i sets up an interactive session; -t allocates a pseudo tty; --rm makes this container ephemeral
# -v /etc/localtime:/etc/localtime:ro make sure docker's time syncs with that of the host 
# --name=@ specify the name of the container (here rdev); the image you want to run the container from (here ubuntu-r); the process you want to run in the container (here bash). (The last step of specifying a process is only necessary if you have not set a default CMD or ENTRYPOINT for your image.)

IMAGE_NAME="demo_node"
CONTAINER_NAME="demo-service"

# execute docker run command
docker run -i -t --rm \
	-p 8080:80 \
	--privileged=true \
	-v /etc/localtime:/etc/localtime:ro \
	--name=$CONTAINER_NAME $IMAGE_NAME /bin/bash

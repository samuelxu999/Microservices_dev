#!/bin/bash

# -d Run container in background and print container ID
# -p Publish a container's port(s) to the host. http-8080:80 ssh-8022:22
# -v /etc/localtime:/etc/localtime:ro make sure docker's time syncs with that of the host 
# --name=@ specify the name of the container(opencv_base); the image you want to run the container from (here opencv_baseimage); 

IMAGE_NAME="geth_node"
# CONTAINER_NAME="geth-client"

OPERATION=$1
CONTAINER_NAME=$2
SSH_PORT=$3
RPC_PORT=$4
PORT=$5

# List container
if  [ "list" == "$OPERATION" ] ; then
	echo "List all containers!"
	docker container ls

# Start container
elif [ "start" == "$OPERATION" ] ; then
	if ! [[ $SSH_PORT =~ ^[0-9]+$ ]]; then
		echo "Error: ssh_port should be integer!"
		exit 0
	fi

	if ! [[ $RPC_PORT =~ ^[0-9]+$ ]]; then
		echo "Error: rpc_port should be integer!"
		exit 0
	fi

	if ! [[ $PORT =~ ^[0-9]+$ ]]; then
		echo "Error: port should be integer!"
		exit 0
	fi

	docker run -d --rm \
		-p $SSH_PORT:22 \
		-p $RPC_PORT:8042 \
		-p $PORT:30303 \
		-v /etc/localtime:/etc/localtime:ro \
		-v $CONTAINER_NAME:/home/docker/account \
		-v $(pwd)/node_data:/home/docker/node_data \
		--name=$CONTAINER_NAME $IMAGE_NAME 
# Stop container		
elif [ "stop" == "$OPERATION" ] ; then
	docker container stop $CONTAINER_NAME
else
	echo "Usage $0 list|start|stop| -container_name -ssh_port -rpc_port -port!"
fi

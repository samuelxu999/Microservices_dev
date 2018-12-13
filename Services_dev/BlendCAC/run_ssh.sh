#!/bin/bash

# -d Run container in background and print container ID
# -p Publish a container's port(s) to the host
# --name=@ specify the name of the container(opencv_base); the image you want to run the container from (here opencv_baseimage); 

IMAGE_NAME="geth_node"
CONTAINER_NAME="ethereum-node"
VOLUME_ACCOUNT="gethAccount"

OPERATION=$1
RPC_PORT=$2
PORT=$3

# List container
if  [ "list" == "$OPERATION" ] ; then
	echo "List all containers!"
	docker container ls

# Start container
elif [ "start" == "$OPERATION" ] ; then
	if ! [[ $RPC_PORT =~ ^[0-9]+$ ]]; then
		echo "Error: rpcport should be integer!"
		exit 0
	fi

	if ! [[ $PORT =~ ^[0-9]+$ ]]; then
		echo "Error: port should be integer!"
		exit 0
	fi

	docker run -d --rm \
		-p 8022:22 \
		-p $RPC_PORT:8042 \
		-p $PORT:30303 \
		-v $VOLUME_ACCOUNT:/home/docker/account \
		-v $(pwd)/node_data:/home/docker/node_data \
		--name=$CONTAINER_NAME $IMAGE_NAME
# Stop container		
elif [ "stop" == "$OPERATION" ] ; then
	docker container stop $CONTAINER_NAME
else
	echo "Usage $0 list|start|stop| -rpcport -port!"
fi

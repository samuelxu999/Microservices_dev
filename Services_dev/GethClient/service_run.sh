#!/bin/bash

##-------------- Run constainer as background service given args ------------------------------------

OPERATION=$1
CONTAINER_NAME=$2
IMAGE_TYPE=$3
SSH_PORT=$4
RPC_PORT=$5
PORT=$6

## Check container name
if [[ "" == $2 ]]; then
	CONTAINER_NAME="geth-client"
	echo "Use default container name: $CONTAINER_NAME"
fi

## Start container
if  [ "start" == "$OPERATION" ] ; then
	echo "Startup service!"

	## validate parameters
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

	## Check image type name
	if [ "x86" == $IMAGE_TYPE ]; then
		echo "Use x86 version"
		IMAGE_FILE="samuelxu999/geth_node:x86"
	elif [ "arm" == $IMAGE_TYPE ]; then
		echo "Use armv7l version"
		IMAGE_FILE="samuelxu999/geth_node:armv7l"
	else
		echo "Not support image version."
		exit 0
	fi

	## prepare docker image
	docker pull "$IMAGE_FILE"
	docker tag "$IMAGE_FILE" geth_node

	## bootup container node
	./run_ssh.sh start $CONTAINER_NAME $SSH_PORT $RPC_PORT $PORT

	## run geth as node
	./docker_exec.sh $CONTAINER_NAME docker /home/docker/geth_cmd/startgeth.sh &>/dev/null &

## Stop container
elif [ "stop" == "$OPERATION" ] ; then
	echo "Stop running service!"
	./run_ssh.sh stop $CONTAINER_NAME
## List container
else
	echo "Show running service!"
	./run_ssh.sh list
fi

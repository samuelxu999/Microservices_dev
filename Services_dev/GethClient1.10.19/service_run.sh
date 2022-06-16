#!/bin/bash

##-------------- Run constainer as background service given args ------------------------------------

OPERATION=$1
CONTAINER_NAME=$2
IMAGE_TYPE=$3
SSH_PORT=$4
RPC_PORT=$5
PORT=$6
MINE=$7

## Check container name
if [[ "" == $2 ]]; then
	CONTAINER_NAME="geth-client1.10.19"
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
		IMAGE_FILE="samuelxu999/geth_node_1.10.19:x86"
	elif [ "arm" == $IMAGE_TYPE ]; then
		echo "Use armv7l version"
		IMAGE_FILE="samuelxu999/geth_node_1.10.19:armv7l"
	else
		echo "Not support image version."
		exit 0
	fi

	## prepare docker image
	docker pull "$IMAGE_FILE"
	docker tag "$IMAGE_FILE" geth_node_1.10.19

	## bootup container node
	./run_ssh.sh start $CONTAINER_NAME $SSH_PORT $RPC_PORT $PORT

	if  [ "mine" == "$MINE" ] ; then
		## run geth as miner by using 1 core
		./docker_exec.sh $CONTAINER_NAME docker /home/docker/geth_cmd/startminer.sh &>/dev/null &
	else
		## run geth as node without mining
		./docker_exec.sh $CONTAINER_NAME docker /home/docker/geth_cmd/startnode.sh &>/dev/null &
	fi

## Stop container
elif [ "stop" == "$OPERATION" ] ; then
	echo "Stop running service!"
	./run_ssh.sh stop $CONTAINER_NAME

## List container
elif [ "show" == "$OPERATION" ] ; then
	echo "Show running service!"
	docker container ls

## Show usage
else
	echo "Usage $0 -operation(start|stop|show) -container_name(geth-client@id) -image_type(x86|arm) -ssh_port(8022) -rpc_port(8042) -port(30305) mine"
fi

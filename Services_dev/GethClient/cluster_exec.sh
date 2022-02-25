#!/bin/bash

## ============= Run cluster by launching multiple containerized geth nodes given args ==============
OPERATION=$1
NODE_NUM=$2
CMD=$3
SSH_PORT=$4
RPC_PORT=$5
PORT=$6


CONTAINER_NAME="geth-client"

if [[ "" == $3 ]]; then
	CMD="pwd"
	echo "Use default cmd value: $CMD"
fi
if [[ "" == $4 ]]; then
	SSH_PORT=8022
	echo "Use default ssh_port value: $SSH_PORT"
fi
if [[ "" == $5 ]]; then
	RPC_PORT=18042
	echo "Use default rpc_port value: $RPC_PORT"
fi
if [[ "" == $6 ]]; then
	PORT=30305
	echo "Use default port value: $PORT"
fi

## Start cluster
if  [ "start" == "$OPERATION" ] ; then
	## validate parameters
	if ! [[ $NODE_NUM =~ ^[0-9]+$ ]]; then
		echo "Error: node_num should be integer!"
		exit 0
	fi

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

	## sequential launch geth client container
	for i in $(seq 1 $NODE_NUM); do 
		echo "Startup container: $CONTAINER_NAME$i!"
		port_idx=$((i-1))
		sudo ./service_run.sh start $CONTAINER_NAME$i x86 $((SSH_PORT+port_idx)) $((RPC_PORT+port_idx)) $((PORT+port_idx)) $CMD
	done

## Stop cluster
elif [ "stop" == "$OPERATION" ] ; then
	## validate parameters
	if ! [[ $NODE_NUM =~ ^[0-9]+$ ]]; then
		echo "Error: node_num should be integer!"
		exit 0
	fi

	## sequential stop geth client container
	for i in $(seq 1 $NODE_NUM); do 
		echo "Shutdowm container: $CONTAINER_NAME$i!"

		sudo ./service_run.sh stop $CONTAINER_NAME$i
	done

## exec cmd inside container
elif [ "exec" == "$OPERATION" ] ; then
	## validate parameters
	if ! [[ $NODE_NUM =~ ^[0-9]+$ ]]; then
		echo "Error: node_num should be integer!"
		exit 0
	fi

	## sequential stop geth client container
	for i in $(seq 1 $NODE_NUM); do 
		echo "Enable mining for: $CONTAINER_NAME$i!"

		sudo ./docker_exec.sh $CONTAINER_NAME$i docker "$CMD"
	done

## List cluster
else
	echo "Show running geth client!"
	sudo ./run_ssh.sh list | grep $CONTAINER_NAME
fi


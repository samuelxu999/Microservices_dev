#!/bin/bash

IMAGE_NAME="geth_node"

OPERATION=$1

if [[ "list" == $OPERATION ]]; then
	echo "List image "$IMAGE_NAME" ...!"
	#docker image ls $IMAGE_NAME
	docker image ls
	exit 0
fi

if [[ "make" == $OPERATION ]]; then
	echo "Start make "$IMAGE_NAME" ...!"
	docker build -t $IMAGE_NAME .
	exit 0
fi

if [[ "clean" == $OPERATION ]]; then
	echo "Remove "$IMAGE_NAME" ...!"
	docker image rm -f $IMAGE_NAME
	exit 0
fi

echo "Usage: $0 list|make|clean ...!"

#!/bin/bash

OPERATION=$1
IMAGE_TYPE=$2
IMAGE_NAME=$3

# Check image name
if [[ "" == $3 ]]; then
	IMAGE_NAME="geth_node_1.10.19"
	#echo "Use default image $IMAGE_NAME ...!"
fi

# Liat all image
if [[ "list" == $OPERATION ]]; then
	echo "List image $IMAGE_NAME ...!"
	docker image ls $IMAGE_NAME
	#docker image ls

# Make image
elif [[ "make" == $OPERATION ]]; then
	echo "Start make $IMAGE_NAME ...!"

	## Check image type name
	if [ "x86" == "$IMAGE_TYPE" ]; then
		echo "Use x86 version"
		Docker_file="Dockerfile_x86"
		IMAGE_FILE="samuelxu999/geth_node_1.10.19:x86"
	elif [ "arm" == "$IMAGE_TYPE" ]; then
		echo "Use armv7l version"
		Docker_file="Dockerfile_armv7l"
		IMAGE_FILE="samuelxu999/geth_node_1.10.19:armv7l"
	else
		echo "Not a supported platform."
		exit 0
	fi

	docker build -t $IMAGE_NAME -f $Docker_file .

	docker tag $IMAGE_NAME:latest $IMAGE_FILE

# Clean image given IMAGE_NAME
elif [[ "clean" == $OPERATION ]]; then
	echo "Remove $IMAGE_NAME ...!"
	docker image rm -f $IMAGE_NAME:latest

else
	echo "Usage $0 cmd[list|make|clean|] image_name image_type(x86/arm)"
fi


#!/bin/bash

#This creates a Docker image, which we’re going to tag using -t so it has a friendly name.
# Usage: ./build_img.sh @repository @tag
# Example:  sudo ./build_img.sh myhelloworld x86

if [ "$#" -ne 2 ]
then
	echo "Error: Need both container name and tag name."
	echo "Usage: ./build_img.sh @repository"
	exit 0
fi

if [ "$1" == '' ]
then
	echo "Error: the container name cannot be empty."
	exit 0
fi

if [ "$2" == '' ]
then
	echo "Error: the tag name cannot be empty."
	exit 0
fi

docker build -t "$1":"$2" .

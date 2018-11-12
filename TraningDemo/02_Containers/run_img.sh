#!/bin/bash

#This creates a Docker image, which we’re going to tag using -t so it has a friendly name.
# Usage: ./run_img.sh @repository @tag @mappingPort
# Example:  sudo ./run_img.sh myhellowld x86 4001 

if [ "$#" -ne 3 ]
then
	echo "Error: Need container name, tag name and mapping port."
	echo "Usage: ./build_img.sh @repository @mappingPort"
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

if [ "$3" == '' ]
then
	echo "Error: mapping port number cannot be empty."
	exit 0
fi

docker run -p "$3":80 "$1":"$2"

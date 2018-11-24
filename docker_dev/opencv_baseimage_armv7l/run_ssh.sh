#!/bin/bash

# -d Run container in background and print container ID
# -p Publish a container's port(s) to the host
# --name=@ specify the name of the container(opencv_base); the image you want to run the container from (here opencv_baseimage); 


docker run -d --rm \
-p 8022:22 \
--name opencv_base opencv_baseimage

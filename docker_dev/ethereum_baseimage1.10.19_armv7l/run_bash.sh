#!/bin/bash

# -i sets up an interactive session; -t allocates a pseudo tty; --rm makes this container ephemeral
# sets the host display to the local machines display (which will usually be :0)
# -u specify the process should be run by a user (here docker) and not by root. This step is important (v.i.)!
# --name=@ specify the name of the container (here rdev); the image you want to run the container from (here ubuntu-r); the process you want to run in the container (here bash). (The last step of specifying a process is only necessary if you have not set a default CMD or ENTRYPOINT for your image.)

xhost +local:docker
docker run -i -t --rm \
	-p 8022:22 \
	-u docker \
	--name="ethereum_base" ethereum_baseimage_1.10.19 /bin/bash

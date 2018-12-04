#!/bin/bash

# -i sets up an interactive session; -t allocates a pseudo tty; --rm makes this container ephemeral
# -u specify the process should be run by root. This step is important (v.i.)!
# --device grand docker access right to host devices 
# --name=@ specify the name of the container (here rdev); the image you want to run the container from (here ubuntu-r); the process you want to run in the container (here bash). (The last step of specifying a process is only necessary if you have not set a default CMD or ENTRYPOINT for your image.)

docker run -i -t --rm \
	-p 8080:80 \
	-u root \
	--device /dev/video0 \
	--name="live_video" live_video /bin/bash
#!/bin/bash

# -d Run container in background and print container ID
# -p Publish a container's port(s) to the host
# --device grand docker access right to host devices 
# --name=@ specify the name of the container(live_video); the image you want to run the container from (here live_video);

docker run -d --rm \
	-p 8080:80 \
	--device /dev/video0 \
	--name "live_video" live_video
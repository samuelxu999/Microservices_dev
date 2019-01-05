#!/bin/bash

OPERATION=$1

# Start container
if  [ "start" == "$OPERATION" ] ; then
	echo "Startup service!"
	# bootup container node
	./run_ssh.sh start 8142 30305

	# run geth as node
	./docker_exec.sh blendcac-service docker /home/docker/geth_cmd/startnode.sh &>/dev/null &

	# run sshd to start ssh server
	./docker_exec.sh blendcac-service root /home/docker/geth_cmd/sshd_start.sh &>/dev/null &

# Stop container
elif [ "stop" == "$OPERATION" ] ; then
	echo "Stop running service!"
	./run_ssh.sh stop
# List container
else
	echo "Show running service!"
	./run_ssh.sh list
fi

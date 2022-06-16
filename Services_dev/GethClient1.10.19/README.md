# GethClient
This docker image built on samuelxu999/ethereum_baseimage_1.10.19:(x86 or armv7l)  to act as blockchain node to work as Geth client

The overview of contents of project are:

## Dockerfile
The Dockerfile defines all ethereum environment and account inside your container.

Before build docker, run $dos2unix geth_cmd/*.sh to transfer scripts to unix format to avoid runtime error.

## geth_cmd

|   source   | Description |
|:----------:|-------------|
| init_account.sh | initialize node configuration given 'genesis.json'.|
| startgeth.sh | startup node wihout unlock account |
| startminer.sh | startup node as miner and unlock base account |
| startnode.sh | startup node as node without mining and unlock base account.|



## node_data

|   source   | Description |
|:----------:|-------------|
| genesis.json | genesis data for private blockchain network initialization. |
| static-nodes.json | Global record for all paired static nodes information on private entereum network. Copy all or part of static nodes information to each account folder to configurate pared nodes. |
| password.sec | Default to new account. Only used for test.|


## build.sh

After executing build.sh, the docker image geth_node_1.10.19 will be built on your local environment.

./service_run.sh make x86 geth_node_1.10.19

## run_ssh.sh 

Run the docker image with ssh interface. After container startup, use ssh to access container:

## run_bash.sh

Run the docker image, just execute run_bash.sh. After container startup, run sample programs in docker CLI to test functionality:

## docker_exec.sh

Run 'docker exec command' to interact with tools and scripts in container.

## service_run.sh

Instruct hwo to run 'docker_exec.sh' to startup services and execute scripts in container.

./service_run.sh start geth-client1 x86 8022 8042 30305 mine

## cluster_exec.sh

This script is used to launch mining cluster on a cloud server.

./cluster_exec.sh start 6 mine

./cluster_exec.sh stop 6

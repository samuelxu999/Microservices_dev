# IndexAuth
This docker image built on ethereum_baseimage  to act as blockchain node to support Time banking service exchange microservices

The overview of contents of project are:

## Dockerfile
The Dockerfile defines all ethereum environment and account inside your container. Change From image based on platform: x86|armv7l

Before build docker, run $dos2unix geth_cmd/*.sh to transfer scripts to unix format to avoid runtime error.

## geth_cmd

|   source   | Description |
|:----------:|-------------|
| init_account.sh | initialize node configuration given 'genesis.json'.|
| startgeth.sh | startup node wihout unlock account |
| startminer.sh | startup node as miner and unlock base account |
| startnode.sh | startup node as node without mining and unlock base account.|
| sshd_start.sh | start sshd service in container |



## node_data

|   source   | Description |
|:----------:|-------------|
| genesis.json | genesis data for private blockchain network initialization. |
| static-nodes.json | Global record for all paired static nodes information on private entereum network. Copy all or part of static nodes information to each account folder to configurate pared nodes. |
| password.sec | Default to new account. Only used for test.|
| addr_list.json | Static node information.|


## app

|   source   | Description |
|:----------:|-------------|
| requirements.txt | dependency requirement for app.|
| src/contracts | smart contract ABI json data |
| SrvExchangeToken.py | This module provide encapsulation of web3.py API to interact with exposed ABI of src/contracts/SrvExchange.json |
| utilities.py | This module provide utility functions to support project. |
| service_utils.py | This module provide RPC functions to support Test_Client. |
| Test_Client.py | This module provide encapsulation of client API that access to Web service. |
| SrvExchange_Server.py | This module provide encapsulation of server API that handle and response client's request. |

## build.sh

After executing build.sh, the docker image live_video will be built on your local environment.

## run_ssh.sh

Run the docker image with ssh interface. After container startup, use ssh to access container:

## run_bash.sh

Run the docker image, just execute run_bash.sh. After container startup, run sample programs in docker CLI to test functionality:

## docker_exec.sh

Run 'docker exec command' to interact with tools and scripts in container.

## service_run.sh

Instruct hwo to run 'docker_exec.sh' to startup services in container.




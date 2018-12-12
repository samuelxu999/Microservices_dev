# BlendCAC
This docker image built on ethereum_baseimage to act as webservice and provide access control services.
The overview of contents of project are:

## Dockerfile
The Dockerfile defines all environmental tools and denpendencies inside your container.

Before build docker, run $dos2unix geth_cmd/*.sh to transfer scripts to unix format to avoid runtime error.

## geth_cmd

|   source   | Description |
|:----------:|-------------|
| init_account.sh | initialize node configuration given 'genesis.json'.|
| startminer.sh | startup node as miner |
| genesis.json | genesis data for private blockchain network initialization. |
| static-nodes.json | Global record for all paired static nodes information on private entereum network. Copy all or part of static nodes information to each account folder to configurate pared nodes. |


## build.sh
After executing build.sh, the docker image live_video will be built on your local environment.

## run_ssh.sh
Run the docker image with ssh interface. After container startup, use ssh to access container:

## run_bash.sh

Run the docker image, just execute run_bash.sh. After container startup, run sample programs in docker CLI to test functionality:





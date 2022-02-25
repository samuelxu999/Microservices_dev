#!/bin/sh

## Set key folder path
KEY_DIR="/home/docker/account/keystore"

## check if main account is available
if ! [ "$(/bin/ls -A $KEY_DIR)" ]; then

	## Initialize miners
	/opt/go-ethereum/build/bin/geth --datadir /home/docker/account init /home/docker/node_data/genesis.json

	## Copy password to docker
	/bin/cp /home/docker/node_data/password.sec /home/docker/account/password.sec

	## Create account based on password.sec
	/opt/go-ethereum/build/bin/geth --datadir /home/docker/account account new --password /home/docker/account/password.sec
fi

## copy static-nodes.json to account folder
/bin/cp /home/docker/node_data/static-nodes.json /home/docker/account/
#--unlock 0 --password ${HOME}/account/password.sec

## launch geth client app
/opt/go-ethereum/build/bin/geth --identity "geth_node" --networkid 42 --datadir "/home/docker/account" --nodiscover --rpc --rpcport "8042" --port "30303" --ipcpath "/home/docker/.ethereum/geth.ipc"
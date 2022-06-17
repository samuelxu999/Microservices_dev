#!/bin/sh

## Set key folder path
KEY_DIR="/home/docker/account/keystore"
Account_dir="/home/docker/account"
Node_dir="/home/docker/node_data"
Eth_path="/opt/go-ethereum/build/bin/geth"

## check if main account is available
if ! [ "$(/bin/ls -A $KEY_DIR)" ]; then
	## new account dir
	/bin/mkdir $Account_dir

	## Initialize miners
	$Eth_path --datadir $Account_dir init $Node_dir/genesis.json

	## Copy password to docker
	/bin/cp $Node_dir/password.sec $Account_dir/password.sec

	## Create account based on password.sec
	$Eth_path --datadir $Account_dir account new --password $Account_dir/password.sec
fi

## copy static-nodes.json to account folder
/bin/cp $Node_dir/static-nodes.json $Account_dir/geth/

## launch geth client app
$Eth_path --identity "geth_node" \
--networkid 2104 \
--datadir "$Account_dir" \
--nodiscover \
--syncmode full \
--gcmode archive \
--http --http.port "8042" \
--port "30303" \
--allow-insecure-unlock \
--unlock 0 \
--password "$Account_dir/password.sec" \
--ipcpath "$HOME/.ethereum/geth.ipc"
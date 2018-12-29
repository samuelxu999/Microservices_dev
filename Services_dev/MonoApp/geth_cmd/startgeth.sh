#!/bin/sh

# copy static-nodes.json to account folder
/bin/cp /home/docker/node_data/static-nodes.json /home/docker/account/
#--unlock 0 --password ${HOME}/account/password.sec

#geth --identity "geth_node" --networkid 42 --datadir "${HOME}/account" --nodiscover --rpc --rpcport "8042" --port "30303" --ipcpath "${HOME}/.ethereum/geth.ipc"
/opt/go-ethereum/build/bin/geth --identity "geth_node" --networkid 42 --datadir "/home/docker/account" --nodiscover --rpc --rpcport "8042" --port "30303" --ipcpath "/home/docker/.ethereum/geth.ipc"
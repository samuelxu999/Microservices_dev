#!/bin/sh

# copy static-nodes.json to account folder
/bin/cp /home/docker/node_data/static-nodes.json /home/docker/account/

/opt/go-ethereum/build/bin/geth --identity "node" --networkid 42 --datadir "/home/docker/account" --nodiscover --rpc --rpcport "8042" --port "30303" --unlock 0 --password /home/docker/account/password.sec --ipcpath "/home/docker/.ethereum/geth.ipc"

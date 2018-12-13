#!/bin/sh

# copy static-nodes.json to account folder
cp ${HOME}/node_data/static-nodes.json ${HOME}/account/

geth --identity "miner" --networkid 42 --datadir "${HOME}/account" --nodiscover --mine --rpc --rpcport "8042" --port "30303" --unlock 0 --password ${HOME}/account/password.sec --ipcpath "${HOME}/.ethereum/geth.ipc"

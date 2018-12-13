#!/bin/sh

geth --identity "miner" --networkid 42 --datadir "${HOME}/account" --nodiscover --rpc --rpcport "8042" --port "30303" --unlock 0 --password ${HOME}/account/password.sec --ipcpath "${HOME}/.ethereum/geth.ipc"

#!/bin/sh

#Delete chaindata for account
/bin/rm -rf /home/docker/account/geth

#Initialize miners
/opt/go-ethereum/build/bin/geth --datadir /home/docker/account init /home/docker/node_data/genesis.json

#Create accounts
#Copy password to docker
/bin/cp /home/docker/node_data/password.sec /home/docker/account/password.sec

#geth --datadir ../account account new
/opt/go-ethereum/build/bin/geth --datadir /home/docker/account account new --password /home/docker/account/password.sec

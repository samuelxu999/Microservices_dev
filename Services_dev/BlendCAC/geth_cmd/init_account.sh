#!/bin/sh

#Delete chaindata for account
rm -rf ../account/geth

#Initialize miners
geth --datadir ../account init genesis.json

#Create accounts
#geth --datadir ../account account new
#geth --datadir ../account account new

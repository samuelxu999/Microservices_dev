#!/bin/bash

OPERATION=$1
IMAGE_NAME=$2

GO_PKG=go1.18.3.linux-armv6l.tar.gz
GETH_PKG=go-ethereum

echo "$GO_PKG"

return 0

## Check image name
if [[ "" == $2 ]]; then
	## "Use default image $IMAGE_NAME ...!"
	IMAGE_NAME="ethereum_baseimage_1.10.19"
fi

## Liat all image
if [[ "list" == $OPERATION ]]; then
	echo "List image $IMAGE_NAME ...!"
	docker image ls $IMAGE_NAME
	#docker image ls

## Make image
elif [[ "make" == $OPERATION ]]; then
	echo "Start make $IMAGE_NAME ...!"

	## fetch go tar to local
	wget "https://storage.googleapis.com/golang/$GO_PKG"

	## pull go-ethereum to local by
	git clone https://github.com/ethereum/go-ethereum.git

	docker build -t $IMAGE_NAME .

	## remove go tar and go-ethereum package
	rm $GO_PKG
	rm -rf $GETH_PKG

## Clean image given IMAGE_NAME
elif [[ "clean" == $OPERATION ]]; then
	echo "Remove $IMAGE_NAME ...!"
	docker image rm -f $IMAGE_NAME

else
	echo "Usage $0 cmd[list|make|clean|] image_name"
fi


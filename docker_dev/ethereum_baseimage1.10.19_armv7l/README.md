# ethereum_baseimage_1.10.19:armv7l
This docker image built on Ubuntu-20.04 and includes: go-1.18.3 and geth-1.10.19.

The overview of contents of project are:

## Dockerfile
The Dockerfile defines all environmental tools and denpendencies inside your container.

## build.sh
After executing build.sh, the docker image ethereum_baseimage_1.10.19 will be built on your local environment.

To share image, you could push 'ethereum_baseimage_1.10.19' image to docker hub.

1) Log in with your Docker ID

$ docker login

2) Tag the image: 

$ docker tag imagename username/repository:tag

For example:

$ docker tag ethereum_baseimage_1.10.19 samuelxu999/ethereum_baseimage_1.10.19:armv7l

3) Publish the imagename by uploading your tagged image to the repository:

$ docker push username/repository:tag

For example:

$ docker push samuelxu999/ethereum_baseimage_1.10.19:armv7l

## run_bash.sh

Run the docker image, just execute run_bash.sh. After container startup, run sample programs in docker CLI to test go and geth:

$ go version

$ geth version

## run_ssh.sh

Run the docker image with ssh interface. After container startup, use ssh to access container:

$ ssh docker@localhost -p 8022

Then input the password: samuelxu999, and log on container.

Stop ethereum_base container, run command:

$ docker container stop ethereum_base

# ethereum_baseimage_armv7l
This docker image built on Ubuntu-16.04 and includes: python2.7, python3.5, go-1.9.3 and geth-1.7.3.

The overview of contents of project are:

## Dockerfile
The Dockerfile defines all environmental tools and denpendencies inside your container.

## build.sh
After executing build.sh, the docker image ethereum_baseimage will be built on your local environment.

To share image, you could push 'ethereum_baseimage' image to docker hub.

1) Log in with your Docker ID

$ docker login

2) Tag the image: 

$ docker tag imagename username/repository:tag

For example:

$ docker tag ethereum_baseimage samuelxu999/ethereum_baseimage:armv7l

3) Publish the imagename by uploading your tagged image to the repository:

$ docker push username/repository:tag

For example:

$ docker push samuelxu999/ethereum_baseimage:armv7l

## run_bash.sh

Run the docker image, just execute run_bash.sh. After container startup, run sample programs in docker CLI to test functionality:

$ go version

$ geth version

## run_ssh.sh

Run the docker image with ssh interface. After container startup, use ssh to access container:

$ ssh docker@localhost -p 8022

Then input the password: samuelxu999, and log on container.

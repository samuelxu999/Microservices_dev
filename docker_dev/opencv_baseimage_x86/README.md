# opencv_baseimage_x86
This docker image built on Ubuntu-16.04 and includes: python2.7, python3.5 and opencv libs 3.4.0.

The overview of contents of project are:

## Dockerfile
The Dockerfile defines all environmental tools and denpendencies inside your container.

## app
The demo sample codes and resources. Executing sample program to verify docker container functionality.

|   source   | Description |
|:----------:|-------------|
| BasicOperationsImages.py | Test core fucntion of opencv |
| face_detect.py | Demonstrate a face detection fucntion in opencv |
| res | Test images |


## build.sh
After executing build.sh, the docker image opencv_baseimage will be built on your local environment.

To share image, you could push 'opencv_baseimage' image to docker hub.

1) Log in with your Docker ID

$ docker login

2) Tag the image: 

$ docker tag imagename username/repository:tag

For example:

$ docker tag opencv_baseimage samuelxu999/opencv_baseimage:x86

3) Publish the imagename by uploading your tagged image to the repository:

$ docker push username/repository:tag

For example:

$ docker push samuelxu999/opencv_baseimage:x86

## run_bash.sh

Run the docker image, just execute run_bash.sh. After container startup, run sample programs in docker CLI to test functionality:

$ python BasicOperationsImages.py

## run_ssh.sh

Run the docker image with ssh interface. After container startup, use ssh to access container:

$ ssh docker@localhost -p 8022

Then input the password: samuelxu999, and log on container.

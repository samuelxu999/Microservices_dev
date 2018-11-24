# myopencv
This docker image includes: python2.7, python3.5 and opencv libs.

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
After executing build.sh, the docker container myopencv will be built on your local environment.

To share image, you could push 'myopencv' image to docker hub.

1) Log in with your Docker ID

$ docker login

2) Tag the image: 

$ docker tag image username/repository:tag

For example:

$ docker tag image samuelxu999/opencv_baseimage:ubuntu_x86

3) Publish the image by uploading your tagged image to the repository:

$ docker push username/repository:tag

For example:

$ docker push samuelxu999/opencv_baseimage:ubuntu_x86

## run_bash.sh

Run the docker contrainer, just execute run_bash.sh. After container startup, run sample programs in docker CLI to test functionality:

$ python BasicOperationsImages.py

## run_ssh.sh

Run the docker contrainer with ssh interface. After container startup, use ssh to attach contrainer:

$ ssh docker@localhost -p 8022

Then input the password: samuelxu999, and log on contrainer.

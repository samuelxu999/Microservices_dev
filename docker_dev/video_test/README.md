# video_test
This docker image built on opencv_baseimage.
The overview of contents of project are:

## Dockerfile
The Dockerfile defines all environmental tools and denpendencies inside your container.

## app
The demo sample codes and resources. Executing sample program to verify docker container functionality.

|   source   | Description |
|:----------:|-------------|
| video_demo.py | Test video and camera play function|
| res | Test video |


## build.sh
After executing build.sh, the docker image opencv_baseimage will be built on your local environment.

## run_bash.sh

Run the docker image, just execute run_bash.sh. After container startup, run sample programs in docker CLI to test functionality:

$ python video_demo.py --video|camera


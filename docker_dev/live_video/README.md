# live_video
This docker image built on opencv_baseimage to act as webservice and provide live camera video streams.
The overview of contents of project are:

## Use RPI camera as a USB video device (Only for Raspberry Pi)
As opencv code use /dev/video0 as videstream source, execute following command to mount RPI camera to /dev/video0. 

sudo modprobe bcm2835-v4l2

## Dockerfile
The Dockerfile defines all environmental tools and denpendencies inside your container.

## app
The demo sample codes and resources.

|   source   | Description |
|:----------:|-------------|
| main.py | Web service main application|
| camera_opencv.py | Camera class to implement frames() function using opencv lib |
| base_camera.py | BaseCamera class to manage camera thread and events |
| requirements.txt | Dependencies for app, such as flask,.etc. |


## build.sh
After executing build.sh, the docker image live_video will be built on your local environment.

## run.sh
Run the docker image, just execute run.sh. After container startup, main.py startup automatically to serve live video.

## run_bash.sh

Run the docker image, just execute run_bash.sh. After container startup, run sample programs in docker CLI to test functionality:

$ python3 main.py

## Show livevideo service
Input livevideo service api address in network blowser, eg:'http://128.226.78.24:8080/' (replace to IP of host machine that runs container.)

## If you want auto-run livevideo service after system bootup, you need add following commands in /etc/rc.local

sudo modprobe bcm2835-v4l2

$(your local directory)/Microservices_dev/docker_dev/live_video/run.sh

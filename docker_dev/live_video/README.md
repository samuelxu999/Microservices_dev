# live_video
This docker image built on opencv_baseimage to act as webservice and provide live camera video streams.
The overview of contents of project are:

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


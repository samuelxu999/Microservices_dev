# Microservices_dev
Microservices based application development.

The overview of organization of project are:

## TraningDemo
The training materials and sample codes, including:

|   source   | Description |
|:----------:|-------------|
| 01_Orientation | Concept orientation and setup for docker. |
| 02_Containers | Contrainer setup instruction. |

## docker_dev
The docker container development, including:

|   source   | Description |
|:----------:|-------------|
| myopencv | Test OpenCV container image for Ubuntu_x86 platform. |
| myopencv_armv7l | Test OpenCV container image for armv7l platform. |
| opencv_baseimage_x86 | OpenCV baseimage from Ubuntu-16.04 on x86 platform. |
| opencv_baseimage_armv7l | OpenCV baseimage image from Debian/Jessie on armv7l platform. |
| video_test | Video test image from opencv_baseimage. Demo how to access local video file and host camera in docker. |
| live_video | live_video image from opencv_baseimage. Demo how to build live video stream web service based on flask. |


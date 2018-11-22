# Use an official Python runtime as a parent image
FROM python:2.7
#FROM python:3.5

# Developer information
MAINTAINER Samuel Xu <samuelxu999@gmail.com>

# ------------- Dependencies and tools installation ----------------
# Install system tools and dependencies
RUN apt-get update && \
	apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
        yasm \
        libgtk2.0-dev \
	pkg-config \
	libavcodec-dev \
	libavformat-dev \
	libswscale-dev \
# clean up
 && apt-get autoremove

# Install python2 tools and configurations
#Run apt-get install -y \
#	python-tk \
#	python-pip \
#	python-dev \
#	python-setuptools

# Install python3 tools and configurations
#Run apt-get install -y \ 
#	python3-tk \
#	python3-pip \
#	python3-dev \
#	python3-setuptools

# Install pip tools and configurations
Run python -m pip install --upgrade pip
#Run python3.5 -m pip install --upgrade pip

# Install numpy
Run python2.7 -m pip install numpy
#Run python3.5 -m pip install numpy

# Install matplotlib
Run python2.7 -m pip install matplotlib
#Run python3.5 -m pip install matplotlib

# Install Qt
#Run apt-get install -y libqt4-dev libvtk5-qt4-dev
Run apt-get install -y qt-sdk

# Optinal dependencies
#Run apt-get install -y libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

# ---------- Building OpenCV from Source Using CMake -----------------
ENV OPENCV_VERSION="3.4.0"
RUN mkdir /opt/src \
&& cd /opt/src \
&& git clone https://github.com/opencv/opencv.git \
&& git clone https://github.com/opencv/opencv_contrib.git \
&& cd /opt/src/opencv_contrib \
&& git checkout ${OPENCV_VERSION} \
&& cd /opt/src/opencv \
&& git checkout ${OPENCV_VERSION} \
&& mkdir /opt/src/opencv/build \
&& cd /opt/src/opencv/build \
&& cmake -D CMAKE_BUILD_TYPE=Release \
	-D WITH_QT=ON \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D OPENCV_TXTRA_MODULES_PATH=/opt/src/opencv_contrib/modules ..\
&& make -j4 \
&& make install \
&& rm -rf /opt/src

# Minimize image size 
RUN apt-get autoremove -y && apt-get autoclean -y

# Make port 22 available to the world outside this container
EXPOSE 22

# ---------------------- Setup docker user account -------------
# Set root passwd 
RUN echo "root:test" | chpasswd

# Add user so that container does not run as root 
RUN useradd -m docker 
RUN echo "docker:test" | chpasswd 
RUN usermod -s /bin/bash docker 
RUN usermod -aG sudo docker 
ENV HOME /home/docker


# -------------------- Add apps to docker ------------------
# Setting up working directory
#RUN su docker
RUN mkdir ${HOME}/app
WORKDIR ${HOME}/app

#Copy the app scripts into the container at /app
COPY ./app/ ${HOME}/app/

# Change owner and group to docker
RUN chown -R docker:docker ${HOME}/app

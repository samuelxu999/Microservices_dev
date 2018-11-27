#!/bin/bash

# This instruction is used for setup docker environment on armv7l platform, such as Raspberry Pi and Tinkerboard 
# Reference: https://docs.docker.com/install/linux/docker-ce/debian/#install-docker-ce-1

#A) ------------- Update package and install dependencies --------------------
#1) Update the apt package index.
sudo apt-get update -y

#2) Install python2 dependency
sudo apt-get install -y \
	python-pip \
	python-dev \
	python-setuptools

#3) Install python3 dependency	
sudo apt-get install -y \
	python3-pip \
	python3-dev \
	python3-setuptools
	
#4) Update pip tools
python -m pip install --upgrade pip && python3 -m pip install --upgrade pip


#A) ------------- Install using the convenient scripts --------------------
# 1) Install Docker:
sudo curl -sSL https://get.docker.com | sh

# 2) Adding your user to the "docker" group with something like:
sudo usermod -aG docker samuel

# 3) Install docker compose:
sudo pip install docker-compose

# B) ---------------- Update docker to specific version  --------------------
#Since convenient scripts will install edge and testing versions of Docker CE, and it will not work on current OS.
# The following step to install a specific version to work properly on host:

#1) To install a specific version of Docker CE, list the available versions in the repo, then select and install:
sudo apt-cache madison docker-ce

#2) Install a specific version by its fully qualified package name, which is package name (docker-ce) “=” version string (2nd column), 
# for example, docker-ce=18.03.0~ce-0~ubuntu
sudo apt-get install -y docker-ce=18.04.0~ce~3-0~debian

#C) ---------------- Verify whether Docker CE installed correctly -----------
# Verification is performed by running the hello-world image.
sudo docker run hello-world

#D) ---------------------  Upadte docer-ce -------------------------------
sudo apt-get update -y

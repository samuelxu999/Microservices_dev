# Use an Ubuntu official image as base image
FROM ubuntu:16.04

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
        unzip 

# ----------------------- Python configuration ----------------------
# Install python2 tools and configurations
Run apt-get install -y \
	python-tk \
	python-pip \
	python-dev \
	python-setuptools

# Install python3 tools and configurations
Run apt-get install -y \
	python3-tk \
	python3-pip \
	python3-dev \
	python3-setuptools

# Install pip tools and configurations
Run python -m pip install --upgrade pip && python3.5 -m pip install --upgrade pip

# ===================================== golang configuration ============================
ARG GO_URL=https://storage.googleapis.com/golang/
ARG GO_PKG=go1.9.3.linux-amd64.tar.gz

# First of all, wget package to local, then copy to docker to extract.
#	wget "$GO_URL""$GO_PKG"

COPY ./"$GO_PKG" /opt/

RUN cd /opt && \
	tar -C /usr/local -xzf "$GO_PKG" && \
	rm -f "$GO_PKG"

# ============================ build go-ethereum from source code ============================
#ARG GETH_URL=https://gethstore.blob.core.windows.net/builds/
#ARG GETH_PKG=geth-linux-amd64-1.8.20-24d727b6.tar.gz
#ARG GETH_MD5=02dbf3cbe10c684a67ca890f647fa0b7

#RUN wget "$GETH_URL""$GETH_PKG" && \
#	tar -C /opt/go-ethereum -xzf "GETH_PKG" && \
#	rm -f "GETH_PKG"

# First of all, pull source code to local by:
# git clone https://github.com/ethereum/go-ethereum.git
# Then Add source code to docker and build. it will save time

ARG GETH_VERSION="v1.7.3"

RUN mkdir /opt/go-ethereum
COPY ./go-ethereum/ /opt/go-ethereum/

# build geth
RUN export PATH=$PATH:/usr/local/go/bin && \
	cd /opt/go-ethereum && \
	git checkout ${GETH_VERSION} && \
	make geth



# ========================================== Install openssh =========================================
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:samuelxu999' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# Minimize image size 
RUN apt-get autoremove -y && apt-get autoclean -y

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# ========================== PATH Configure for root ================== 
# ------------------------- Add GOROOT and append to PATH ---------------
RUN echo 'export GOROOT=/usr/local/go' >> ~/.bashrc && \
	echo 'export PATH=$PATH:$GOROOT/bin' >> ~/.bashrc

# ------------------- Add GOETHEREUM and append to PATH -----------------
RUN echo 'export GOETHEREUM=/opt/go-ethereum/build' >> ~/.bashrc && \
	echo 'export PATH=$PATH:$GOETHEREUM/bin' >> ~/.bashrc

# =========================== Setup docker user account ==================================
# Add user so that container does not run as root 
RUN useradd -m docker 
RUN echo "docker:samuelxu999" | chpasswd 
RUN usermod -s /bin/bash docker 
RUN usermod -aG sudo docker 
ENV HOME /home/docker

# ========================== PATH Configure for docker ================== 
# ------------------------- Add GOROOT and append to PATH ---------------
RUN echo 'export GOROOT=/usr/local/go' >> ~/.bashrc && \
	echo 'export PATH=$PATH:$GOROOT/bin' >> ~/.bashrc

# ------------------- Add GOETHEREUM and append to PATH -----------------
RUN echo 'export GOETHEREUM=/opt/go-ethereum/build' >> ~/.bashrc && \
	echo 'export PATH=$PATH:$GOETHEREUM/bin' >> ~/.bashrc

# Make port 22 available to the world outside this container
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

# Use an Ubuntu official image as base image
FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

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
# Install python3 tools and configurations
Run DEBIAN_FRONTEND=noninteractive apt-get install -y \
	python3-tk \
	python3-pip \
	python3-dev \
	python3-setuptools

# Install pip tools and configurations
Run python3 -m pip install --upgrade pip

# ===================================== golang installation ============================
ARG GO_PKG=go1.18.3.linux-amd64.tar.gz

COPY ./"$GO_PKG" /opt/

RUN cd /opt && \
	tar -C /usr/local -xzf "$GO_PKG" && \
	rm /opt/$GO_PKG

# ============================ build go-ethereum from source code ============================
ARG GETH_VERSION="v1.10.19"

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

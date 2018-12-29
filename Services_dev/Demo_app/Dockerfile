# Use ethereum-basedimage to build service application
FROM samuelxu999/ethereum_baseimage:x86
#FROM samuelxu999/ethereum_baseimage:armv7l


# ============================ app work directory setup =============================
# Setting up working directory
ENV HOME /home/docker

# New account data dir 
RUN mkdir ${HOME}/app
#Copy scripts into the container at ${HOME}/app
COPY ./app/ ${HOME}/app/
RUN chown -R docker:docker ${HOME}/app

# ----------- Install requirements ------------
#RUN python -m pip install -r ${HOME}/app/requirements.txt
RUN apt-get update -y
RUN apt-get install -y nano libssl-dev libffi-dev
RUN python3 -m pip install -r ${HOME}/app/requirements.txt

# Minimize image size 
RUN apt-get autoremove -y && apt-get autoclean -y

WORKDIR ${HOME}/app

# bootnode port
EXPOSE 80

#Default command
CMD ["./WS_Server.py"]


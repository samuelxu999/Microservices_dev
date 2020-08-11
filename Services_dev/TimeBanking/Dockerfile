# Use ethereum-basedimage to build service application
FROM samuelxu999/ethereum_baseimage:x86
#FROM samuelxu999/ethereum_baseimage:armv7l

# ============================ geth work directory setup =============================
# Setting up working directory
ENV HOME /home/docker

# New account data dir 
RUN mkdir ${HOME}/account
RUN chown -R docker:docker ${HOME}/account

# ================ Configure geth_cmd dir to save geth command scripts ===============
RUN mkdir ${HOME}/geth_cmd
RUN chown -R docker:docker ${HOME}/geth_cmd

# -------------------- Add geth_cmd to docker ------------------
#Copy the geth command scripts into the container at ${HOME}/geth_cmd
COPY ./geth_cmd/ ${HOME}/geth_cmd/

# Change owner and group to docker
RUN chown -R docker:docker ${HOME}/geth_cmd
RUN chmod +x ${HOME}/geth_cmd/*.sh

# ============================ app work directory setup =============================
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

WORKDIR ${HOME}/app/src

# bootnode port
EXPOSE 30303
EXPOSE 8042
EXPOSE 80

#Default command
CMD ["./SrvExchange_Server.py"]
#ENTRYPOINT ["${HOME}/geth_cmd/startminer.sh"]

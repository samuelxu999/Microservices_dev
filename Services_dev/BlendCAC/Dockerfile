# Use ethereum-basedimage to build service application
FROM samuelxu999/ethereum_baseimage:x86
#FROM samuelxu999/ethereum_baseimage:armv7l

# ================================ Install Independencies =============================
#RUN python3 -m pip install flask
#RUN python -m pip install -r requirements.txt
#RUN python3 -m pip install -r requirements.txt

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

WORKDIR ${HOME}

# bootnode port
EXPOSE 30303
EXPOSE 8042

#Default command
#CMD ["/home/docker/geth_cmd/startminer.sh"]
#ENTRYPOINT ["${HOME}/geth_cmd/startminer.sh"]
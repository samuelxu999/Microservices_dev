# Use opencv-based image
FROM samuelxu999/opencv_baseimage:x86


# -------------------- Add apps to docker ------------------
# Setting up working directory
ENV HOME /home/docker
RUN mkdir ${HOME}/test
WORKDIR ${HOME}/test

#Copy the app scripts into the container at /app
COPY ./app/ ${HOME}/test/

# Change owner and group to docker
RUN chown -R docker:docker ${HOME}/test
# Use opencv-based image given platform
FROM samuelxu999/opencv_baseimage:x86

# -------------------- Add apps to docker ------------------
# Setting up working directory
ENV HOME /home/docker
RUN mkdir ${HOME}/livevideo
WORKDIR ${HOME}/livevideo

#Copy the app scripts into the container at /app
COPY ./app/ ${HOME}/livevideo/

# -------------------- Install Independencies ------------------
#RUN python3 -m pip install flask
RUN python3 -m pip install -r requirements.txt

# Change owner and group to docker
RUN chown -R docker:docker ${HOME}/livevideo
RUN chmod +x ./main.py

#Expose port 80
EXPOSE 80
#Default command
CMD ["./main.py"]
# List stacks or apps
docker stack ls

# Before we can use the docker stack deploy command we first run: 
docker swarm init

# Run the specified Compose file                                            
# docker stack deploy -c <composefile> <appname>  
docker stack deploy -c docker-compose.yml myhelloworld

# List running services associated with an app
docker service ls 

# List tasks associated with an app                
# docker service ps <service>
# the same as execute:  docker container ls     
docker service ps myhelloworld_web 

# Inspect task or container
# docker inspect <task or container>    
docker inspect myhelloworld_web  

# List container IDs             
docker container ls -q    

# Tear down an application                                  
# docker stack rm <appname>
docker stack rm myhelloworld 

# Take down a single node swarm from the manager                        
docker swarm leave --force      

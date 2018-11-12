## Containers
The sample codes that built a docker container to demonstrate basic helloworld app.

Refer to official documentation by Docker: 
https://docs.docker.com/get-started/part2/


### Build and run shell
--- build_img.sh: build docker image given repository and tag. 
		Usage: ./build_img.sh @repository @tag
		Example:  sudo ./build_img.sh myhelloworld x86

--- run_img.sh: run docker image to launch container
		Usage: ./run_img.sh @repository @tag @mappingPort
		Example:  sudo ./run_img.sh myhellowld x86 4001 
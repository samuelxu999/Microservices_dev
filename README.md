# Microservices_dev
Microservices based application development.

The overview of organization of project are:

## TraningDemo
The training materials and sample codes, including:

|   source   | Description |
|:----------:|-------------|
| 01_Orientation | Concept orientation and setup for docker. |
| 02_Containers | Contrainer setup instruction. |

## docker_dev
The docker container development, including:

|   source   | Description |
|:----------:|-------------|
| myopencv | Test OpenCV container image for Ubuntu_x86 platform. |
| myopencv_armv7l | Test OpenCV container image for armv7l platform. |
| opencv_baseimage_x86 | OpenCV baseimage from Ubuntu-16.04 on x86 platform. |
| opencv_baseimage_armv7l | OpenCV baseimage image from Debian/Jessie on armv7l platform. |
| video_test | Video test image from opencv_baseimage. Demo how to access local video file and host camera in docker. |
| live_video | live_video image from opencv_baseimage. Demo how to build live video stream web service based on flask. |
| ethereum_baseimage_x86 | Ethereum baseimage from Ubuntu-16.04 on x86 platform. |
| ethereum_baseimage_armv7l | Ethereum baseimage from Ubuntu-16.04 on armv7l platform. |

## contract_dev
The truffle project folder to develop smart contracts that work as a underlying contract layer on Ethereum blockchain network.

For smart contract development, please refer to [Truffle](https://truffleframework.com/docs) for truffle environment setup and usage. 

* contract:

	--- AuthToken.sol: smart contract for security service AuthID, an ideitity authentication mechanism.

	--- CapACToken.sol: smart contract for security service BlendCAC, an Capability-based AC mechanism.

	--- IndexToken.sol: smart contract for security service IndexAuth, an hashed value integrity verification mechanism.
	
	--- Migrations.sol: This is a separate Solidity file that manages and updates the status of your deployed smart contract. This file comes with every Truffle project, and is usually not edited.
	
* migrations:

	--- 1_initial_migration.js: This file is the migration (deployment) script for the Migrations contract found in the Migrations.sol file.
	
	--- 2_deploy_contracts.js: This file is the migration (deployment) script for deploying our developed smart contract Solidity files.

## Services_dev
The micorservices applications development, including:

|   source   | Description |
|:----------:|-------------|
| AuthID | Identity authentication services for smart public safety system. |
| BlendCAC | Capability based access control services for smart public safety system. |
| Demo_app | Microservices enabled client applicaion for smart public safety system. |
| GethClient | Geth client container to run as a miner or node in Ethereum. |
| IndexAuth | Hashed index authentication services for smart public safety system. |
| MonoApp | Monolithic enabled client applicaion for smart public safety system. |
| SmartSurveillance | Smart surveillance services for video stream analysis. |
| TimeBanking | Service exchange container for Time Banking system. |


#!/usr/bin/env python3.5

'''
========================
Test_Client module
========================
Created on March.17, 2021
@author: Xu Ronghua
@Email:  rxu22@binghamton.edu
@TaskDescription: This module provide FEd-DDM Client app that access to web service of FEd-DDM Server.
'''

import logging
import argparse
import sys
import time

from utilities import FileUtil
from service_utils import SrvExchangeClient

logger = logging.getLogger(__name__)

#global variable
addr_list = '../../node_data/addr_list.json'

  
def test_getBroker(args):
	logger.info("Get broker information.")
	# construct data argument
	data_args = {}
	data_args['host_ip'] = args.host_ip
	# data_args ['host_address'] = node_address


	broker_info = SrvExchangeClient.getBroker(data_args)['data']

	logger.info("Host: account:{} balance:{}".format(broker_info['host']['account'],
                                                    broker_info['host']['balance']) )

	logger.info("Publisher: vid:{} zid: {} status: {} balance:{} txs: {}".format(broker_info['publisher']['vid'], 
	                                                                    broker_info['publisher']['zid'], 
	                                                                    broker_info['publisher']['status'],
	                                                                    broker_info['publisher']['balance'],
	                                                                    broker_info['publisher']['txs']) )

	logger.info("Subscriber: vid:{} zid: {} status: {} balance:{} txs: {}".format(broker_info['subscriber']['vid'], 
	                                                                        broker_info['subscriber']['zid'],
	                                                                        broker_info['subscriber']['status'],
	                                                                        broker_info['subscriber']['balance'],
	                                                                        broker_info['subscriber']['txs']) )

def test_initalizeBroker(args):
	logger.info("Initalize broker data.")
	# construct data argument
	data_args = {} 
	data_args['host_ip'] = args.host_ip

	SrvExchangeClient.initalizeBroker(data_args) 

def test_delegateBroker(args):
	logger.info("Delegate broker for service.")
	# construct data argument
	data_args = {}
	data_args['host_ip'] = args.host_ip
	data_args['op_state'] = args.broker_op

	if(args.broker_op==1):
		node_address = SrvExchangeClient.getAddress("Desk_PI_Plus_Sam2", addr_list)
		data_args['host_address'] = node_address
		data_args['zone_id'] = "zone-2"
		data_args['tx_ref'] = "0xd67b57e6ae47623f"
	else:
		node_address = SrvExchangeClient.getAddress("Desk_PI_Plus_Sam1", addr_list)
		data_args['host_address'] = node_address
		data_args['zone_id'] = "zone-1"  
		data_args['tx_ref'] = "0xea12421586661067"     

	SrvExchangeClient.delegateBroker(data_args)  

def test_updateBroker(args):
	logger.info("Update broker information.")
	# construct data argument
	data_args = {}
	data_args ['host_ip'] = args.host_ip
	data_args['time_currency'] = 3
	data_args['op_state'] = args.broker_op 
	if(args.broker_op==1):
		node_address = SrvExchangeClient.getAddress("Ubuntu18-Dell7010-1", addr_list)
		data_args ['host_address'] = node_address
		data_args['zone_id'] = "zone-4" 
	else:
		node_address = SrvExchangeClient.getAddress("Ubuntu18-Dell7010-1", addr_list)
		data_args['host_address'] = node_address
		data_args['zone_id'] = "zone-3" 
	    

	SrvExchangeClient.updateBroker(data_args) 

def test_commitService(args):
	logger.info("Commit service.")
	# construct data argument
	data_args = {}
	data_args ['host_ip'] = args.host_ip
	data_args['op_state'] = args.broker_op 
	if(args.broker_op==1):
		## subscriber deposit balance
	    data_args['balance'] = 100
	else:
	    data_args['balance'] = 0     

	SrvExchangeClient.commitService(data_args) 

def test_paymentService(args):
	logger.info("Service payment.")
	# construct data argument
	data_args = {}
	data_args ['host_ip'] = args.host_ip     

	SrvExchangeClient.paymentService(data_args)      

  
def define_and_get_arguments(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(
	    description="Run websocket client test."
	)

	parser.add_argument("--service_op", type=int, default=0, 
	                    help="Execute test function: 0-test_getBroker(), \
	                                                1-test_initalizeBroker(), \
	                                                2-test_delegateBroker, \
	                                                3-test_updateBroker \
	                                                4-test_commitService, \
	                                                5-test_paymentService")
	parser.add_argument("--broker_op", type=int, default=0, 
	                    help="broker for service operation: 0-publisher, \
	                                                1-subscriber.")
	parser.add_argument("--host_ip", default='0.0.0.0:8088', type=str, 
						help="server node address format[ip:port].")

	args = parser.parse_args(args=args)
	return args

if __name__ == "__main__":
    # Logging setup
    FORMAT = "%(asctime)s | %(message)s"
    logging.basicConfig(format=FORMAT)
    logger.setLevel(level=logging.DEBUG)

    # serviceUtils_logger = logging.getLogger("service_utils")
    # serviceUtils_logger.setLevel(logging.INFO)

    args = define_and_get_arguments()

    if(args.service_op==1):
        test_initalizeBroker(args)
    elif(args.service_op==2):
        test_delegateBroker(args)
    elif(args.service_op==3):
        test_updateBroker(args)
    elif(args.service_op==4):
        test_commitService(args)
    elif(args.service_op==5):
        test_paymentService(args)
    else:
        test_getBroker(args)
	

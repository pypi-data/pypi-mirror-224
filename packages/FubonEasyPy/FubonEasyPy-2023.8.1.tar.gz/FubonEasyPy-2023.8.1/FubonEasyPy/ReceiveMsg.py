# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 11:06:56 2022

@author: Cheryl.fan
"""
import zmq
import persizmq
import datetime
import logging.config
import threading
import asyncio
import zmq.asyncio
import sys
import nest_asyncio
import pathlib
import unittest
import os
nest_asyncio.apply()  
from .ReplyPy import *
from .QueryPy import *
from .EasyPyEvent import *

logconf_file = os.path.join(os.path.dirname(__file__), 'easypy.config')
logging.config.fileConfig(logconf_file)
logger = logging.getLogger('MainLogger')        
filehandler = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.date.today()))
formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s')
filehandler.setFormatter(formatter)        
logger.addHandler(filehandler)

'''
subscribe Receive: 回報, 查詢
'''
class ReceiveMsg(object):    
    
    def __init__(self, address: str):   
        self.eventhandler = EventsHandler()
        self.address = address
        #self.receiveFlag=0
        #self.persistent_dir = pathlib.Path("/some/dir")
        #self.storage = persizmq.PersistentStorage(persistent_dir=persistent_dir)
        #asyncio.get_event_loop().run_until_complete(asyncio.wait([self.receiveMsg()]))
        
    def runReceive(self):
        self.receiveMsg(self.address)
        
    def receiveMsg(self, address):
        with SubscribeContext() as ctx:
            with ctx.subscriber(url=f"tcp://{address}:5560") as subscriber:                                    
                while True:      
                    with persizmq.ThreadedSubscriber(callback=self.callback, subscriber=subscriber, on_exception=ReceiveMsg.on_exception):                                                
                        pass
                    
                #while True:
                    #with persizmq.ThreadedSubscriber(subscriber=subscriber,callback=SubscribeReceive.callback, on_exception=SubscribeReceive.on_exception):                        
                        #pass
                #print ('接收訊息...')
                #while True:
                    #message = subscriber.recv_multipart()
                    #dataStr=message[0].decode('utf-8')
                    #self.eventhandler.change(dataStr)
                    #print(dataStr)
                    #break
                    #with persizmq.ThreadedSubscriber(callback=SubscribeReceive.callback, subscriber=subscriber, on_exception=SubscribeReceive.on_exception)  :                        
                        #pass
                                                     
    def callback(self, msg: bytes)->None:
        try:           
            #print("pubMsg:", msg.decode('utf-8'))                                                         
            self.eventhandler.change(msg.decode('utf-8'))   
            #dataStr="{}".format(str(msg, 'utf-16'))
            #data=json.loads(dataStr)
            #functionCode=int(data['functionCode'])
            #receiveObj=None
            #if functionCode < 3:
                # receiveObj=ReplyPy(dataStr)
            #else:
                #receiveObj=QueryResponse(dataStr)
            #print(receiveObj.jsonFormat(True))                          
        except Exception as e:
            logger.error("sub error: {}".format(e))   
        return
            
    def on_exception(exception: Exception)->None:
        logger.error("sub error: {}".format(exception))
        
        

"""
subscriber context
"""
class SubscribeContext:
    def __init__(self):       
        self.context = zmq.Context()
        self.subscribers = [] # type: List[zmq.Socket]

    def subscriber(self, url: str) -> zmq.Socket:       
        """
        Creates a new subscriber that listens to whatever the publisher of this instance
        publishes.
        The subscriber will be closed by this instance.
        :return: zmq subscriber
        """
        subscriber = self.context.socket(zmq.SUB)  # pylint: disable=no-member
        self.subscribers.append(subscriber)
        subscriber.setsockopt_string(zmq.SUBSCRIBE, "")  # pylint: disable=no-member
        subscriber.connect(url)
        return subscriber
    
    def __enter__(self):        
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for subscriber in self.subscribers:
            subscriber.close()
        self.context.term()
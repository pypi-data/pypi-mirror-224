# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 17:39:39 2022

@author: Cheryl.fan
"""
import threading
import asyncio
import zmq
import zmq.asyncio
import sys
import nest_asyncio
nest_asyncio.apply()  
from .ReceiveMsg import ReceiveMsg
from .EasyPyEvent import *

'''
send message: 委託, 查詢
'''    
class SendMsg(object):
    queue=asyncio.Queue()
    tasks=[]
    def sub_ReceiveMsg(self, sender, msg):
        self.eventsSUB.change(msg)
        
    def __init__(self, address: str):
        self.eventsSUB = EventsHandler()
        self.eventsREQ = EventsHandler()
        obj = ReceiveMsg(address)
        t1 = threading.Thread(target=obj.runReceive)#self.trade_sub_th)
        t1.start()
        obj.eventhandler.Changed += self.sub_ReceiveMsg        
        context = zmq.asyncio.Context.instance()
        self.socket = context.socket(zmq.REQ)
        self.socket.connect(f"tcp://{address}:5556")           
                
    def msgTo(self, dataStr):
        asyncio.get_event_loop().run_until_complete(asyncio.wait([self.run(dataStr)]))      
               
    async def run(self, dataStr):
        self.queue.put_nowait(dataStr)
        await asyncio.sleep(1)
        task = asyncio.create_task(self.main(self.queue))
        self.tasks.append(task)
        await self.queue.join()
        # Cancel our worker tasks.
        for task in self.tasks:
            task.cancel()
        # Wait until all worker tasks are cancelled.
        await asyncio.gather(*self.tasks, return_exceptions=True)
        return task.result()
        
    #def trade_sub_th(self):
        #contextsub = zmq.Context()
        #self.socket_sub = contextsub.socket(zmq.SUB)
        #socket_sub.RCVTIMEO=5000           #ZMQ超時設定
        #self.socket_sub.connect("tcp://127.0.0.1:5560")
        #self.socket_sub.setsockopt_string(zmq.SUBSCRIBE, "")
        #while True:
            #message =  self.socket_sub.recv()
            #dataStr=message.decode('utf-8')
            #print(dataStr);
        
    async def main(self, queue):
       #while True:
            # Get a "work item" out of the queue.
            msg = await self.queue.get()
            # Sleep for the "sleep_for" seconds.
            await self.main_loop_num(msg)  
            # Notify the queue that the "work item" has been processed.
            queue.task_done()
    
    async def receive(self):
        message = await self.socket.recv_string()
        return message

    async def send(self, msg):
        await self.socket.send(msg.encode('utf-8'))
        print("ReqMsg:", msg)
        
    async def main_loop_num(self, msg):
        await self.send(msg)
        #  Get the reply.
        message = await self.receive()
        self.eventsREQ.change(message)     
    
   
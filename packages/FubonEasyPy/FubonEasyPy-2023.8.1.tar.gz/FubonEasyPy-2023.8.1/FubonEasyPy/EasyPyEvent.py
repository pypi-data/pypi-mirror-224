# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:55:38 2023

@author: vinjent.fan
"""

class Event:
    def __init__(self):
        self.listeners = []
        
    def __call__(self, *params):
        for l in self.listeners:
            l(*params)
            
    def __add__(self, listener):       
        self.listeners.append(listener)        
        return self
    
    def __sub__(self, listener):
        self.listeners.remove(listener)
        return self


class EventsHandler:
   def __init__(self):
      self.Changed = Event()
      
   def change(self, text):
       self.Changed(self, text);

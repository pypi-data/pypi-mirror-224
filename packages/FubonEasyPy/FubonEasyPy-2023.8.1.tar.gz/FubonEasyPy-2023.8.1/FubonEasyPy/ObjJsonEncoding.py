# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:10:56 2022

@author: Cheryl.fan
"""
import json
import inspect

'''
Json Encoding
Json Format
'''
class ObjJsonEncoding(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj)
                if not key.startswith("__")
                and not inspect.isabstract(value)
                and not inspect.isbuiltin(value)
                and not inspect.isfunction(value)
                and not inspect.isgenerator(value)
                and not inspect.isgeneratorfunction(value)
                and not inspect.ismethod(value)
                and not inspect.ismethoddescriptor(value)
                and not inspect.isroutine(value)
                and not inspect.isclass(value)              
            )
            return self.default(d)
        return obj        
    
'''
and not inspect.isasyncgen(value)
and not inspect.isasyncgenfunction(value)
and not inspect.istraceback(value)
and not inspect.isawaitable(value)
and not inspect.iscode(value)
and not inspect.iscoroutine(value)
and not inspect.iscoroutinefunction(value)
and not inspect.isdatadescriptor(value)
and not inspect.isframe(value)
and not inspect.isgetsetdescriptor(value)
and not inspect.ismemberdescriptor(value)
and not inspect.ismodule(value)'''
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:26:51 2019

@author: Rosa
"""

class Node:
    def __init__(self,value = None,pointer = None):
        self.value = value
        self.pointer = pointer
        
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.pointer
    
    def set_value(self, value):
        self.value = value
        
    def set_next(self,pointer):
        self.pointer = pointer
        
bnode = Node(55)
anode = Node(15, bnode)

print(anode.get_next())
 

print(bnode)       
        
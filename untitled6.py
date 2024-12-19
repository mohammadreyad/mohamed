# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:11:25 2024

@author: mohamedmr
"""

class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"   
    def getter (self,__priv):
        self.__priv = __priv
x=A()
print(x.pub)
x.pub= x.pub +" and my value can be changed"
print(x.pub)
print("------------")
print(x._prot)
print("------------")
x.getter
print("the privete method is creat")
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:44:58 2024

@author: mohamedmr
"""

class Pizza:
    def __init__(self,ingredients):
        self.ingredients=ingredients
    
    @classmethod
    def veg(cls):
        return cls(["mushrooms","olives","onion"])
    
    @classmethod
    def margherita(cls):
        return cls(["mozarella","sauce"])

    def __str__(self):
        return f"ingredients are {self.ingredients}"
    
pizza1=Pizza(["tomatos","olives"])
pizza2=Pizza.veg()
pizza3=Pizza.margherita()
print(pizza2,pizza3)

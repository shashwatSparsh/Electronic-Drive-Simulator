#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 13:25:52 2022
Classes
@author: shashwatsparsh
"""

#%%
        
class AirFrame:
    def __init__(self, n, mass):
        self.__n = n # number of arms
        self.__mass = mass # maxx

    @property
    def numArms(self):
        return self.__n
    
    @property
    def mass(self):
        return self.__mass
   
#%%

class FlightComputer:
    def __init__(self, name, mass, current):
        self.__name = name
        self.__current = current
        self.__mass = mass
        
    @property
    def current(self):
        return self.__current
    
    @property
    def mass(self):
        return self.__mass
    

#%%     

class Prop:
    def __init__(self, diameter, pitch, mass):
        self.__pitch = pitch
        self.__diameter = diameter
        self.__mass = mass
        
    @property
    def pitch(self):
        return self.__pitch
    
    @property
    def diameter(self):
        return self.__diameter
    
    @property
    def mass(self):
        return self.__mass
    
#%%
    
class Battery:
    def __init__(self, Voltage, Capacity, C, S, mass):
        self.__Voltage = Voltage
        self.__Capacity = Capacity
        self.__C = C
        self.__S = S
        self.__mass = mass
        
    def getMaxCurrent(self):
        Imax = (self.Capacity * self.C)/1000 # [Amps]
        return Imax
  
    @property
    def Voltage(self):
        return self.__Voltage
    
    @property
    def Capacity(self):
        return self.__Capacity
    
    @property
    def C(self):
        return self.__C
    
    @property
    def S(self):
        return self.__S
    
    @property
    def mass(self):
        return self.__mass

#%%
    
class Motor:
    def __init__(self, Kv, mass, name):
        self.__Kv = Kv
        self.__mass = mass
        self.__name = name
    
    @property
    def Kv(self):
        return self.__Kv    
    
    @property
    def mass(self):
        return self.__mass
    
    @property
    def name(self):
        return self.__name

#%%

class ESC:
    def __init__(self, I, Imax, mass):
        self.__I = I
        self.__Imax = Imax
        self.__mass = mass

    @property
    def I(self):
        return self.__I
    
    @property
    def Imax(self):
        return self.__Imax    
    
    @property
    def mass(self):
        return self.__mass
    
# #%%

# class Configuration:
#     def __init__(self, AirFrame, FlightComputer, Prop, Battery, Motor, ESC):
#         self.__AirFrame = AirFrame
#         self.__FlightComputer = FlightComputer
#         self.__Prop = Prop
#         self.__Battery = Battery
#         self.__Motor = Motor
#         self.__ESC = ESC
    
#     @property
#     def getAUW(self):
        
#         return AU



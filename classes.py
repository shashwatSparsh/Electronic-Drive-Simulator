#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 13:25:52 2022
Classes
@author: shashwatsparsh
"""

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
    
class Motor:
    def __init__(self, Kv, mass):
        self.Kv = Kv
        self.mass = mass
    
    @property
    def Kv(self):
        return self.__Kv    
    
    @property
    def mass(self):
        return self.__mass

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
        

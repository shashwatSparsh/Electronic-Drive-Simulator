#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:30:04 2022
Functions
@author: shashwatsparsh
"""

#%% Imports
import numpy as np
import scipy as sc
import classes.py

#%%
""" Power """

def calcUnloadedRPM(kV: float, Batt: classes.Battery):
    # kV Motor Rating
    # V Battery Voltage
    V = Batt.V
    return kV*V

def calcLoadedRPM(RPM_Unloaded: float):
    # k Efficiency Factor (Guestimate)
    k = 0.75
    return RPM_Unloaded*k

# def calcPower(propConst: float, rpm: float, pFactor: float):
#     # propCons: function of the prop
#     # RPM: 0 load RPM
#     # pFactor: Power Factor
#     return propConst * np.power(float, pFactor)
         
#%%
""" Thrust """

def calcThrustSingle(RPM: float, prop: classes.Prop, V0: float):
    V0 = 0
    d = prop.diameter
    pitch = prop.pitch
    C1 = 4.392399E-8
    C2 = 4.23333E-4
    
    T = C1 * RPM * ((d**3.5)/(pitch**0.5)) * ((C2*RPM*pitch) - V0)
    return T
    
def calcTotalThrust(T: float, n: int):
    # T: Thrust from one Motor
    # n: Number of motors
    return T*n

# def calcThrust(D: float, rho: float, P: float):
#     # D: Prop Diameter in [m]
#     # rho: air density [1255 kg/m^3]
#     # P: Power [W]
#     return np.power(((np.pi/2) * (D**2) * rho * (P**2)), (1/3))

# def calcNoDimThrust(D: float, rho: float, P: float, g: float):
#     # Standard 
#     return (np.power(((np.pi/2) * (D**2) * rho * (P**2)), (1/3))) / g

#%%
""" All Up Weight """

def calcAUW(Batt: classes.Battery)#, airframe: classes.AirFrame, esc: classes.ESC)#, \
#           motor: classes.Motor, prop: classes.Prop)
    
    return 5


#%%
""" Flight Time """

# AAD: Average Amp Draw
def calcAAD(AUW: float, V: float):
    # P: Power required to lift 1kg of equipment
    # 120W/kg is generous
    # 170W/kg is conservative
    # AUW: All up Weight
    # V: Battery Voltage
    Pdot = 170
    return AUW * (Pdot/V)

# Estimated Flight Time of the Aircraft
def calcFlightTime(Capacity: float, Discharge: float, AUW: float, V: float):
    # Capacity: Listed Battery Capacity
    # Discharge: Max Percent Discharge:
    #            Going Beyond 80% Discharge Damages battery
    # AUW: All Up Weight
    AAD = calcAAD(AUW, V)
    return (Capacity * Discharge) / AAD
    
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
import componentObjects as c

#%%
""" All Up Weight + Average Amp Draw """

def AUW(frame: c.AirFrame, flightComp: c.FlightComputer, Batt: c.Battery,\
        motor: c.Motor, ESC: c.ESC, prop: c.Prop):
    # frame = air frame, flightComp = Flight Computer, Batt = Battery
    # motor = motor, ESC = ESC, prop = propeller
    
    n = frame.numArms
    AUW = frame.mass + flightComp.mass + Batt.mass + \
        (n * (motor.mass + ESC.mass + prop.mass))
    
    return AUW;

def AAD(AUW: float, Pdot: float, Batt: c.Battery):
    # Pdot: Power required to lift 1kg of equipment
        # 120W/kg is generous
        # 170W/kg is conservative
    # AUW: All up Weight
    AAD = AUW * (Pdot/Batt.Voltage)
    return AAD
    
#%%
""" Flight Time """

def estFlightTime(Batt: c.Battery, Discharge: float, AAD: float):
    # Capacity: Listed Battery Capacity
    # Discharge: Max Percent Discharge:
    #            Going Beyond 80% Discharge Damages battery
    # AAD: Average Amp Draw
    
    flightTime = ((Batt.Capacity * Discharge)/AAD)*60
    return flightTime
    
#%%
""" Power """

def unloadedRPM(motor: c.Motor, Batt: c.Battery):
    # kV Motor Rating
    # V Battery Voltage
    kV = motor.Kv
    V = Batt.Voltage
    return kV*V

def loadedRPM(unloadedRPM: float, k: float):
    # k Efficiency Factor (Guestimate)
    # k = 0.75
    return unloadedRPM*k

# def calcPower(propConst: float, rpm: float, pFactor: float):
#     # propCons: function of the prop
#     # RPM: 0 load RPM
#     # pFactor: Power Factor
#     return propConst * np.power(float, pFactor)
         
#%%
""" Thrust """

def thrustSingle(RPM: float, prop: c.Prop, V0: float):
    V0 = 0
    d = prop.diameter
    pitch = prop.pitch
    C1 = 4.392399E-8
    C2 = 4.23333E-4
    
    T = C1 * RPM * ((d**3.5)/(pitch**0.5)) * ((C2*RPM*pitch) - V0)
    return T
    
def thrustTotal(T: float, n: int):
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

    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 11:02:05 2022

@author: shashwatsparsh
"""

#%%
#%% Imports
import numpy as np
import scipy as sc
import functions as f
import componentObjects as c
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
import numpy as np
#%%

"""Airframe"""
frame = c.AirFrame(4, 454)

"""Propulsion"""
prop = c.Prop(15, 5.5, 21)

motorVals = [[680, 47, "V2806"], [700, 97, "V3508"], [300, 51, "V4004"], [320, 66, "V4006"], \
             [600, 105, "V4008"]]
motors = []
kVlist = []
motorMassList = []
motorNames = []
for i in range(0, len(motorVals)):
    kV = motorVals[i][0]
    m = motorVals[i][1]
    name = motorVals[i][2]
    kVlist.append(kV)
    motorMassList.append(m)
    motorNames.append(name)
    motors.append(c.Motor(kV, m, name))
    
esc = c.ESC(40, 60, 58)

"""Battery"""
battery = c.Battery(11.1, 5200, 50, 3, 410)

"""Flight Computer"""
flightComputer = c.FlightComputer("Pixhawk", 35, 2.5)

#%%

"""AUW Calculations"""
AUWs  = []
for i in range(0, len(motors)):
    AUWs.append(f.AUW(frame, flightComputer, battery, motors[i], esc, prop))

"""AAD Calculations"""
AADs = []
for i in range(0, len(motors)):
    AADs.append(f.AAD(AUWs[i], 150, battery))
    
"""Flight Time Estimates"""
estFlightTimes = []
for i in range(0, len(motors)):
    estFlightTimes.append(f.estFlightTime(battery, 0.8, AADs[i]))

"""RPM Calculations"""
unloadedRPMs = []
loadedRPMs = []

for i in range(0, len(motors)):
    unloadedRPMs.append(f.unloadedRPM(motors[i], battery))
    loadedRPMs.append(f.loadedRPM(unloadedRPMs[i], 0.9))


"""Thrust Calculations"""
motorThrusts = []
totalThrusts = []

for i in range(0, len(motors)):
    motorThrusts.append(f.thrustSingle(loadedRPMs[i], prop, 0))
    totalThrusts.append(f.thrustTotal(motorThrusts[i], frame.numArms))

"""TWR Calculations"""
TWRs = []
Weights = []

for i in range(0, len(motors)):
    Weights.append(9.81* ((AUWs[i])/1000))
    
for i in range(0, len(motors)):
    TWRs.append(f.TWR(totalThrusts[i], Weights[i]))
    
    
#%%
"""Test Case"""

testFrame = c.AirFrame(4, 454)
testMotor = c.Motor(650, 47, "V2806")
testProp = c.Prop(11, 4.5, 9)
testESC = c.ESC(40, 60, 58)
testBattery = c.Battery(11.1, 5200, 50, 3, 410)
testFC = c.FlightComputer("Pixhawk", 35, 2.5)

testAUW = f.AUW(testFrame, testFC, testBattery, testMotor, testESC, testProp)
testAAD= f.AAD(testAUW, 150, testBattery)
testFlightTime = f.estFlightTime(testBattery, 0.8, testAAD)
testRPM = f.loadedRPM(f.unloadedRPM(testMotor, testBattery), 0.75)
testThrust = f.thrustTotal(f.thrustSingle(testRPM, testProp, 0), testFrame.numArms)
testWeight = f.totalWeight(testFrame, testFC, testBattery, testMotor, testESC, testProp)
testTWR = f.TWR(testThrust, testWeight)

#%%

x_values = np.arange(1, len(motorNames) + 1, 1)

"""Generate Plot 1"""
    
fig, TWRvsMotor = plt.subplots()
plt.grid()
TWRvsMotor.scatter(x_values, TWRs);
plt.xticks(x_values, motorNames, rotation = "horizontal");
TWRvsMotor.set_xlabel("SunnySky Motor Types");
TWRvsMotor.set_ylabel("Thrust to Weight Ratios");
TWRvsMotor.set_title("Thrust to Weight Ratio vs Motor");
plt.show()

"""Generate Plot 2"""

fig, EFTvsMotor = plt.subplots()
plt.grid()
EFTvsMotor.scatter(x_values, estFlightTimes);
plt.xticks(x_values, motorNames, rotation = "horizontal");
EFTvsMotor.set_xlabel("SunnySky Motor Types");
EFTvsMotor.set_ylabel("Estimated Flight Time (mins)");
EFTvsMotor.set_title("Estimated Flight Time vs Motor");
plt.show()

#%%
"""Generate Plot 3"""


plot3 = plt.figure(figsize = (5, 5));
TWRvsMotorvsEFT = plt.axes(projection = "3d");
TWRvsMotorvsEFT.scatter(TWRs, x_values, estFlightTimes, color = "green");
plt.yticks(x_values, motorNames, rotation = "horizontal");
TWRvsMotorvsEFT.set_xlabel("Thrust to Weight Ratio");
TWRvsMotorvsEFT.set_ylabel("SunnySky Motor Types");
TWRvsMotorvsEFT.set_zlabel("Estimated Flight Time");
TWRvsMotorvsEFT.set_title("TWR vs Motor vs Estimated Flight Time")
plt.show()



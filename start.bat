@echo off
TITLE IronMen Robot
:: Enables virtual env mode and then starts IronMen
env\scripts\activate.bat && py -m IronMenRobot

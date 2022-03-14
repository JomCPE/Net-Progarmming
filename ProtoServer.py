# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:28:22 2022

@author: ASUS
"""
from tkinter import *
from turtle import st
import socket
#==============Server======================
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 15555
serversocket.bind((host, port))
serversocket.listen(5)

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:52:55 2022

@author: ASUS
"""
#===============import==================================
from tkinter import *
from turtle import st
import socket
#===============Funtion=================================
won = False
n = ""
play = False
mplay = False
hplay = False
#======================================================
def check():
    count = 0
    global msg
    global won
    global n
    if (msg[0] == msg[1]) and (msg[1] == msg[2]):         
        if (msg[0] == 'x'):
            n = "X WIN"         
        if (msg[0] == 'o'):
            n = "O WIN"
        won = True                    
    if (msg[3] == msg[4]) and (msg[4] == msg[5]):        
        if (msg[3] == 'x'):
            n = "X WIN"  
        if (msg[3] == 'o'):
            n = "O WIN"
        won = True           
    if (msg[6] == msg[7]) and (msg[7] == msg[8]):
        if (msg[6] == 'x'):
            n = "X WIN"              
        if (msg[6] == 'o'):
            n = "O WIN"
        won = True                        
    if (msg[0] == msg[3]) and (msg[3] == msg[6]):        
        if (msg[0] == 'x'):
            n = "X WIN"
            
        if (msg[0] == 'o'):
            n = "O WIN"
        won = True                    
    if (msg[1] == msg[4]) and (msg[4] == msg[7]):
        if (msg[1] == 'x'):
            n = "X WIN"              
        if (msg[1] == 'o'):
            n = "O WIN"
        won = True       
    if (msg[2] == msg[5]) and (msg[5] == msg[8]):        
        if (msg[2] == 'x'):
            n = "X WIN"  
            
        if (msg[2] == 'o'):
            n = "O WIN"
        won = True                    
    if (msg[0] == msg[4]) and (msg[4] == msg[8]):
        if (msg[0] == 'x'):
            n = "X WIN"              
        if (msg[0] == 'o'):
            n = "O WIN"
        won = True                    
    if (msg[2] == msg[4]) and (msg[4] == msg[6]):
        if (msg[2] == 'x'):
            n = "X WIN"              
        if (msg[2] == 'o'):
            n = "O WIN"
        won = True  
    else:
        for i in msg:
            if(i == "x" or i == "o"):
                count+=1
        if(count == 9):
            won = True
            n = "DRAW"

def showWin():
    global n
    top = Toplevel(root)
    top.geometry("150x50")
    top.title("Tic-Tac-Toe")
    Label(top, text= n, font=('TH Sarabun New', 18, 'bold'),justify = CENTER).place(x=int(75/2),y=0)

def XO(b,num):
    global n
    global msg
    global status
    global won
    global play
    if(play):
        if(not won):
            if status==True:
                if(msg[num] == 'o' or msg[num] == 'x'):
                    status = True
                else:
                    b.set("x")
                    msg[num]="x"
                    status=False
                    check()
            else:
                if(msg[num] == 'o' or msg[num] == 'x'):
                    status = False
                else:          
                    b.set("o")
                    msg[num]="o"
                    status=True
                    check()
        if(won):
            print(n)
            showWin()

#===============variable================================
root = Tk()
root.geometry("750x300")
root.title("Tic-Tac-Toe")

player_var = StringVar()
player = ""

status = True

msg = ['1','2','3','4','5','6','7','8','9']
btn1_text=StringVar()
btn1_text.set(msg[0])

btn2_text=StringVar()
btn2_text.set(msg[1])

btn3_text=StringVar()
btn3_text.set(msg[2])

btn4_text=StringVar()
btn4_text.set(msg[3])

btn5_text=StringVar()
btn5_text.set(msg[4])

btn6_text=StringVar()
btn6_text.set(msg[5])

btn7_text=StringVar()
btn7_text.set(msg[6])

btn8_text=StringVar()
btn8_text.set(msg[7])

btn9_text=StringVar()
btn9_text.set(msg[8])

btnh_text=StringVar()
btnh_text.set("Play With Host")

btnm_text=StringVar()
btnm_text.set("Multiplayer")

sbtn_text=StringVar()
sbtn_text.set("Submit")

Label_text=StringVar()

def Multiplay():
    global play
    if(play):
        pass
    else:
        play = True
def plywhost():
    global play
    if(play):
        pass
    else:
        play = True
def Submit():
    global player
    global player_var
    player = player_var.get()
    print(player)

#===============Table===================================
btn1 = Button(root,padx=16,pady=16,bd=8,fg="black",
              font=("TH Sarabun New",20,'bold'),
              textvariable=btn1_text,bg="powder blue",command=lambda:XO(btn1_text,0)).grid(row=0,column=0)
btn2 = Button(root,padx=16,pady=16,bd=8,fg="black",
              font=("TH Sarabun New",20,'bold'),
              textvariable=btn2_text,bg="powder blue",command=lambda:XO(btn2_text,1)).grid(row=0,column=1)
btn3 = Button(root,padx=16,pady=16,bd=8,fg="black",
              font=("TH Sarabun New",20,'bold'),
              textvariable=btn3_text,bg="powder blue",command=lambda:XO(btn3_text,2)).grid(row=0,column=2)
btn4 = Button(root,padx=16,pady=16,bd=8,fg="black",
              font=("TH Sarabun New",20,'bold'),
              textvariable=btn4_text,bg="powder blue",command=lambda:XO(btn4_text,3)).grid(row=1,column=0)
btn5 = Button(root,padx=16,pady=16,bd=8,fg="black",
              font=("TH Sarabun New",20,'bold'),
              textvariable=btn5_text,bg="powder blue",command=lambda:XO(btn5_text,4)).grid(row=1,column=1)
btn6 = Button(root,padx=16,pady=16,bd=8,fg="black",
              font=("TH Sarabun New",20,'bold'),
              textvariable=btn6_text,bg="powder blue",command=lambda:XO(btn6_text,5)).grid(row=1,column=2)
btn7 = Button(root,padx=16,pady=16,bd=8,fg="black",
              font=("TH Sarabun New",20,'bold'),
              textvariable=btn7_text,bg="powder blue",command=lambda:XO(btn7_text,6)).grid(row=2,column=0)
btn8 = Button(root,padx=16,pady=16,bd=8,fg="black",
              font=("TH Sarabun New",20,'bold'),
              textvariable=btn8_text,bg="powder blue",command=lambda:XO(btn8_text,7)).grid(row=2,column=1)
btn9 = Button(root,padx=16,pady=16,bd=8,fg="black",
              font=("TH Sarabun New",20,'bold'),
              textvariable=btn9_text,bg="powder blue",command=lambda:XO(btn9_text,8)).grid(row=2,column=2)

LabelText1= Label(root,font=('TH Sarabun New',18,'bold',),text = "Name",
              bd=16, anchor='w').grid(row=0,column=4)

Ref = Entry(root,font=('TH Sarabun New',18,'bold',),textvariable = player_var,
              bd=5,insertwidth=4,bg='powder blue',justify = 'center').grid(row=0,column=5)

sbtb = Button(root,padx=16,pady=13,bd=8,fg="black",
              font=("TH Sarabun New",15,'bold'),
              textvariable=sbtn_text,bg="powder blue",width = 3,command=lambda:Submit()).grid(row=0,column=6) 

btnh = Button(root,padx=16,pady=13,bd=8,fg="black",
              font=("TH Sarabun New",15,'bold'),
              textvariable=btnh_text,bg="powder blue",command=lambda:Multiplay()).grid(row=1,column=5)
btnm = Button(root,padx=16,pady=13,bd=8,fg="black",
              font=("TH Sarabun New",15,'bold'),
              textvariable=btnm_text,bg="powder blue",command=lambda:plywhost()).grid(row=2,column=5)

root.mainloop()
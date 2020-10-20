# Inductor and Capacitor impedance calculator + resonance frequency
# with GUI
# Riccardo Montaguti 20/10/2020
import tkinter as tk
from tkinter import *
from tkinter import ttk
import math


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()


# Title
label1 = tk.Label(root, text='Impedance Calculator')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)


# First input 
label2 = tk.Label(root, text='Frequency [Mhz]:')
label2.config(font=('helvetica', 10))
canvas1.create_window(50, 50, window=label2)

entry1 = tk.Entry(root,width=10) 
canvas1.create_window(150, 50, window=entry1)

# Second input
label3 = tk.Label(root, text='Capacitance [pF]:')
label3.config(font=('helvetica', 10))
canvas1.create_window(50, 75, window=label3)

entry2 = tk.Entry(root,width=10) 
canvas1.create_window(150, 75, window=entry2)

# Second input
label4 = tk.Label(root, text='Inductance [uH]:')
label4.config(font=('helvetica', 10))
canvas1.create_window(50, 100, window=label4)

entry3 = tk.Entry(root,width=10) 
canvas1.create_window(150, 100, window=entry3)


## menu a tendina Frequenza
OPTIONS =[ "Mhz", "Khz", "Hz", "Ghz"]

Fvariable = StringVar(root)
Fvariable.set(OPTIONS[0]) # default value

w = tk.OptionMenu(root, Fvariable, *OPTIONS)
canvas1.create_window(250, 50, window=w)

## menu a tendina Condensatore
OPTIONS =["pF", "nF", "uF","mF", "F"]

Cvariable = StringVar(root)
Cvariable.set(OPTIONS[0]) # default value

w = tk.OptionMenu(root, Cvariable, *OPTIONS)
canvas1.create_window(250, 75, window=w)


## menu a tendina induttore
OPTIONS =["nH", "uH", "mH","H"]

Lvariable = StringVar(root)
Lvariable.set(OPTIONS[1]) # default value

w = tk.OptionMenu(root, Lvariable, *OPTIONS)
canvas1.create_window(250, 100, window=w)




def CapImpedance ():

	if Fvariable.get()=="Mhz":
		ff = 1E6
	if Fvariable.get()=="Khz":
		ff = 1E3
	if Fvariable.get()=="Hz":
		ff = 1
	if Fvariable.get()=="Ghz":
		ff = 1E9

	if Cvariable.get()=="pF":
		cc = 1E-12
	if Cvariable.get()=="nF":
		cc = 1E-9
	if Cvariable.get()=="uF":
		cc = 1E-6
	if Cvariable.get()=="mF":
		cc = 1E-3
	if Cvariable.get()=="F":
		cc = 1
	
	f = float(entry1.get()) # get frequency
	c = float(entry2.get()) # get capacitance#Mhz = 1E6 
	
	xc = 1 / (2*math.pi*f*ff*c*cc )
	xc = round(xc,2)

	#clear previous value
	label55 = tk.Label(root, text="                      ",font=('helvetica', 10, 'bold'))
	canvas1.create_window(75, 150, window=label55)

	label5 = tk.Label(root, text= xc,font=('helvetica', 10, 'bold'))
	canvas1.create_window(75, 150, window=label5)
    
button1 = tk.Button(text='Capacitor Impedance [ohm]', command=CapImpedance, fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(75, 130, window=button1)





def IndImpedance ():

	if Fvariable.get()=="Mhz":
		ff = 1E6
	if Fvariable.get()=="Khz":
		ff = 1E3
	if Fvariable.get()=="Hz":
		ff = 1
	if Fvariable.get()=="Ghz":
		ff = 1E9	

	if Lvariable.get()=="nH":
		ll = 1E-9
	if Lvariable.get()=="uH":
		ll = 1E-6
	if Lvariable.get()=="mH":
		ll = 1E-3
	if Lvariable.get()=="H":
		ll = 1

	f = float(entry1.get()) # get frequency
	L = float(entry3.get()) # get capacitance

	xl = 2*math.pi*f*ff*L*ll
	xl = round(xl,2)

	#clear previous value
	label56 = tk.Label(root, text="                      ",font=('helvetica', 10, 'bold'))
	canvas1.create_window(220, 150, window=label56)

	label6 = tk.Label(root, text= xl,font=('helvetica', 10, 'bold'))
	canvas1.create_window(220, 150, window=label6)

button1 = tk.Button(text='Inductor Impedance [ohm]', command=IndImpedance, fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(220, 130, window=button1)




def Resonance ():

	if Cvariable.get()=="pF":
		cc = 1E-12
	if Cvariable.get()=="nF":
		cc = 1E-9
	if Cvariable.get()=="uF":
		cc = 1E-6
	if Cvariable.get()=="mF":
		cc = 1E-3
	if Cvariable.get()=="F":
		cc = 1	

	if Lvariable.get()=="nH":
		ll = 1E-9
	if Lvariable.get()=="uH":
		ll = 1E-6
	if Lvariable.get()=="mH":
		ll = 1E-3
	if Lvariable.get()=="H":
		ll = 1

	C = float(entry2.get()) # get inductance
	L = float(entry3.get()) # get capacitance

	res = 1/(2*math.pi* math.sqrt(C*cc*L*ll))
	

	if res >= 1000000:
		res = res/1000000
		res = round(res,5)
		res= str(res)+"Mhz"
	elif res < 1000000:
		res = round(res,2)
		res = str(res)+"Hz" 
	#clear previous value
	label57 = tk.Label(root, text="                      ",font=('helvetica', 10, 'bold'))
	canvas1.create_window(330, 150, window=label57)

	label7 = tk.Label(root, text= res,font=('helvetica', 10, 'bold'))
	canvas1.create_window(330, 150, window=label7)

button3 = tk.Button(text=' Resonance ', command=Resonance, fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(330, 130, window=button3)




root.mainloop()
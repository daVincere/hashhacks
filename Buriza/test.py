import Tkinter
import subprocess
import sys, os

top = Tkinter.Tk()

def PulseCallBack():
	print "Below is the output from the shell script in terminal::"
	output = subprocess.call('./test.bat', shell=True)
	os.system('call a.bat');

def MainCallBack():
	os.system('call b.bat');

Pulse = Tkinter.Button(top, text="Pulse", command= PulseCallBack)
Main = Tkinter.Button(top, text="Face Detection", command= MainCallBack)

Main.pack()
Pulse.pack()

top.mainloop()

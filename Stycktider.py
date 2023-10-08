"""
A simple program to calculate part times
By Stugo 2015-07-26
"""

from tkinter import *


class Stycktider(Tk):
	
	def __init__(self, master):
		"""Initalize the Frame"""
		frame = Frame(master)
		frame.pack()
		
		"""Create the layout"""
		self.label1 = Label(frame, text="Stycktid i minuter", padx=4, pady=4).grid(row=0,column=0)
		self.label2 = Label(frame, text="Antal bitar", padx=4, pady=2).grid(row=1,column=0)

		stycktidmin = Entry(frame, textvariable=stmin).grid(row=0, column=1)
		#stycktidmin.focus()
		self.antalbitar = Entry(frame, textvariable=bitantal).grid(row=1, column=1)

		self.button1 = Button(frame, text="Total körtid i h", command=self.claculatetime).grid(row=2, column=0)
		self.resultatruta = Entry(frame, textvariable=rruta).grid(row=2, column=1, pady=4)

	def claculatetime(self):
		"""Do the math"""
		bitant = float(bitantal.get())
		minst = float(stmin.get())
		totalmin = minst*bitant
		totalh = totalmin / 60
		rruta.set("%.2f" % totalh)
		return

	def enterPress(self, event):
		"""Runs the math if Enter is pressed"""
		self.claculatetime()
		return


root = Tk()
root.geometry("240x85+850+500")
root.title("Stycktider")

stmin = StringVar()
bitantal = StringVar()
bitantal.set("1")
rruta = StringVar()

app = Stycktider(root)

#app.bind("<KeyPress-Return>", enterPress)

root.mainloop()
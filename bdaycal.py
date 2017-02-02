#Given someone's birthday and today's date... Find their age in days!
import tkinter
import datetime

master = tkinter.Tk()
user = datetime.date(year, month, day)
today = datetime.date.today()

class date:

	def __init__(self, days, month, years):
		self.days = days
		self.month = month
		self.years = years
		Label(master, text="Birth Day").grid(row=0)
		Label(master, text="Birth Month").grid(row=1)
		Label(master, text="Birth Year").grid(row=2)

def calculate():
	global today
	global user
	return today - user

e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=2)

mainloop()
print(calculate())
import tkinter as tk 
import webbrowser

window = tk.Tk() 
window.geometry("500x500") #creates window 500 x 500 pixels


class Button:

	def __init__(self, name, positionx, postiony, padx, pady): # __init__ method intializes as soon as you create button from class..
		self.name = name
		butt = tk.Button(window, text=name, command= self.click) 
		butt.grid(column= positionx, row=postiony, padx= padx, pady= pady)
		

	def click(self):
		if self.name == "Blog":
			webbrowser.open_new_tab(URL + "/blog") 
		

URL = 'https://cleverprogrammer.com'
home = Button("Home", 0, 0, 0, 0,)
my_courses = Button("My Courses", 6, 0, 1, 0)
all_courses = Button("All Courses", 7, 0, 1, 0)
personal_coach = Button("Personal Coach", 8, 0, 1, 0)
blog = Button("Blog", 9, 0, 1, 0)
donate = Button("Donate", 10, 0, 1, 0)

oop = Button("Learn Python OOP", 2, 5, 20, 20)
lp = Button("Learn Python", 3, 5, 20, 20)
cpwt = Button("Codecademy Python Walkthrough and Tutorial Series", 4,5,20,20)

window.mainloop()

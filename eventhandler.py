import tkinter as tk 
import webbrowser
from PIL import Image, ImageTk

window = tk.Tk() 
window.title('Clever Programmer')
window.geometry("400x500") #creates window 500 x 500 pixels
image = Image.open('Logo.png')
image.thumbnail((400,300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image= tk.Label(image=photo)
label_image.grid(column=2, row=0)



class Button:

	def __init__(self, name, positionx, postiony, padx, pady): # __init__ method intializes as soon as you create button from class..
		self.name = name
		butt = tk.Button(window, text=name, command= self.click) 
		butt.grid(column= positionx, row=postiony, padx= padx, pady= pady)
		

	def click(self):
		if self.name == "Blog":
			webbrowser.open_new_tab(URL + "/blog") 
		if self.name == "My Courses":
			webbrowser.open_new_tab(URL + "/courses/enrolled")
		if self.name == "All Courses":
			webbrowser.open_new_tab(URL + "/courses")
		if self.name == "Personal Coach":
			webbrowser.open_new_tab(URL + "/p")
		if self.name == "Donate":
			webbrowser.open_new_tab("https://www.patreon.com/cleverprogrammer?sa=eyJ1c2VyX2lkIjoyNzE4MzQwLCJleHBpcmVzX2F0IjoxNDg2MDg0NzUxLCJzY2hvb2xfaWQiOjQ1MjQ4LCJhdXRoZW50aWNhdGlvbl90b2tlbiI6InN4bXdleTQ1ZUNGTHN5eC0yRjJ4ZFNYSGtOanhhd0tmMmcifQ%3D%3D--90aaa087ebabde35b8c39bf25f1ebf9fd4366b5f")
		if self.name == "Learn Python OOP":
			webbrowser.open_new_tab(URL + "/courses/enrolled/130834")
		if self.name == "Learn Python":
			webbrowser.open_new_tab(URL + "/courses/enrolled/105512)")
		if self.name == "Codecademy Python Walkthrough and Tutorial Series":
			webbrowser.open_new_tab(URL + "/p/python-walkthrough-and-tutorial-series-2016")
		else:
			webbrowser.open_new_tab(URL)






URL = 'https://cleverprogrammer.com'
home = Button("Home", 2, 1, 0, 1,)
my_courses = Button("My Courses", 2, 2, 0, 1)
all_courses = Button("All Courses", 2, 3, 0, 1)
personal_coach = Button("Personal Coach", 2, 4, 0, 1)
blog = Button("Blog", 2, 5, 0, 1)
donate = Button("Donate", 2, 6, 0, 1)

oop = Button("Learn Python OOP", 3, 3, 0, 1)
lp = Button("Learn Python", 3, 4, 0, 1)
cpwt = Button("Codecademy Python Walkthrough and Tutorial Series", 3,5,0,1)

window.mainloop()

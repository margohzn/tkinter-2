from tkinter import *

window = Tk()
window.title("Log in")
window.geometry("450x350")

#background color to window 
window.config(background = "pink")

#creating label for username                               #fg = the color of the text 
username = Label(window, text = "Username: ", bg = "pink", fg = "black").place(x = 40, y = 60)
password = Label(window, text = "Password: ", bg = "pink", fg = "blue").place(x = 40, y = 100)

#creating input boxes 
username_input = Entry(window, width = 30).place(x = 110, y = 60)
password_input = Entry(window, width = 30, show = "*").place(x = 110, y = 100)

button1 = Button(window, text = "submit").place(x = 40, y = 140)



window.mainloop()
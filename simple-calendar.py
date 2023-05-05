#import tkinter
from tkinter import *

#import calendar module
import calendar

#function for showing the given year
def showCal():
    #get the year entered in the year_field entry widget
    fetch_year = int(year_field.get())
    
    #create a new window to display the calendar
    new_gui = Toplevel(gui)
    new_gui.title("SIMPLE CALENDAR")
    new_gui.config(background="white")
    new_gui.geometry("800x800")
    
    #create a calendar widget and add it to the new window
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(new_gui, text=cal_content, font="consolas 12 bold")
    cal_year.grid(row=5, column=1, padx=20)

#create the main GUI window
gui = Tk()
gui.title("SIMPLE CALENDAR")
gui.config(background="white")
gui.geometry("350x200")

#create a label for the title
cal = Label(gui, text="SIMPLE CALENDAR", bg="white", font=("times roman", 24, 'bold'))
cal.grid(row=1, column=1)

#create a label and entry widget for entering the year
year_label = Label(gui, text="Enter Year", bg="light green")
year_label.grid(row=2, column=1)
year_field = Entry(gui)
year_field.grid(row=3, column=1)

#create a button for showing the calendar
show_button = Button(gui, text="Show Calendar", fg="black", bg="light blue", command=showCal)
show_button.grid(row=4, column=2)

#create an exit button for closing the window
exit_button = Button(gui, text="Exit", fg="black", bg="red", command=gui.quit)
exit_button.grid(row=5, column=1)

#start the GUI
gui.mainloop()

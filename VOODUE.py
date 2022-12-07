from tkinter import *
from PIL import Image,ImageTk
from tkcalendar import Calendar

window=Tk()
window.title("VOODUE")
window.configure(bg='#55556B',width=800, height=800)
# width of window

 
# Add Calendar
cal = Calendar(window, selectmode = 'day',
               year = 2022, month = 11,
               day = 14, )
 
cal.pack(pady = 80, padx=80)
 
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
 
# Add Button and Label
Button(window, text = "What would you like to schedule?",
       command = grad_date).pack(pady = 20)
 
date = Label(window, text = "")
date.pack(pady = 20)
 
# Execute Tkinter









window.mainloop()
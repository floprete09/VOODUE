import schedule
import time
from tkinter import *
from PIL import Image,ImageTk
from tkcalendar import Calendar
import time

root=Tk()
root.title("VooDue")
root.geometry("700x900")
root.configure(bg='#55556B')

label=Label(root, text="VOODUE", font=("Frente H1",50),bg="mistyrose4", fg="midnight blue" )
label.pack(padx=8, pady=8)



########EVENT PICKER

enter=Entry(
    root,
    width=50,
)
enter.pack()

def label1():
    mylabel=Label(root, text="")
    mylabel.pack()


def button3():
    thirdentry=Label(
        root,
        font=("century gothic", 20),
        borderwidth=5,
        text=enter.get()
        #function=(),
    )
    thirdentry.pack()


thirdbutton=Button(
    root, 
    command=button3, 
    text="What would you like to do?",
    font=("century gothic", 16),
    borderwidth=7,
    )
thirdbutton.pack(padx=6, pady=6)





######DATE PICKER

choose=Label(
    root,
    text="Choose a date from the calendar below",
    font=("century gothic bold",18),
    bg="slate gray",
   )
choose.pack(side=TOP)


hour_string=StringVar()
min_string=StringVar()
last_value_sec = ""
last_value = ""        
f = ('Times', 20)


fone = Frame(root)
ftwo = Frame(root)




fone.pack(pady=10)
ftwo.pack(pady=10)

msg = Label(
    root, 
    text="Hour | Minute | Seconds",
    font=("century gothic", 14),
    bg="slate gray"
    )
msg.pack(side=TOP)




sec_hour = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=min_string,
    font=f,
    width=2,
    justify=CENTER
)



def display_msg():
    date = cal.get_date()
    m = min_sb.get()
    h = sec_hour.get()
    s = sec.get()
    t = f"This event is scheduled for {date} at {m}:{h}:{s}."
    msg_display.config(text=t, font="verdana 20" )
       


if last_value == "59" and min_string.get() == "0":
    hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)   
    last_value = min_string.get()

if last_value_sec == "59" and sec_hour.get() == "0":
    min_string.set(int(min_string.get())+1 if min_string.get() !="59" else 0)
if last_value == "59":
    hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)            
    last_value_sec = sec_hour.get()

pktime=Label(
root, 
text="Choose your time",
bg="slate gray",
font=("A Pompadour Bold",18),
)
pktime.pack()


min_sb = Spinbox(
    ftwo,
    from_=0,
    to=23,
    wrap=True,
    textvariable=hour_string,
    width=2,
    state="readonly",
    font=f,
    justify=CENTER
)


sec = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=sec_hour,
    width=2,
    font=f,
    justify=CENTER
)

min_sb.pack(side=LEFT, fill=X, expand=True)
sec_hour.pack(side=LEFT, fill=X, expand=True)
sec.pack(side=LEFT, fill=X, expand=True)



actionBtn =Button(
    root,
    text="Enter the date and time", 
    font=("century gothic", 16),
    borderwidth=7,
    padx=10,
    pady=10,
    command=display_msg
)
actionBtn.pack(pady=10)

msg_display = Label(
    root,
    text="",
    bg="white"
)
msg_display.pack(pady=10)


#########CALENDAR


cal = Calendar(
    fone, 
    selectmode="day", 
    year=2022, 
    month=12,
    day=3
    )
cal.pack()



#cal = Calendar(root, selectmode = 'day',
 #              year = 2022, month = 11,
  #             day = 14, )
#cal.pack(pady = 80, padx=80)


#def grad_date():
 #   date.config(text = "Selected Date is: " + cal.get_date())

#Button(root,text = "Choose a date",command =lambda:[grad_date(),button3() ]).pack(pady = 20)
 
#date = Label(root, text = "")
#date.pack(pady = 20)

#######time

hour_string=StringVar()
min_string=StringVar()
last_value_sec = ""
last_value = ""        
f = ('Times', 20)




#def button1():
    #firstetntry=Entry()
    #firstetntry.pack(pady=6, padx=4)

#def button2():
    #secondentry=Entry()
    #secondentry.pack(padx=7, pady=3)




#secondbutton=Button(root, command=button2,text="Choose a Time.")
#secondbutton.pack (padx=1, pady=3)




#firstbutton=Button(root, command=button1, )
#firstbutton.pack(padx=3,pady=4)



#Time
#schedule.every(5).seconds.do(button1)
#schedule.every(10).seconds.do(button2)
#schedule.every(1).day.at("18:56").do(button3)
#while True:
 #   schedule.run_pending()
  #  time.sleep(1)
  # 
root.mainloop()
from tkinter import *
import time,pyttsx3
import datetime
import time


Name = "Chaitanya"

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            count=0
            while count<=10:
                count=count+1
                engine=pyttsx3.init()
                engine.say("hey"+Name + "wake up")
                engine.runAndWait()
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
#GUI 
clock = Tk()
clock.title("Chaitanya Alarm Clock")
clock.configure(background='#070536')
clock.geometry("400x200")
time_format=Label(clock, text= "hey user! please enter in 24hrs format", fg="black",bg="white",font=("Times Roman",10)).place(x=70,y=160)
addTime = Label(clock,text ="  Hour  ",bg="#54bce9",fg = "white",relief="solid",font=20).place(x = 70,y= 40)
addTime = Label(clock,text ="  min  ",bg="#54bce9",fg = "white",relief="solid",font=20).place(x = 165,y= 40)
addTime = Label(clock,text ="  sec  ",bg="#54bce9",fg = "white",relief="solid",font=20).place(x = 250,y= 40)
setYourAlarm = Label(clock,text = "Wakeup Buddy",fg="black",relief = "solid",font=("Helevetica",12,"bold")).place(x=130, y=0)

hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "#ceebfd",relief="solid",width = 15).place(x=65,y=80)

minTime= Entry(clock,textvariable = min,bg = "#ceebfd",relief="solid",width = 15).place(x=145,y=80)

secTime = Entry(clock,textvariable = sec,bg = "#ceebfd",relief="solid",width = 15).place(x=230,y=80)

#input by user:
submit = Button(clock,text = "Generate alarm",fg="white",width = 20,bg="black",command = actual_time).place(x =120,y=110)

clock.mainloop()
#Execution of the window.



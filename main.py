from fastapi import FastAPI
from fastapi.responses import JSONResponse
from tkinter import StringVar, Tk
from tkinter import ttk
from tkinter import font
import time
import datetime
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

app = FastAPI()
# user, db, password, host, port = get_credentials()
# con = psycopg2.connect(database=db, user=user,
#                        password=password, host=host, port=port)
# cur = con.cursor()


def show_time():
    print(var)
    # Get the time remaining until the event
    remainder = endTime - datetime.datetime.now()
    # remove the microseconds part
    remainder = remainder - datetime.timedelta(microseconds=remainder.microseconds)
    # Show the time left
    txt.set(remainder)
    # Trigger the countdown after 1000ms
    root.after(1000, show_time)


    # Set the end date and time for the countdown
endTime = datetime.datetime(2021, 9, 19, 9, 0, 0)

var = 1

# Use tkinter lib for showing the clock
root = Tk()
# root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("x", quit)
root.after(1000, show_time)

fnt = font.Font(family='Helvetica', size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="green", background="black")
lbl.place(relx=0.5, rely=0.5, anchor="center")

@app.get("/")
def read_root():
    return 'server is running'


@app.get("/start")
async def startclock():
    def show_time():
        print(var)
        # Get the time remaining until the event
        remainder = endTime - datetime.datetime.now()
        # remove the microseconds part
        remainder = remainder - datetime.timedelta(microseconds=remainder.microseconds)
        # Show the time left
        txt.set(remainder)
        # Trigger the countdown after 1000ms
        root.after(1000, show_time)


    # Set the end date and time for the countdown
    endTime = datetime.datetime(2021, 9, 19, 9, 0, 0)

    var = 1

    # Use tkinter lib for showing the clock
    root = Tk()
    # root.attributes("-fullscreen", True)
    root.configure(background='black')
    root.bind("x", quit)
    root.after(1000, show_time)



    fnt = font.Font(family='Helvetica', size=60, weight='bold')
    txt = StringVar()
    lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="green", background="black")
    lbl.place(relx=0.5, rely=0.5, anchor="center")

    # root.mainloop()

    return 1 

@app.get("/s")
async def startclock():
    

    root.mainloop()

    return 1 

@app.get("/stop")
async def startclock():
    

    root.destroy()

    return 1 

#import relevant libraries
from tkinter import * 
import sqlite3 as sq 
import datetime



window = Tk()
window.title("Compound Tracker") 
#and the size of the window is set.
window.geometry("800x600+0+0")
window.configure(background="SpringGreen2")
#We can input text to form a header for the GUI. This is done via the ‘header’ variable.
header = Label(window, text="Running Tracker", font=("arial",30,"bold"),bg="SpringGreen2", fg="black")
header.pack()
#connect to the DB
con = sq.connect("running.db")
c = con.cursor()

#mess around with menu widget
def quit_app():
    window.destroy()
def blue_window():
    window.config(background="Blue")
    #L1 = Label(window, text = 'Run Type', font=('arial', 18),bg="Blue").place(x=10,y=100)
    L1.config(bg="Blue") #this has to be placed seperately as its ref is none
    L2.config(bg="Blue")
    L3.config(bg="Blue")
    L4.config(bg="Blue")
    L5.config(bg="Blue")
    L6.config(bg="Blue")
    header.config(bg="Blue")
def red_window():
    window.config(background="Red")
def grey_window():
    window.config(background="Grey")
def green_window():
    window.config(background="SpringGreen2")


    
mainmenu = Menu(window)
mainmenu.add_command(label="Quit",command=quit_app)
dropmenu = Menu(mainmenu)
dropmenu.add_command(label="Blue",command=blue_window)
dropmenu.add_command(label="Red",command=red_window)
dropmenu.add_command(label="Grey",command=grey_window)
dropmenu.add_command(label="Green",command=green_window)
mainmenu.add_cascade(label="Colour", menu=dropmenu)

#variables which are assigned as Label object
L1 = Label(window, text = 'Run Type', font=('arial', 18),bg="SpringGreen2")
L1.place(x=10,y=100)
L2 = Label(window, text = 'Day (dd)', font=('arial',18),bg="SpringGreen2")
L2.place(x=10,y=150)
L3 = Label(window, text = 'Month (mm)', font=('arial',18),bg="SpringGreen2")
L3.place(x=10,y=200)
L4 = Label(window, text = 'Year (yyyy)', font=('arial',18),bg="SpringGreen2")
L4.place(x=10,y=250)
L5 = Label(window, text = 'Time (mins)', font=('arial',18),bg="SpringGreen2")
L5.place(x=10,y=300)
L6 = Label(window, text = 'Miles', font=('arial',18),bg="SpringGreen2")
L6.place(x=10,y=350)

runtype = StringVar(window)
runtype.set("Choose")



window.config(menu=mainmenu)
#menu widget finishes


#create a list(dictionary) for runs
runtypelist = {'Recovery', 'Speed', 'Interval', 'HillTrain'}
#set up optionmenu
runtypemenu = OptionMenu(window, runtype, *runtypelist)
runtypemenu.config(width=15)
runtypemenu.place(x=220, y=105)

#dropdowndbase = OptionMenu(window, rundb, *runtypelist)#For 2nd drop down list
#dropdowndbase.place(x=100,y=500)
#set up your entry boxes you need to define as stringvar
day = StringVar()#these bind the variables that you get from the entry boxes
dayT = Entry(window, textvariable=day)
dayT.place(x=220, y=155)
month = StringVar()
monthT = Entry(window, textvariable=month)
monthT.place(x=220,y=205)
year = StringVar()
yearT = Entry(window, textvariable=year)
yearT.place(x=220,y=255)
timetaken = StringVar()
timeT = Entry(window, textvariable=timetaken)
timeT.place(x=220,y=305)
miles = StringVar()
milesT = Entry(window, textvariable=miles)
milesT.place(x=220,y=355)

def clear():
    runtype.set('Choose')
    day.set('')
    month.set('')
    year.set('')
    timetaken.set('')
    miles.set('')

def sendrecord():
  print("You have submitted a record")
  c.execute('CREATE TABLE IF NOT EXISTS ' +runtype.get()+ ' (Datestamp TEXT, timetaken INTEGER, miles INTEGER)') #SQL syntax

  date = datetime.date(int(year.get()),int(month.get()), int(day.get())) #Date in format from 'import datetime'

  c.execute('INSERT INTO ' +runtype.get()+ ' (Datestamp, timetaken, miles) VALUES (?, ?, ?)',
                  (date, timetaken.get(), miles.get())) #Insert record into database.
  con.commit()

def record():
    c.execute('SELECT * FROM ' +rundb.get()) #Select from which ever compound lift is selected

    frame = Frame(newwindow)
    frame.place(x= 400, y = 150)
   
    Lb = Listbox(frame, height = 8, width = 25,font=("arial", 12))
    Lb.pack(side = LEFT, fill = Y)
   
    scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set)
   

    Lb.insert(0, 'Date, Time Taken, Miles') #first row in listbox
   
    data = c.fetchall() # Gets the data from the table
    
    
    for row in data:
        Lb.insert(1,row) # Inserts record row by row in list box

    L7 = Label(newwindow, text = rundb.get()+ '      ',
              font=("arial", 16)).place(x=400,y=100) # Title of list box, given which compound lift is chosen

    L8 = Label(newwindow, text = "They are ordered from most recent",
              font=("arial", 16)).place(x=400,y=350)
    con.commit()

def newwindow():
    def record():
        c.execute('SELECT * FROM ' +rundb.get()) #Select from which ever compound lift is selected

        frame = Frame(newWin)
        frame.place(x= 400, y = 150)
       
        Lb = Listbox(frame, height = 8, width = 25,font=("arial", 12))
        Lb.pack(side = LEFT, fill = Y)
       
        scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
        scroll.config(command = Lb.yview)
        scroll.pack(side = RIGHT, fill = Y)
        Lb.config(yscrollcommand = scroll.set)
       

        Lb.insert(0, 'Date, Time Taken, Miles') #first row in listbox
       
        data = c.fetchall() # Gets the data from the table
        
        
        for row in data:
            Lb.insert(1,row) # Inserts record row by row in list box

        L7 = Label(newWin, text = rundb.get()+ '      ',
                  font=("arial", 16)).place(x=400,y=100) # Title of list box, given which compound lift is chosen

        L8 = Label(newWin, text = "They are ordered from most recent",
                  font=("arial", 16)).place(x=400,y=350)
        con.commit()
    newWin = Toplevel(window)
    newWin.geometry("1000x800+0+0")
    header = Label(newWin, text="another window",font=("ariel",30,"bold")).pack()
    rundb = StringVar(newWin)
    rundb.set("Choose")
    dropdowndbase = OptionMenu(newWin, rundb, *runtypelist)#For 2nd drop down list
    dropdowndbase.place(x=100,y=500)
    button_4 = Button(newWin, text="Get Runs", command=record)
    button_4.place(x=160, y=600)
    button5 = Button(newWin, text="Dismiss", command=newWin.destroy)
    button5.place(x=200,y=600)
    numone=intVar()
    numEntry = Entry(newWin, textvariable=numone)
      
  

button_1 = Button(window, text="Clear",command=clear)
button_1.place(x=10,y=400)

button_2 = Button(window, text="Submit",command=sendrecord)
button_2.place(x=80,y=400)

button_3 = Button(window, text="another window", command=newwindow)
button_3.place(x=200, y=400)






#To keep the root window open, a loop needs to be set to the root window.
window.mainloop()

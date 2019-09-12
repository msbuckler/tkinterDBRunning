from tkinter import * #GUI package
import sqlite3 as sq #For tables and database
import datetime

window = Tk()
window.title("Run Tracker") 
window.geometry('1000x800+0+0')
header = Label(window, text="Running Tracker", font=("impact",30,"bold"), fg="steelblue").pack()

con = sq.connect('Run.db') #dB browser for sqlite needed
c = con.cursor() #SQLite command, to connect to db so 'execute' method can be called


L1 = Label(window, text = "Run Type", font=("impact", 18)).place(x=10,y=100)
L2 = Label(window, text = "Day (dd)", font=("impact",18)).place(x=10,y=150)
L3 = Label(window, text = "Month (mm)", font=("impact",18)).place(x=10,y=200)
L4 = Label(window, text = "Year (yyyy)", font=("impact",18)).place(x=10,y=250)
L5 = Label(window, text = "Time Taken(mins)", font=("impact",18)).place(x=10,y=300)
L6 = Label(window, text = "Miles", font=("impact",18)).place(x=10,y=350)

#Create variables for each list
runtype = StringVar(window)#For 1st drop time
runtype.set('Choose') #Inital placeholder for field



day = StringVar(window)
month = StringVar(window)
year = StringVar(window)
timetaken = StringVar(window)
miles = StringVar(window)

#Dictionary for drop down list
runtypelist = {'HillTrain', 'Speed', 'Recovery','Interval'}

dropdownrun = OptionMenu(window, runtype, *runtypelist) #For 1st drop down list 
dropdownrun.place(x=220,y=105)




#Entry for 'input' in GUI
dayT = Entry(window, textvariable=day)
dayT.place(x=220,y=155)

monthT = Entry(window, textvariable=month)
monthT.place(x=220,y=205)

yearT = Entry(window, textvariable=year)
yearT.place(x=220,y=255)

timeT = Entry(window, textvariable=timetaken)
timeT.place(x=220,y=305)

milesT = Entry(window, textvariable=miles)
milesT.place(x=220,y=355)

#get func to isolate the text entered in the entry boxes and submit to database
def sendrecord():
        print("You have submitted a record")
        
        c.execute('CREATE TABLE IF NOT EXISTS ' +runtype.get()+ ' (Datestamp TEXT, timetaken INTEGER, miles INTEGER)') #SQL syntax
        
        date = datetime.date(int(year.get()),int(month.get()), int(day.get())) #Date in format from 'import datetime'

        c.execute('INSERT INTO ' +runtype.get()+ ' (Datestamp, timetaken, miles) VALUES (?, ?, ?)',
                  (date, timetaken.get(), miles.get())) #Insert record into database.
        con.commit()

#Reset fields after submit
        runtype.set('----')
        day.set('')
        month.set('')
        year.set('')
        timetaken.set('')
        miles.set('')

#Clear boxes when submit button is hit
def clear():
    runtype.set('----')
    rundb.set('----')
    day.set('')
    month.set('')
    year.set('')
    timetaken.set('')
    miles.set('')
    

button_1 = Button(window, text="Submit",command=sendrecord)
button_1.configure(font=('Impact', 18))
button_1.place(x=100,y=400)

button_2 = Button(window,text= "Clear",command=clear)
button_2.place(x=10,y=400)




window.mainloop() #mainloop() -> make sure that window stays open

import tkinter

top = tkinter.Tk()
top.title("Event Planner")
top.resizable(width=False,height=False)
top.geometry('{}x{}'.format(225,125))
top.configure(bg="#005266")

#Asks for the event name
eventNameL = tkinter.Label(top, text="Event name:", fg="#33ff33", bg="#005266")
eventNameL.grid(row=1,column=0)

eventNameEText = tkinter.StringVar()
eventNameE = tkinter.Entry(top, textvariable=eventNameEText, fg="#ffffff", bg="#00a3cc")
eventNameE.grid(row=1,column=2)

#Asks for the persons name
personNameL = tkinter.Label(top, text="Person's name:", fg="#33ff33", bg="#005266")
personNameL.grid(row=2,column=0)

personNameEText = tkinter.StringVar()
personNameE = tkinter.Entry(top, textvariable=personNameEText, fg="#ffffff", bg="#00a3cc")
personNameE.grid(row=2,column=2)

#Asks for the days available format
eventDateL = tkinter.Label(top, text="Days available:", fg="#33ff33", bg="#005266")
eventDateL.grid(row=3,column=0)

eventDateEText = tkinter.StringVar()
eventDateE = tkinter.Entry(top, textvariable=eventDateEText, fg="#ffffff", bg="#00a3cc")
eventDateE.grid(row=3,column=2)

#Asks for the times available
eventTimeL = tkinter.Label(top, text="Time available:", fg="#33ff33", bg="#005266")
eventTimeL.grid(row=4,column=0)

eventTimeEText = tkinter.StringVar()
eventTimeE = tkinter.Entry(top, textvariable=eventTimeEText, fg="#ffffff", bg="#00a3cc")
eventTimeE.grid(row=4,column=2)

#Submits the data and puts it into a text file, then clears the entry boxes
def SaveData():
	file = open(".\\" + str(eventNameEText.get()) + ".txt","a+")
	file.write(str("Persons name: " + personNameEText.get()) + "\n" + "Day availability: " + str(eventDateEText.get()) + "\n" + "Time availability: " + str(eventTimeEText.get()) + "\n\n")
	file.close()
	personNameE.delete(0,'end')
	eventDateE.delete(0,'end')
	eventTimeE.delete(0,'end')

submitData = tkinter.Button(top, text="Submit", command=SaveData, width=30, bg="#66c2ff")
submitData.grid(row=5,columnspan=3,pady=10)
	
top.mainloop()
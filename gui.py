from tkinter import *
import os
from os import path
from datetime import datetime;

root=Tk()
root.configure(background="white")

def onClickCreateDataSet():    
    os.system("python3 dataSetCreater.py")
    print("Data Set created")
    
def onClickTrainDataSet():
    os.system("python3 trainer.py")
    print("Trained classifier")

def onClickRecognize1():
    os.system("python3 tester1.py")

def onClickRecognize2():
    os.system("python3 tester2.py")

def onclickAttendanceSheet():
   attendanceRecordXlsFileName = "Attendance.xls"
   if(path.exists(attendanceRecordXlsFileName) and path.isfile(attendanceRecordXlsFileName)):
    os.system("libreoffice --calc Attendance.xls") #or os.system("localc Attendance.xls")
   else:
    print("Attendance.xls file does't exists") 

def onClickExit():
    root.destroy()

# Main()

#title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=onClickCreateDataSet).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=onClickTrainDataSet).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Attendance(DESKTOP)",font=('times new roman',20),bg="#0D47A1",fg="white",command=onClickRecognize1).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating fourth button
Button(root,text="Attendance(RASPI)",font=('times new roman',20),bg="#0D47A1",fg="white",command=onClickRecognize2).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#0D47A1",fg="white",command=onclickAttendanceSheet).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating exit button
Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=onClickExit).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()

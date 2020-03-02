import xlwt
import xlrd
import datetime as dt
from xlutils.copy import copy
import os
from os import path
from calendar import monthrange

def initRollnoName(sheet):
    names = ("Aastha Gupta", "Abhay Rajput", "Aima Juveria", "Alamdar Abbas", "Aman Kumar", "Arjun Singh", "Ashar Ahmad Khan", "Ashutosh Dwivedi", "Ashutosh Kumar Dwivedi", "Dipanshu Negu", "Himanshu Adhikari", "Ifra Sabi", "Isha Khaleel", "Ishraq Ansari", "Israil Ahmad","Kavya Chandra", "Kunal Raghav", "Mariam Jamal", "Mariam Khan", "Md Asadullah", "Mohammed Najir Nagori", "Mohd Atif Siddiqui", "Mohd Muzakkir", "Mohd Sahil Warsi", "Mohd Sharique Alam", "Mohd Shoaib", "Mohd Tauhid", "Mohd Zahid Aslam", "Mohd Zargham Ahmed", "Moin Khan", "Naman Jain", "Nausheen Fatima", "Nawal saeed", "Nazreen", "Nikhil Kalani", "Pushpendra Kumar", "Rishi Kumar", "S Shabahat Hussain", "Saba Sarwar", "Sandeep", "Shaba Ahmad", "Shah Fahad", "Shaquib Ali Khan", "Shivam Gupta", "Shubam Jangra", "Shubhangi Singh", "Sumit Nagpal", "Syed Hamid Ashraf", "Tairah Andrabi", "Tarun Sharma", "Vaishali Gupta", "Vinay Ranjan", "Wasif Jamal", "Wasit Shafi", "Yogesh Kargeti", "Ives", "Zain Ullah Khan")
    x = 1 #used to point cell (x - cordinate of cell)
    for i in range(0,len(names)):
            prefix = "MCA0"                 # + 1 because rollno starts from 1
            rollno =  prefix + str('%02d' % (i + 1)) # '%02d' it is used to make a single digit 1-9 as two digit like 01-09
            name = names[i]
            sheet.write(x, 0, rollno)
            sheet.write(x, 1, name)
            x = x + 1
            print("Roll no : ", rollno, "Name : ", name)
    return sheet

def initAttendanceRecordXlsFile():
    currentDateTime = dt.datetime.now()

    year = int(currentDateTime.strftime("%Y"))
    month = int(currentDateTime.strftime("%m"))
    _, noOfDaysInCurrentMonth = monthrange(year, month)                            
    
    monthName = currentDateTime.strftime("%B")
    sheetName = monthName + str(year)   
    print("Sheeet name is : ", sheetName)
    
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet(sheetName) 

    sheet1.write(0,0,"Roll no")
    sheet1.write(0,1,"Name")
    y = 2
    
    for i in range(1,noOfDaysInCurrentMonth + 1):
        sheet1.write(0, y, i)
        y = y + 1
    sheet1 = initRollnoName(sheet1)
    wb.save("Attendance.xls")
    return wb

def getCellValue(wb, sheetNo, x, y):
    sheet = wb.sheets()[sheetNo]
    cellText = sheet.cell(x, y)
    return cellText.value

def markAttendence(userid):   
    currentDateTime = dt.datetime.now()
    DATE = int(currentDateTime.strftime("%d")) 
    x = userid
    y = int(DATE) + 1 #the DATE + 1 will be used to select the column # +1 instead of +2(Rollno, Name) because the cell starts from index value starts from 0
    rb = xlrd.open_workbook("Attendance.xls")  # i think rb refers 'return book'
    wb = copy(rb)                              # wb refers 'workbook'
    sheet = wb.get_sheet(0) # or sheet = wb.sheet_by_name('June2019')
    sheet.write(x, y,"P")    
    y = DATE + 1 
    global maxRollno
    for i in range(1, maxRollno+1): #maxRollNo+1 because range don't iterate for the last value eg: range(1,5) === 1,2,3,4
       if(getCellValue(rb, 0, i, y) == ""): # CTM: we have to pass 'rb' as args rather than wb, for reading purpose
          sheet.write(i, y,"A") # column no is constant
    wb.save("Attendance.xls")

# Main
attendanceRecordXlsFileName = "Attendance.xls" # global variables
maxRollno = 57 # Max Rollno of our class

if(path.exists(attendanceRecordXlsFileName) and path.isfile(attendanceRecordXlsFileName)):
    print("Yes file exists...")
    print ("Now ypu need to insert only faces and record in the excel file")
else:
    print("No file does not exists...")
    wb = initAttendanceRecordXlsFile()

#markAttendence(54)
#markAttendence(5)

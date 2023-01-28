from tkinter import *
from tkinter import ttk

import convertData as cd
import workingWithData as wwd
import os

varList = []
checkbuttonList = []
labelList = []

# считать БД в словарь
myDict = cd.importCSV()

def myChange():
    print()

def myExport():
    cd.exportToCSV(myDict)

def myAdd():
    mySize = len(myDict)
    for i in range(mySize):
        checkbuttonList[i].destroy()
        for j in range(5):
            labelList[i][j].destroy()

    wwd.newPersonal(myDict,[enName.get(), enSurname.get(), enPatronomic.get(), enPosition.get(), enSalary.get()])
    myCount = len(myDict)
    key = list(myDict)[-1]

    if len(varList) < myCount:
        varList.append(IntVar())
        myCheckbutton = Checkbutton(text = str(key), variable = varList[myCount - 1])
        myCheckbutton.grid(row = myCount, column = 0)
        checkbuttonList.append(myCheckbutton)
        surname = Label(myWindow, text = myDict[key][1])
        name = Label(myWindow, text = myDict[key][0])
        patronomic = Label(myWindow, text = myDict[key][2])
        position = Label(myWindow, text = myDict[key][3])
        salary = Label(myWindow, text = myDict[key][4])
        labelList.append([surname, name, patronomic, position, salary])

    myCount = 0
    for key in myDict:
        varList[myCount] = IntVar()
        myCheckbutton = Checkbutton(text = str(key), variable = varList[myCount])
        myCheckbutton.grid(row = myCount + 3, column = 0)
        checkbuttonList[myCount] = myCheckbutton
        surname = Label(myWindow, text = myDict[key][1])
        surname.grid(row = myCount + 3, column = 1)
        name = Label(myWindow, text = myDict[key][0])
        name.grid(row = myCount + 3, column = 2)
        patronomic = Label(myWindow, text = myDict[key][2])
        patronomic.grid(row = myCount + 3, column = 3)
        position = Label(myWindow, text = myDict[key][3])
        position.grid(row = myCount + 3, column = 4)
        salary = Label(myWindow, text = myDict[key][4])
        salary.grid(row = myCount + 3, column = 5)
        labelList[myCount] = [surname, name, patronomic, position, salary]
        myCount += 1

def myDelete():
    mySize = len(myDict)
    for i in range(mySize):
        if varList[i].get() != 0:
            wwd.deletionOnID(myDict, int(checkbuttonList[i]["text"]))
    for i in range(mySize):
        checkbuttonList[i].destroy()
        for j in range(5):
            labelList[i][j].destroy()
    myCount = 0
    for key in myDict:
        varList[myCount] = IntVar()
        myCheckbutton = Checkbutton(text = str(key), variable = varList[myCount])
        myCheckbutton.grid(row = myCount + 3, column = 0)
        checkbuttonList[myCount] = myCheckbutton
        surname = Label(myWindow, text = myDict[key][1])
        surname.grid(row = myCount + 3, column = 1)
        name = Label(myWindow, text = myDict[key][0])
        name.grid(row = myCount + 3, column = 2)
        patronomic = Label(myWindow, text = myDict[key][2])
        patronomic.grid(row = myCount + 3, column = 3)
        position = Label(myWindow, text = myDict[key][3])
        position.grid(row = myCount + 3, column = 4)
        salary = Label(myWindow, text = myDict[key][4])
        salary.grid(row = myCount + 3, column = 5)
        labelList[myCount] = [surname, name, patronomic, position, salary]
        myCount += 1

# инициализация окна
myWindow = Tk()
myWindow.title('ДЗ-8')
myWindow.geometry('540x600')
myWindow.resizable(width=False, height=False)

# кнопка добавить
addButton = Button(myWindow, text = "Добавить", width = 10, height = 2, font=('Courier', 10), command = myAdd)
addButton.grid(row = 0, column = 0)

# кнопка найти
findButton = Button(myWindow, text = "Найти", width = 10, height = 2, font=('Courier', 10), command = None)
findButton.grid(row = 0, column = 1)

# кнопка экспорт
exportButton = Button(myWindow, text = "Экспорт", width = 10, height = 2, font=('Courier', 10), command = myExport)
exportButton.grid(row = 0, column = 2)

# кнопка изменить
changeButton = Button(myWindow, text = "Изменить", width = 10, height = 2, font=('Courier', 10), command = myChange)
changeButton.grid(row = 0, column = 3)

# кнопка удалить
deleteButton = Button(myWindow, text = "Удалить", width = 10, height = 2, font=('Courier', 10), command = myDelete)
deleteButton.grid(row = 0, column = 4)

# кнопка удалить
menuButton = Button(myWindow, text = "Справка", width = 10, height = 2, font=('Courier', 10), command = None)
menuButton.grid(row = 0, column = 5)

# вывести строку наименования таблицы БД
Label(myWindow, text = "Фамилия").grid(row = 1, column = 1)
Label(myWindow, text = "Имя").grid(row = 1, column = 2)
Label(myWindow, text = "Отчество").grid(row = 1, column = 3)
Label(myWindow, text = "Должность").grid(row = 1, column = 4)
Label(myWindow, text = "З/П").grid(row = 1, column = 5)

#
enSurname = Entry(width = 10, font=('Courier', 10))
enSurname.grid(row = 2, column = 1)
enName = Entry(width = 10, font=('Courier', 10))
enName.grid(row = 2, column = 2)
enPatronomic = Entry(width = 10, font=('Courier', 10))
enPatronomic.grid(row = 2, column = 3)
enPosition = Entry(width = 10, font=('Courier', 10))
enPosition.grid(row = 2, column = 4)
enSalary = Entry(width = 10, font=('Courier', 10))
enSalary.grid(row = 2, column = 5)

# цикл вывода Checkbutton и строчек БД
myCount = 3
for key in myDict:
    varList.append(IntVar())
    myCheckbutton = Checkbutton(text = str(key), variable = varList[myCount - 3])
    myCheckbutton.grid(row = myCount, column = 0)
    checkbuttonList.append(myCheckbutton)
    surname = Label(myWindow, text = myDict[key][1])
    surname.grid(row = myCount, column = 1)
    name = Label(myWindow, text = myDict[key][0])
    name.grid(row = myCount, column = 2)
    patronomic = Label(myWindow, text = myDict[key][2])
    patronomic.grid(row = myCount, column = 3)
    position = Label(myWindow, text = myDict[key][3])
    position.grid(row = myCount, column = 4)
    salary = Label(myWindow, text = myDict[key][4])
    salary.grid(row = myCount, column = 5)
    labelList.append([surname, name, patronomic, position, salary])
    myCount += 1
    
# открыть окно
myWindow.mainloop()
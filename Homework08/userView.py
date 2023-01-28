from tkinter import *
import TestControl as control

varList = []
slideButton = {}
slideButtonTumbler = [False, False, False]


def mainWindow():
    # инициализация окна
    myWindow = Tk()
    myWindow.title('Project01')
    myWindow.geometry('540x600')
    myWindow.resizable(width=False, height=False)
    return myWindow


# Верхнее меню
def upMenu(myWindow):
    # кнопка справка
    menuButton = Button(myWindow, text="Сотрудники", width=10, height=2, font=('Courier', 10),
                        command=control.showInformation)
    menuButton.grid(row=0, column=0)
    # кнопка добавить
    addButton = Button(myWindow, text="Добавить", width=10, height=2, font=('Courier', 10), command=control.addMember)
    addButton.grid(row=0, column=1)
    # кнопка найти
    findButton = Button(myWindow, text="Найти", width=10, height=2, font=('Courier', 10), command=control.findMember)
    findButton.grid(row=0, column=2)
    # кнопка изменить
    selectionButton = Button(myWindow, text="Выборка", width=10, height=2, font=('Courier', 10),
                             command=lambda: selectionView(myWindow))
    selectionButton.grid(row=0, column=3)
    # кнопка удалить
    ectionButton = Button(myWindow, text="Действия", width=10, height=2, font=('Courier', 10),
                          command=lambda: actionView(myWindow))
    ectionButton.grid(row=0, column=4)
    # кнопка экспорт
    exportButton = Button(myWindow, text="Экспорт", width=10, height=2, font=('Courier', 10),
                          command=lambda: exportView(myWindow))
    exportButton.grid(row=0, column=5)
    # Отступ
    Label(myWindow, text='', width=10, height=2).grid(row=1, column=2)


# Высплывающии кнопки:
# Экспорт
def exportView(myWindow):
    global slideButton
    if not slideButtonTumbler[2]:
        JSONButton = Button(myWindow, text="JSON", width=10, height=2, font=('Courier', 10), command=control.exportJSON)
        TXTButton = Button(myWindow, text="TXT", width=10, height=2, font=('Courier', 10), command=control.exportTXT)
        JSONButton.grid(row=1, column=5)
        TXTButton.grid(row=2, column=5)
        slideButton['JSON'] = JSONButton
        slideButton['TXT'] = TXTButton
    else:
        slideButton['JSON'].destroy()
        slideButton['TXT'].destroy()
    slideButtonTumbler[2] = not slideButtonTumbler[2]

# Выборка
def selectionView(myWindow):
    global slideButton
    if not slideButtonTumbler[1]:
        positionButton = Button(myWindow, text="Должность", width=10, height=2, font=('Courier', 10), command=control.position)
        salaryButton = Button(myWindow, text="Зарплата", width=10, height=2, font=('Courier', 10), command=control.salary)
        slideButton['position'] = positionButton
        slideButton['salary'] = salaryButton
        positionButton.grid(row=1, column=3)
        salaryButton.grid(row=2, column=3)
    else:
        slideButton['position'].destroy()
        slideButton['salary'].destroy()
    slideButtonTumbler[1] = not slideButtonTumbler[1]

# Действия
def actionView(myWindow):
    global slideButton
    if not slideButtonTumbler[0]:
        changeButton = Button(myWindow, text="Изменить", width=10, height=2, font=('Courier', 10), command=control.update)
        delButton = Button(myWindow, text="Удадить", width=10, height=2, font=('Courier', 10), command=control.delMember)
        slideButton['change'] = changeButton
        slideButton['del'] = delButton
        changeButton.grid(row=1, column=4)
        delButton.grid(row=2, column=4)
    else:
        slideButton['change'].destroy()
        slideButton['del'].destroy()
    slideButtonTumbler[0] = not slideButtonTumbler[0]



# Список на экране
def viewList(myDict, myWindow):
    labelList = []
    checkbuttonList = []
    space = 10
    myCount = space
    varList.clear()
    clear(myWindow)

    # цикл вывода Checkbutton и строчек БД
    for key in myDict:
        varList.append(BooleanVar())
        myCheckbutton = Checkbutton(text=key, variable=varList[myCount - space])
        myCheckbutton.grid(row=myCount, column=0)
        checkbuttonList.append(myCheckbutton)
        surname = Label(myWindow, text=myDict[key][1])
        surname.grid(row=myCount, column=1)
        name = Label(myWindow, text=myDict[key][0])
        name.grid(row=myCount, column=2)
        patronomic = Label(myWindow, text=myDict[key][2])
        patronomic.grid(row=myCount, column=3)
        position = Label(myWindow, text=myDict[key][3])
        position.grid(row=myCount, column=4)
        salary = Label(myWindow, text=myDict[key][4])
        salary.grid(row=myCount, column=5)
        labelList.append([surname, name, patronomic, position, salary])
        myCount += 1

# Чеклист
def watchCheckList(clear = False):
    checkList = [] # Показания счётчиков
    for count, i in enumerate(varList):
        if i.get():
            checkList.append(count)
            if clear:
                i.set(0)
    return checkList # Возвращаем позиции элементов в списке (не в словаре!)



# Добавление сотрудника
def changeField(myWindow, action):
    clear(myWindow)
    # вывести строку наименования таблицы БД
    Label(myWindow, text="Фамилия").grid(row=5, column=0)
    Label(myWindow, text="Имя").grid(row=5, column=1)
    Label(myWindow, text="Отчество").grid(row=5, column=2)
    Label(myWindow, text="Должность").grid(row=5, column=3)
    Label(myWindow, text="З/П").grid(row=5, column=4)
    #
    enSurname = Entry(width=10, font=('Courier', 10))
    enSurname.grid(row=6, column=0)
    enName = Entry(width=10, font=('Courier', 10))
    enName.grid(row=6, column=1)
    enPatronomic = Entry(width=10, font=('Courier', 10))
    enPatronomic.grid(row=6, column=2)
    enPosition = Entry(width=10, font=('Courier', 10))
    enPosition.grid(row=6, column=3)
    enSalary = Entry(width=10, font=('Courier', 10))
    enSalary.grid(row=6, column=4)
    # кнопка добавить
    addButton = Button(myWindow, text="Добавить", width=10, height=2, font=('Courier', 10), \
                       command=lambda: control.changesTransit(action, (
                           enName.get(), enSurname.get(), enPatronomic.get(), enPosition.get(), enSalary.get())))
    addButton.grid(row=6, column=5)


# Окно запросов
def findRequest(myWindow):
    clear(myWindow)
    Label(myWindow, text="Запрос").grid(row=4, column=1)
    request = Entry(width=10, font=('Courier', 10))
    request.grid(row=4, column=2)
    findButton = Button(myWindow, text="Найти", width=10, height=2, font=('Courier', 10), \
                        command=lambda: control.transit(1, (request.get())))
    findButton.grid(row=4, column=3)


# Выбор должности
def profRequest(myWindow):
    clear(myWindow)
    Label(myWindow, text="Должность").grid(row=4, column=1)
    request = Entry(width=10, font=('Courier', 10))
    request.grid(row=4, column=2)
    findButton = Button(myWindow, text="Найти", width=10, height=2, font=('Courier', 10), \
                        command=lambda: control.transit(2, (request.get())))
    findButton.grid(row=4, column=3)


# Выбор зарплаты
def salRequest(myWindow):
    clear(myWindow)
    Label(myWindow, text="От").grid(row=4, column=0)
    downLine = Entry(width=10, font=('Courier', 10))
    downLine.grid(row=4, column=1)
    Label(myWindow, text="До").grid(row=4, column=3)
    upLine = Entry(width=10, font=('Courier', 10))
    upLine.grid(row=4, column=4)
    findButton = Button(myWindow, text="Найти", width=10, height=2, font=('Courier', 10), \
                        command=lambda: control.transit(3, (downLine.get(), upLine.get())))
    findButton.grid(row=6, column=2)


# Всплывающее окно
def infoWindow(message):
    newWindow = Tk()
    newWindow.title('message')
    newWindow.geometry('250x200')
    newWindow.resizable(width=False, height=False)
    Label(newWindow, text=message, width=250, height=200).pack()
    newWindow.mainloop()


# Очистка окна
def clear(myWindow):
    for widget in myWindow.winfo_children():
        widget.destroy()
    upMenu(myWindow)

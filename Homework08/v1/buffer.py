def mainWindow(myDict):
    # инициализация окна
    myWindow = Tk()
    myWindow.title('ДЗ-8')
    myWindow.geometry('540x600')
    myWindow.resizable(width=False, height=False)
    upMenu(myWindow) # Верхнее меню
    indention(myWindow, 2) # Отступ
    viewList(myDict, myWindow) # Окно с данными

    # Мотор
    myWindow.mainloop()
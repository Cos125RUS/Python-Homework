import view as v
import workingWithData as wwd
import convertData as cd
import userView as uv


# Стартовое меню
def start():
    programRun = True # Флаг для зацикливания
    options = [exitOfProgram, findMember, position, salary, addMember, delMember, update, exportJSON, exportCSV, showAllPersonal]
    while programRun:
        # Выбор пользователя в меню:
        userIn = v.showMenu() # v.showMenu заменить на модуль основного меню из windowsView
        if userIn < 0 or userIn > 9:
            v.info('\nОшибка ввода!\n') # Проверка на дурака
            v.request('Нажмите Enter для продолжения работы')  # Задержка экрана до нажатия Enter
        else:
            # Проверка на exit:
            if userIn == 0:
                # Меняем флаг для выхода из программы
                programRun = False
            options[userIn]()


# 1. Найти сотрудника
def findMember():
    # v.showMenu заменить на модуль основного меню из windowsView
    searchParameter = v.request('Введите запрос: ') # Получили запрос
    dataBase = cd.importCSV() # Подгрузили БД
    res = wwd.findPersonal(dataBase, searchParameter) # Получили результат поиска
    v.viewDataBase(res) # Вывод результата
    v.request('Нажмите Enter для продолжения работы') # Задержка экрана до нажатия Enter
    # res отправить на вывод в windowsView
    # содержить не менее одного элемента словаря
    # индек "0" указывает на неудачный поиск и содержит список из одного str-элемента


# 2. Сделать выборку сотрудников по должности
def position():
    # v.showMenu заменить на модуль основного меню из windowsView
    find = v.request('Введите профессию: ') # Запрос профессии для поиска
    dataBase = cd.importCSV() # Подгрузка БД
    res = wwd.sortOfPosition(dataBase, find) # Получили результат поиска
    v.viewDataBase(res) # Вывод результата
    v.request('Нажмите Enter для продолжения работы') # Задержка экрана до нажатия Enter
    # res отправить на вывод в windowsView
    # содержить не менее одного элемента словаря
    # индек "0" указывает на неудачный поиск и содержит список из одного str-элемента



# 3. Сделать выборку сотрудников по зарплате
def salary():
    # v.showMenu заменить на модуль основного меню из windowsView
    dataBase = cd.importCSV() # Подгрузка БД
    min, max = v.salarySort() # Получаем от пользователя два значения int
    res = wwd.sortOfSalary(dataBase, min, max) # Получили результат поиска
    v.viewDataBase(res) # Вывод результата
    v.request('Нажмите Enter для продолжения работы') # Задержка экрана до нажатия Enter
    # res отправить на вывод в windowsView
    # содержить не менее одного элемента словаря
    # индек "0" указывает на неудачный поиск и содержит список из одного str-элемента



# 4. Добавить сотрудника
def addMember():
    # v.showMenu заменить на модуль основного меню из windowsView
    dataBase = cd.importCSV() # Подгрузка БД
    newMember = v.requestPersonalData() # Ввод информации пользователем
    dataBase = wwd.newPersonal(dataBase, newMember) # Получили обновлённую БД
    cd.exportToCSV(dataBase) # Сохраняем БД
    v.info('Сотрудник добавлен') # Вывод сообщения о добавлении
    v.request('Нажмите Enter для продолжения работы') # Задержка экрана до нажатия Enter


# 5. Удалить сотрудника
def delMember():
    # v.showMenu заменить на модуль основного меню из windowsView
    dataBase = cd.importCSV() # Подгрузка БД
    v.viewDataBase(dataBase) # Отображаем список сотрудников
    deletionID = v.enterID() # Запрос ID на удаление
    dataBase = wwd.deletionOnID(dataBase, deletionID) # Получили обновлённую БД
    v.info('Сотрудник удалён') # Вывод сообщения об удалении
    cd.exportToCSV(dataBase) # Сохраняем БД
    v.request('Нажмите Enter для продолжения работы') # Задержка экрана до нажатия Enter


# 6. Обновить данные сотрудника
def update():
    # v.showMenu заменить на модуль основного меню из windowsView
    dataBase = cd.importCSV() # Подгрузка БД
    v.viewDataBase(dataBase) # Отображаем список сотрудников
    changeID = v.enterID() # Запрос ID на изменение
    changeMember = v.requestPersonalData() # Ввод информации пользователем
    dataBase = wwd.reloading(dataBase, changeMember, changeID)
    v.info('Изменения внесены') # Вывод сообщения о внесении изменения
    cd.exportToCSV(dataBase) # Сохраняем БД
    v.request('Нажмите Enter для продолжения работы') # Задержка экрана до нажатия Enter


# 7. Экспортировать данные в формате json
def exportJSON():
    # v.showMenu заменить на модуль основного меню из windowsView
    # передавать словарь
    cd.exportToJSON()
    v.info('Файл JSON создан') # Сообщение о создании файла
    v.request('Нажмите Enter для продолжения работы') # Задержка экрана до нажатия Enter


# 8. Экспортировать данные в формате txt
def exportCSV():
    # v.showMenu заменить на модуль основного меню из windowsView
    cd.exportToTXT() # Сохраняем БД
    v.info('Файл TXT создан')
    v.request('Нажмите Enter для продолжения работы') # Задержка экрана до нажатия Enter



# 9. Отобразить список сотрудников
def showAllPersonal():
    dataBase = cd.importCSV() # Подгрузка БД
    v.viewDataBase(dataBase) # Отображаем список сотрудников
    v.request('Нажмите Enter для продолжения работы') # Задержка экрана до нажатия Enter


# 0. Закончить работу
def exitOfProgram():
    # v.showMenu заменить на модуль основного меню из windowsView
    v.info('Выход из приложения') # Прощальное сообщение
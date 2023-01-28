import workingWithData as wwd
import convertData as cd
import userView as uv

dataBase = cd.importCSV()  # Подгрузили БД
myWindow = uv.mainWindow()  # Загружаем меню
useData = dataBase # Временные данные


# Стартовое меню
def start():
    uv.upMenu(myWindow) # Верхнее меню
    myWindow.mainloop() # Мотор


# 1. Отобразить список сотрудников
def showInformation(data = dataBase):
    global dataBase
    uv.viewList(data, myWindow)


# 2. Добавить сотрудника
def addMember():
    uv.changeField(myWindow, 0)
def saveAddMembers(dataBase, newPers):
    dataBase = wwd.newPersonal(dataBase, newPers)
    cd.exportToCSV(dataBase)
    # uv.infoWindow('Сотрудник добавлен')
    return dataBase


# 3. Найти сотрудника
def findMember():
    uv.findRequest(myWindow)

# 4. Сделать выборку сотрудников по должности
def position():
    uv.profRequest(myWindow)
def checkPosition(position):
    professionsList = cd.importProf()
    return wwd.checkValidPosition(professionsList, position)
def newPos(pos):
    cd.exportProf(pos)

# 5. Сделать выборку сотрудников по зарплате
def salary():
    uv.salRequest(myWindow)


# 6. Удалить сотрудника
def delMember():
    checkList = uv.watchCheckList(True) # Список выбранных позиций (со сбросом выбранных элементов)
    keysList = wwd.createKeysList(useData, checkList) # Ключи
    for delID in keysList:
        wwd.deletionOnID(dataBase, delID)
        if useData != dataBase:
            wwd.deletionOnID(useData, delID)
    cd.exportToCSV(dataBase)
    showInformation(useData) if len(useData) else uv.clear(myWindow)
    # uv.infoWindow('Удалено')


# 7. Обновить данные сотрудника
def update():
    checkList = uv.watchCheckList() # Список выбранных позиций (без сброса флажков)
    if not checkList:
        uv.infoWindow('Выберите сотрудника')
    elif len(checkList) > 1:
        uv.infoWindow('Выбрано несколько сотрудников')
    else:
        uv.changeField(myWindow, 1)
def saveChangeMember(dataBase, personal):
    global useData
    checkList = uv.watchCheckList(True) # Обнуляем флаги
    keysList = wwd.createKeysList(useData, checkList)
    dataBase = wwd.reloading(dataBase, personal, keysList[0])
    cd.exportToCSV(dataBase)
    # useData = wwd.reloading(useData, personal, keysList[0])
    # uv.infoWindow('Данные изменены')
    return dataBase


# 8. Экспортировать данные в формате json
def exportJSON():
    cd.exportToJSON(dataBase)



# 9. Экспортировать данные в формате txt
def exportTXT():
    cd.exportToTXT(dataBase) # Сохраняем БД





# Транзит данных между функциями
def transit(index, data):
    function = [saveAddMembers, wwd.findPersonal, wwd.sortOfPosition, wwd.sortOfSalary, saveChangeMember]
    global useData
    useData = function[index](dataBase, data)
    if 0 in useData.keys():
        uv.infoWindow(*useData[0])
    else:
        showInformation(useData)

def changesTransit(index, data):
    global dataBase
    function = [saveAddMembers, saveChangeMember]
    dataBase = function[index](dataBase, data)
    # print(dataBase)
    if len(dataBase):
        showInformation(dataBase)
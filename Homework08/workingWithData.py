import TestControl as control

# 1. Основные функции:

# 1.1. Поиск сотрудника по ключу и значению
def findPersonal(myDict, request):
    # request - поисковое значение, вводимое с клавиатуры (str)
    res = {}
    satisfyIndex = [0 for i in range(max(myDict.keys()) + 1)] # Список для подсчёта совпадений
    for i in myDict: # Проход по словарю
        for j in myDict[i]: # Проход по элементам
            if request.lower().count(j.lower()):  # Ищем совпадения по объекту поиска
                satisfyIndex[i] += 1  # Считаем количество совпадений в каждом элементе словаря
    if max(satisfyIndex): # Проверка наличия совпадений
        if satisfyIndex.count(max(satisfyIndex)) > 1: # Проверка на несколько совпадений
            satisfyList = [i for i in range(len(satisfyIndex)) if satisfyIndex[i] == max(satisfyIndex)]
            for i in satisfyList:
                res[i] = myDict[i]
        else: # Единственное совпадение
            maxIndex = satisfyIndex.index(max(satisfyIndex))
            res[maxIndex] = myDict[maxIndex]
    else: # Неудачный поиск
        res[0] = ['Сотрудник не найден']
    return res

# 1.2. Выборка сотрудников по должности
def sortOfPosition(myDict, position):
    res = {}
    if control.checkPosition(position):  # Проверка на правильный ввод (если реализуем выбор профессии из списка вместо ввода, проверка не нужна)
        if str(myDict.items()).count(position) > 0:  # Проверка совпадений во всём словаре по запрашиваемой должности
            for i in myDict:
                if myDict[i][3] == position:
                    res[i] = myDict[i]  # Формируем новый словарь из подходящих сотрудников
        else:
            res[0] = ['Нет сотрудников на данной должности']
    else:
        res[0] = ['Должность указана неверно']
    return res


# 1.3. Выборка сотрудников по зарплате
def sortOfSalary(myDict, value):
    min, max = value
    res = {}
    if checkValue(min, max):  # Проверка введённых значений
        for i in myDict:
            if int(min) <= int(myDict[i][4]) <= int(max):  # Проверка критериев по каждому сотруднику
                res[i] = myDict[i]  # Подходящих сотрудников добавляем в новый словарь
        if not len(res):  # Проверка пустого списка результатов
            res[0] = ['Сотрудники с подходящей зарплатой не найдены']
    else:
        res[0] = ['Значение указано неверно']
    return res


# 1.4. Добавление сотрудника в словарь
def newPersonal(myDict, newMember):
    position = newMember[3]
    if not control.checkPosition(position):
        control.newPos(position)
    lastKeys = int(list(myDict.keys())[-1])  # Смотрим id последней записи
    # Проверяем, равен ли последний id общему количеству записей
    if lastKeys == len(myDict):
        newID = len(myDict) + 1
        myDict[newID] = list(newMember)
    else:
        # Поиск пустых строк (при удалении пользователя id не меняется)
        for i, key in enumerate(myDict, 1):
            if int(key) != i:
                # Если находим пустую строку, вписываем туда нового пользователя
                myDict[i] = list(newMember)
                myDict = dict(sorted(myDict.items()))
                break  # Прерываем поиск после первой найденной пустой строки
    return myDict # Не уверен, что его нужно возвращать. Вроде бы, он передаётся по ссылке.


# 1.5(1) Удаление сотрудника по записи
def deletionOnPerson(myDict, delMember):
    for delID in delMember.keys():  # Извлекаем id пользователя
        del myDict[delID]  # Удаляем пользователя по id


# 1.5(2) Удаление сотрудника по ID
def deletionOnID(myDict, delID):
    del myDict[delID]



# 1.6. Обновление данных сотрудника
def reloading(myDict, changedPersonal, PersID):
    deletionOnID(myDict, PersID)  # Удаляем запись сотрудника
    # If checkCorrectInput(myDict, changedPersonal):  # Проверка на повторения (переделать под GUI)
    myDict[PersID] = list(changedPersonal)  # Создаём новую запись под тем же id
    myDict = dict(sorted(myDict.items()))  # Сортируем словарь
    return myDict

# 1.7 Сортировка по флажку
def checkSort(myDict, PersID):
    sortList = {}
    for i in PersID:
        sortList[i] = myDict[i]
    return sortList




# 2. Вспомогательные функции:

# 2.1 Извлечение записи из БД
def takeProfile(myDict, id):
    return {id: myDict[id]}

# 2.2 Сформировать чеклист
def createKeysList(useList, numbers):
    # checkList = {}
    # for i in range(len(useList)):
    #     if i in numbers:
    #         checkList[i] = useList[i]
    # return checkList
    keysList = []
    allKeys = [i for i in list(useList.keys())]
    for i in numbers:
        keysList.append(allKeys[i])
        return keysList



# 3. Проверочные функции:

# 3.1 Проверка поискового значения (профессия)
def checkValidPosition(professions, request):
    return bool(list(check.count(request) for check in professions.items()).count(1))


# 3.2 Проверка поискового значения (зарплата)
def checkValue(min, max):
    if alphaCheck(min) and alphaCheck(max):  # Проверка на символьный ввод
        # Преобразуем строку в число при удачной проверки
        min = int(min)
        max = int(max)
        # Проверка на отрицательные значения и min > max
        if max < 0 or min < 0 or max < min:
            return False
    else:
        return False
    return True


# 3.3 Проверка на символьный ввод
def alphaCheck(value):
    return bool((list(symbol.isalpha() for symbol in value)).count(1) == 0)


# 3.4 Проверка введённых данных о сотруднике (вызывается из Контроллера после полученных от пользователя значений)
def checkCorrectInput(myDict, newMember):
    # Если реализуем пошаговый ввод данных, тогда общую проверку заменим на поочерёдный вызов из Контроллера
    name, surname, patronymic, position, salary = newMember  # Разнуменуем входящие данные
    # Проверка зп на символьные и отрицательные значения
    if not (alphaCheck(salary) and int(salary) > 0):
        return False
    if not checkValidPosition(position):  # Проверяем, не отсутствует ли профессия в нашем списке профессий
        # Создать запрос на добавление новой профессии в список вместо прерывания
        print('Новая профессия')
    # Проверка на повторный ввод сотрудника (поиск аналогичной записи в БД)
    find = checkPersonal(myDict, 1, surname)
    if not (0 in find.keys()):  # Проверяем фамилии на совпадения
        find = checkPersonal(find, 0, name)
        if not (0 in find.keys()):  # Проверяем имена на совпадения
            find = checkPersonal(find, 2, patronymic)
            if not (0 in find.keys()):  # Проверяем отчество на совпадения
                print('Человек с таким ФИО уже записан')  # Запрос пользователю на продолжение ввода
                find = checkPersonal(find, 3, position)
                if not (0 in find.keys()):  # Проверяем должность на совпадения
                    print(
                        'Полное совпадение с ранее записанным сотрудником')  # Запрос пользователю на продолжение ввода
    return True

# 3.5 Проверка на точное совпадение
def checkPersonal(myDict, searchKey, request):
    # searchKey - отправляем из функции 3.4 (int)
    # request - поисковое значение, введённое с клавиатуры (str)
    res = {}
    for i in myDict: # Проход по словарю
        if myDict[i][searchKey].lower() == request.lower(): # Ищем совпадения по объекту поиска
            res[i] = myDict[i]
    if not len(res): # Неудачный поиск
        res[0] = ['Сотрудник не найден']
    return res


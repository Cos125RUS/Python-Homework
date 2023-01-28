# путь к файлу БД
myDataBasePath = 'database.csv'
myProfBasePath = 'profBase.csv'


# метод для экспорта БД в формат .json
def exportToJSON(dataBase):
    myDataBasePathJson = 'database.json'
    # словарь, в который складываются записи из БД
    myList = []
    for i in dataBase.keys():
        line = [i]
        for j in dataBase[i]:
            line.append(j)
        myList.append(line)
    with open(myDataBasePathJson, 'w+', encoding = 'utf-8') as jsonFile:
        # построчно записываем в формате JSON
        jsonFile.write('[')
        # переменная для подсчета количества записей
        myCount = 0
        for item in myList:
            jsonFile.write('\n')
            jsonFile.write('    {' + '\n')
            jsonFile.write(f'        "id": {item[0]},\n')
            jsonFile.write(f'        "surname": {item[2]},\n')
            jsonFile.write(f'        "name": {item[1]},\n')
            jsonFile.write(f'        "patronymic": {item[3]},\n')
            jsonFile.write(f'        "position": {item[4]},\n')
            jsonFile.write(f'        "salary": {item[5]}\n')
            myCount += 1
            # определяем надо ли ставить запятую в конце
            if myCount != len(myList):
                jsonFile.write('    },')
            else:
                jsonFile.write('    }')
        jsonFile.write('\n]')
        
# метод для экспорта БД в формат .txt
def exportToTXT(dataBase):
    myDataBasePathTxt = 'database.txt'
    # словарь, в который складываются записи из БД
    myList = []
    for i in dataBase.keys():
        line = f'{i}. '
        for j in dataBase[i]:
            line += f'{j} '
        line += '\n'
        myList.append(line)
    # открываем или создаем файл TXT на запись
    with open(myDataBasePathTxt, 'w+', encoding = 'utf-8') as txtFile:
        # построчно записываем список
        for item in myList:
            txtFile.write(item)

# сохранение БД
def exportToCSV(myDict):
    # открываем файл на запись
    with open(myDataBasePath, 'w+', encoding = 'utf-8') as dataBase:
        dataBase.write(f'id;name;surname;patronymic;position;salary;\n')
        # переменная подсчета записей
        myCount = 0
        for key in myDict:
            # пропускаем первую строку
            myString = str(key) + ';'
            for item in myDict[key]:
                myString += str(item) + ';'
            myCount += 1
            if myCount != len(myDict):
                myString += '\n'
            dataBase.write(myString)

# метод для импорта БД в формат .csv. Используется для выдачи словаря, для последующей работы с ним
def importCSV():
    # словарь, в который складываются записи из БД
    myDict = {}
    # открываем файл на чтение
    with open(myDataBasePath, 'r', encoding = 'utf-8') as dataBase:
        for line in dataBase:
            # пропускаем первую строку
            if line.strip()[0] != 'i':
                # инкрементируем счетчик
                oneLine = line.strip()
                count = 1
                while oneLine[count] != ';':
                    count += 1
                memberID = int(oneLine[:count])
                # разбиваем строку и формируем список
                myList = line.strip().split(';')
                # удалить последний элемент ''
                myList.remove('')
                myList.pop(0)
                myDict[memberID] = myList
    # возвращаем словарь
    return myDict


def importProf():
    dictProf = {}
    with open(myProfBasePath, 'r', encoding = 'utf-8') as ProfBase:
        text = ProfBase.read()
        if len(text):
            lines = text.split('\n')
            # инкрементируем счетчик
            for i in range(len(lines)):
                if len(lines[i]):
                    dictProf[i] = lines[i]
        else:
            dictProf[0] = ''
    # возвращаем словарь
    return dictProf


def exportProf(newPosition):
    # открываем файл на запись
    with open(myProfBasePath, 'a', encoding='utf-8') as profBase:
        newPosition = newPosition + '\n'
        profBase.write(newPosition)

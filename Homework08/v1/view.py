def showMenu() -> int:
    print("\n" + "=" * 50)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Отобразить список сотрудников")
    print("0. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


# 1. Запрос на выборку сотрудников по зарплате
def salarySort():
    print('Укажите критерии поиска')
    min = input('От: ')
    max = input('До: ')
    return min, max


# 2. Запрос данных по сотруднику
def requestPersonalData():
    surname = input('Фамилия: ')
    name = input('Имя: ')
    patronymic = input('Отчетсво: ')
    position = input('Должность: ')
    salary = input('Зарплата: ')
    return (name, surname, patronymic, position, salary)


# 3. Вывод сообщения
def info(message):
    print(message)


# 4. Вывод на экран списка сотрудников
def viewDataBase(dataBase):
    print("\n" + "=" * 50)
    print("Список сотрудников:\n")
    for key in dataBase:
        print(key, end='.  ')
        for j in dataBase[key]:
            print(j, end='  ')
        print()
    print()


# 5. Запрос ID
def enterID():
    return int(input('Укажите ID сотрудника: '))


# 6. Запрос строки
def request(message):
    return input(message)





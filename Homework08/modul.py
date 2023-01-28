import csv


# 1. Найти сотрудника
def find_personal(key):
    with open('members.cvs', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                name, surname, position, salary = i.split(';')
                return f'{name} {surname}\n{position}\n{salary}'
            else:
                return 'Not found'


# 2. Сделать выборку сотрудников по должности
def sort_of_position():

    return 0



# 3. Сделать выборку сотрудников по зарплате
def sort_of_salary():

    return 0


# 4. Добавить сотрудника
def new_personal(card):
    name, surname, position, salary = card
    with open('members.cvs', 'a') as data:
        member = f'{name};{surname};{position};{salary}\n'
        data.write(member)
    return 'New member was create'



# 5. Удалить сотрудника
def deletion():

    return 0



# 6. Обновить данные сотрудника
def reloading():

    return 0



# 7. Экспортировать данные в формате json
def to_json():

    return 0



# 8. Экспортировать данные в формате csv
def to_csv(dict_data):
    with open('data_json.csv', 'w') as csvfile:
        fieldnames = ['name', 'surname', 'position', 'salary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(dict_data)



# 9. Закончить работу
def exit_of_system():

     return 0
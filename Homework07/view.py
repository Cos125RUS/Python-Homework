
# Ввод данных

# Создать новый контакт
def add_new():
    name = input('Name: ')
    phone = input('Phone number: ')
    return (name, phone)


# Поиск телефона в списке контактов
def find_phone():
    return input('Name: ')


# Основное меню
def show_nemu():
    return input('1 - create new contact\n' \
                   '2 - find contact\n' \
                   '3 - export contacts to txt\n' \
                   '4 - export contacts to xml\n' \
                   '0 - exit\n')




# Вывод данных на экран

def view_res(res):
    print(f"{res}\n")
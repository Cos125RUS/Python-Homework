import view as v
import module as m


# Создать новый контакт
def create_contact():
    return m.create(v.add_new())


# Поиск телефона в списке контактов
def find_contact():
    return m.find(v.find_phone())


# Экспорт контактов в txt
def export_contact():
    return m.export()


# Основное меню
def menu(answer):
    if answer == '0':
        show_res('Bye-bye')
    else:
        if answer == '1':
            show_res(create_contact())
        elif answer == '2':
            show_res(find_contact())
        elif answer == '3':
            show_res(export_contact())
        else:
            show_res('Input Error')
        menu(v.show_nemu())


# Отправка на печать
def show_res(res):
    v.view_res(res)
import controller as control
import view as v


def create(data):
    with open('contacts.csv', 'a') as book:
        book.write(f'{data[0]};{data[1]};\n')
        return 'Create new contact'

def find(name):
    with open('contacts.csv', 'r') as data:
        lines = data.read().split('\n')
        book = {}
        for i in lines[0:-1]:
            member = i.split(';')
            book[member[0]] = member[1]
        if name in book.keys():
            return book[name]
        else:
            return 'Not found'


def export():
    with open('contacts.csv', 'r') as data:
        lines = data.read().split('\n')
        txt = ''
        for i in lines[0:-1]:
            member = i.split(';')
            txt += f'{member[0]} {member[1]}\n'
        with open('contacts_book.txt', 'w') as book:
            book.truncate()
            book.write(txt)
        return 'Txt-file was creation'

def choice(answer):
    if answer == '0':
        control.show_res('Bye-bye')
    else:
        if answer == '1':
            control.show_res(control.create_contact())
        elif answer == '2':
            control.show_res(control.find_contact())
        elif answer == '3':
            control.show_res(control.export_contact())
        else:
            control.show_res('Input Error')
        choice(v.show_nemu())

# Создать новый контакт
def create(data):
    with open('contacts.csv', 'a') as book:
        book.write(f'{data[0]};{data[1]};\n')
        return 'Create new contact'


# Поиск телефона в списке контактов
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


# Экспорт контактов в txt
def export_txt():
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


# Экспорт контактов в xml
def export_xml():
    with open('contacts.csv', 'r') as data:
        lines = data.read().split('\n')
        xml = '<xml>\n'
        for i in lines[0:-1]:
            member = i.split(';')
            xml += f'    <name units = "{member[0]} ">{member[1]}</name>\n'
        xml += '</xml>'
        with open('contacts_book.xml', 'w') as book:
            book.truncate()
            book.write(xml)
        return 'Xml-file was creation'
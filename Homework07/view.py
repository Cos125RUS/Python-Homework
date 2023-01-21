

def add_new():
    name = input('Name: ')
    phone = input('Phone number: ')
    return (name, phone)


def find_phone():
    return input('Name: ')

def show_nemu():
    return input('1 - create new contact\n' \
                   '2 - find contact\n' \
                   '3 - export contacts to txt\n' \
                   '0 - exit\n')


def view_res(res):
    print(f"{res}\n")
import controller as contol


flag = True
while(flag):
    choice = input('1 - create new contact\n'\
          '2 - find contact\n'\
          '3 - export contacts to txt\n'\
          '0 - exit\n')
    if choice == '1':
        print(contol.create_contact() + '\n')
    elif choice == '2':
        print(contol.find_contact() + '\n')
    elif choice == '3':
        print(contol.export_contact() + '\n')
    elif choice == '0':
        flag = False
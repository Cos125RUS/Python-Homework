from tkinter import *

#
# root = tk.Tk()
# root.geometry("100x50")
#
# button = tk.Button(command = root.quit)
# # button.pack()
#
# root.mainloop()

# a = []
# for i in dic.keys():
#     line = f'{i}. '
#     for j in dic[i]:
#         line += j
#     a.append(f'{line}')


# dic = {1: ['456456', 'dsgfsdf'], 2: '6456456', 3: '6168168'}
# if 1 in dic.keys():
#     print(dic[1])
#
# dictProf = {}
# with open('profBase.csv', 'r', encoding='utf-8') as ProfBase:
#     text = ProfBase.read()
#     if len(text):
#         lines = text.split('\n')
#         # инкрементируем счетчик
#         for i in range(len(lines)):
#             if len(lines[i]):
#                 dictProf[i] = lines[i]
#     else:
#         dictProf[0] = ''
# print(dictProf)


# def z(root):
#     if root.a.get():
#         t = 1
#     else:
#         t = 2
#     print(t)
#
# root = Tk()
# root.geometry("250x150+300+300")
# a = IntVar()
# Checkbutton(text="Показать заголовок", variable=a).pack()
# Button(text="Показать заголовок", command=z).pack()
# root.mainloop()
# root = Tk()
#
# ch_var1 = BooleanVar()
# Checkbutton(text="First", variable=ch_var1).pack(anchor=W)
#
#
# Button(text="Показать", command=lambda: print(1) if ch_var1.get() else print(2)).pack()
#
# root.mainloop()

myDict = {0: 1234, 5: 5161, 1: 234234}
dict2 = {0: 123}
myDict = dict(sorted(myDict.items()))
print(myDict)
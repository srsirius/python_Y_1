
 

# if __name__ == '__main__':
    
#     def print_name(name):
#         print(name)
    
#     package = ('9:36:02', 15000)
#     print(type(package))
#     print_name('Sirius4')
#     print('fff')
#     input('')

# def cut_list_num(list_num: list):
#     res = [list_num[0]]
#     for i in range(1, len(list_num)):
#         if list_num[i] != list_num[i-1]:
#             res.append(list_num[i])
#     return res

# def print_message(list1, list2):
#     if list1 == list2:
#         print('YES')
#     else:
#         print('NO')
    
# massiv1 = list(map(int, input().split(' ')))
# massiv2 = list(map(int, input().split(' ')))
# formated_massiv1 = cut_list_num(massiv1)
# formated_massiv2 = cut_list_num(massiv2)

# print_message(formated_massiv1, formated_massiv2)

# data = list(map(int, input().split(' ')))
# massiv2 = list(map(int, input().split(' ')))
# count = 0
# max = massiv2[data[0]-1]

# for i in range(0,max -1):
#     if i < max:
#         i += data[1]
#         count += 1
# print(count)


import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Выбор меню")
root.geometry('300x100')

style = ttk.Style()
style.theme_use('clam')

options = [
    "Option 1",
    "Option 2",
    "Option 3",
]

option_menu = ttk.Combobox(root, values=options, state="readonly")
option_menu.current(0)
option_menu.bind("<<ComboboxSelected>>", lambda event: print(f"You selected: {option_menu.get()}"))
option_menu.place(x=50, y=25)





button2 = tk.Button(root, text='Отмена', command='exit')
button2.pack(side='right', anchor='sw')
button1 = tk.Button(root, text='Выбрать')
button1.pack(side='right', anchor='se')

root.mainloop()





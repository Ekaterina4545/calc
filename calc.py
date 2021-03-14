from tkinter import *
from make_shape import *
#строку ввода создаем до функции, т.к. из неё будем получать значения
calc_entry = Entry(calc, font='Leelawadee 18', bg='white', width=24)
calc_entry.grid(row=1, column=0, columnspan=4, pady=8)
calc_entry.focus()
#my_math принимает сохраненный оператор, сохраненное число и текущее число из поля ввода
#возвращает1.результат взаимодействия числа из памяти, оператора из памяти и текущего числа2.текущий оператор3.ошибку
#если не было попыток деления на ноль, строка ошибки будет пустой
#при попытке деления на ноль текущий оператор обнулится
def my_math(total_number, total_simbol, number, x):
    error = ''
    if total_simbol == '+':
        total_number += number
    elif total_simbol == '-':
        total_number -= number
    elif total_simbol == '*':
        total_number *= number
    elif total_simbol == '/':
        try:
            total_number /= number
        except ZeroDivisionError:
            total_number = ''
            x = ''
            error = 'ошибка'
    if total_number != '':
        total_number = round(total_number, 2)
    return total_number, x, error
#переменные, которые сохраняют в памяти то, что было введено
total_number = 0
total_simbol = ''
memory = ''
#функция для обработки ввода с клавиатуры присвает переменной х значение клавиши
#и вызывает функцию обработки памяти, если введен символ, использующийся в вычислении
#при этом возвращает строку "break" из обработчика и событие не будет отправлено следующим обработчикам
#в том числе и стандартному, который отвечает за вывод букв в текстовое поле
def what_is_button(event):
    x = event.char
    super_list = ['-', '+', '*', '/', '=']
    if x in super_list:
        button_get(x)
        return "break"
#функция для обработки нажатия enter на клавиатуре
def press_enter(event):
    button_get('=')
#функция для обработки нажатия delete на клавиатуре
def press_delete(event):
    button_get('C')
#функция обработки памяти калькулятора
def button_get(x):
#в переменной total_number хранится число, которое было введено пользователем до математического оператора
#или результат предыдущих вычислений
    global total_number
#в переменной total_simbol хранится введенный оператор для обработки первого и второго ввода чисел
    global total_simbol
#переменная memory для вывода результата и обнуления памяти после завершения вычислений или при возникновении ошибки
    global memory
#память и вывод результа обнуляются при следующем вводе, если до этого была ошибка или вычисления завершены,нажато "="
    if total_simbol == '=' or memory == 'ошибка':
        memory = ''
        resalt_output.config(text='')
    math_list = ['-', '+', '*', '/']
    if x in math_list:
#пустая память означает, что это первый ввод, или до этого мы получили результат, или была ошибка
#присваиваем значения переменным total_number и total_simbol
#пробуем получить значение из строки ввода и привести его к целому числу
#ошибка означает, что введено не число, а, вероятно, символ, поэтому значение total_number не меняем, оно остается 0
#если ошибки нет, то заменим значение переменной total_number введенным числом и сохраняем его в памяти
#сохраняем в памяти введенный символ и выводим в поле 'журнал'(кнопка memory_otput)
        if memory == '':
            try:
               int(calc_entry.get())
            except ValueError:
                pass
            else:
                total_number = int(calc_entry.get())
                memory += str(total_number)
            total_simbol = x
            memory += total_simbol
            memory_otput.config(text=memory)
            calc_entry.delete(0, END)
#в памяти уже есть символ и/или число
#получаем текущее число из строки ввода, присваиваем его значение переменной number
#вызываем математическую функцию, куда передаем 1.число и символ из памяти 2.текущие число и символ(х)
#получаем, сохраняем в памяти и выводим новое число после произведенных вычислений
#передать значение х математической функции и только после возврата присвоить total_simbol строковое значение х
#и сохранить в памяти нужно для обработки ошибки деления на 0
        else:
            number = int(calc_entry.get())
            total_number, x, error = my_math(total_number, total_simbol, number, x)
            total_simbol = str(x)
            if error != '':
                memory = error
            else:
                memory = str(total_number)
                memory += total_simbol
            memory_otput.config(text=memory)
            calc_entry.delete(0, END)
#если введен не математический символ, а '=', добавляем к памяти значение последнего введенного символа
#производим вычисления с последним символом
#выводим результат в поле 'результат'(кнопка resalt_output)
    elif x == '=':
        memory += calc_entry.get()
        number = int(calc_entry.get())
        total_number, x, error = my_math(total_number, total_simbol, number, x)
        if error != '':
            memory = error
        memory_otput.config(text=memory)
        calc_entry.delete(0, END)
        resalt_output.config(text=total_number)
        total_simbol = str(x)
#если введена кнопка сброса - обнуляем значения total_number, полей 'результат' и 'журнал' и память
#когда память обнулена, значение total_simbol будет присвоено при следующем вводе
    elif x == 'C':
        memory = ''
        total_number = 0
        resalt_output.config(text='')
        memory_otput.config(text='')
        calc_entry.delete(0, END)
#условие для отражения в строке ввода чисел
#сработает только при вводе символов из интерфейса калькулятора
    else:
        calc_entry.insert(END, x)
#матрица для создания кнопок калькулятора
list_row = [[7, 8, 9, '+'], [4, 5, 6, '-'], [1, 2, 3, '*'], ['C', 0, '=', '/']]
#цикл для размещения кнопок калькулятора в окне и вызове функции обработки ввода при нажатии
for i in range(len(list_row)):
    for j in range(len(list_row[i])):
        cmd = lambda x=list_row[i][j]: button_get(x)
        calc_button = Button(calc, text=list_row[i][j], font='Leelawadee 18', width=5, command=cmd)
        calc_button.grid(row=i+3, column=j, pady=3, padx=2)
#обработка нажатия клавиш на клавиатуре
calc_entry.bind('<Key>', what_is_button)
calc_entry.bind('<Return>', press_enter)
calc_entry.bind('<Delete>', press_delete)
#создание и размеещние описания метки журнала
memory_otput_name = Label(font='Leelawadee 10', text='журнал')
memory_otput_name.grid(row=0, column=5)
#создание и размеещние метки журнала
memory_otput = Label(width=15, font='Leelawadee 18')
memory_otput.grid(row=0, column=0, columnspan=4, pady=4)
#создание и размеещние описания метки результат
resalt_output_name = Label(font='Leelawadee 10', text='результат')
resalt_output_name.grid(row=2, column=5)
#создание и размеещние метки результат
resalt_output = Label(width=15, font='Leelawadee 18')
resalt_output.grid(row=2, column=0, columnspan=4, pady=4)
#фон калькулятора и отступы по горизонтали
calc.config(bg='#f5f1f2', padx=40)
#запуск
calc.mainloop()
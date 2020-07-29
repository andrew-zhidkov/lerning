import time


print('\t\t___Мастер Python___')
print('Приветствую тебя начинающий программист!')


userName = ''
while len(userName) == 0:#Пока длинна userName = 0 повторять запрос
    userName = input('Как тебя зовут:\n')


print('Очень приятно ' + userName + ', я Python !\n')
time.sleep(1)
print('Я могу рассказать тебе о том, что я умею!\n')
time.sleep(1)


work = '' #Чтобы не было ошибки в цикле while ниже

while type(work) != int or work != 2:
    work = input(userName + ' позанимаемся полезними делами?\n'
                                    '[1] - Да, хочу провести время с пользой\n'
                                    '[2] - На сегодня, пожалуй закончим\n'
                                    '\n\nВведи цифру своего ответа: \n')
    #проверка ответа пользователя:
    try:
        work = int(work)
    except ValueError:
        print('\n___!!!_Нужно ввести цифру_!!!___\n')
        time.sleep(0.5)
    main = 999
    if work == 1:
        try:
            main = int(input('\t\tВыбери тему:\n'
                                 'Выполнение операций\n'
                                '\t[1] Арифметические действия\n'
                                '\t[2] Присваивание значений\n'
                                '\t[3] Сравнение величин\n'
                                '\t[4] Оценочная логика\n'
                                '\t[5] Проверка условий\n'
                                '\t[6] Определение приоритетов\n'
                                 'Веди цифру интересной тебе темы и нажми Enter:\n'
                                 '\n[0] - Выход\n'))
        except ValueError:
            print('\n___!!!_Нужно ввести цифру_!!!___\n')
            time.sleep(0.5)
        if main == 1:
            print('В этом модуле разберем математичесткие операторы:\n'
                    '+\t' 'Сложение - Addition\n'
                    '-\t' 'Вычитание - Substraction\n'
                    '*\t' 'Умножение - Multiplication\n'
                    '/\t' 'Деление - Division\n'
                    '//\t' 'Целочисленное деление - Floor Divison\n'
                    '%\t' 'Деление по модулю - Modulus\n'
                    '**\t' 'Возведение в степень - Exponent\n')
            time.sleep(2)
            print('Для того чтобы лучше понять, задумай два числа от 1 до 9.\n')
            answer = 'Y'
            while answer == 'Y':
                # Запрос информации от пользователя
                num1 = ''
                num2 = ''
                while num1 != int:
                    num1 = input('Введи первое число:\n')
                    try:
                        num1 = int(num1)
                        break
                    except ValueError:
                        print('\n___!!!_Нужно ввести цифру_!!!___\n')
                        time.sleep(1)
                while num2 != int:
                    num2 = input('Введи второе число:\n')
                    try:
                        num2 = int(num2)
                        break
                    except ValueError:
                        print('\n___!!!_Нужно ввести цифру_!!!___\n')
                        time.sleep(1)
                # Демонстрация арифметических действий и результата их выполнения
                print('\nВот результаты действий над числами: ', num1, ' и ', num2)
                time.sleep(1)
                print('\nAddition:\t\t', num1, '+', num2, '=', num1 + num2)
                print('Substraction:\t', num1, '-', num2, '=', num1 - num2)
                print('Multiplicatin:\t', num1, '*', num2, '=', num1 * num2)
                print('Division:\t\t', num1, '/', num2, '=', num1 / num2)
                print('Floor Division:\t', num1, '//', num2, '=', num1 // num2)
                print('Modulus:\t\t', num1, '%', num2, '=', num1 % num2)
                print('Exponent:\t\t', num1, '**', num2, "=", num1 ** num2)
                print('\n!!!Важно!!! Деление - Division всегда возвращает часло с плавающей точкой!')
                print('!!!Важно!!! Деление по модулю - Floor Divison возвращает только целое число, отбрасывая остаток!')
                print('!!!Важно!!! Целочисленное деление - Modulus возвращает остаток после деления!')
                answer = input('\nПопробовать еще раз?\n'
                               '[Y] - да\n'
                               '[N] - нет: \n')
                answer = str.upper(answer)  # возводим ответ в заглавную букву
            print('\nУдачного изучения!')
            time.sleep(0.5)
        elif main == 2:
            print('Сейчас ' + userName + ' ты узнаешь, об операторах присваивания значений.\n')
            print('Необходимо это, в тех случаях, когда нужно переменной присвоить значение или изменить его.\n')
            print('Ты уже знаешь один из операторов присваивания, это знак: = \n')
            print('Теперь рассмотрим другие:')
            print('\nОператор\t' + 'Пример' + '\tЭквивалентная операция\n')
            print('=' + '\t\t\ta = b' + '\t\ta = b')
            print('+=' + '\t\t\ta += b' + '\t\ta = (a + b)')
            print('-=' + '\t\t\ta -= b' + '\t\ta = (a - b)')
            print('*=' + '\t\t\ta *= b' + '\t\ta = (a * b)')
            print('/=' + '\t\t\ta /= b' + '\t\ta = (a / b)')
            print('%=' + '\t\t\ta %= b' + '\t\ta = (a % b)')
            print('//=' + '\t\t\ta //= b' + '\t\ta = (a // b)')
            print('**=' + '\t\t\ta **= b' + '\t\ta = (a ** b)')
            time.sleep(4)
            print('\nМне снова понадобися от тебя 2 числа, желательно от 1 до 9.')
            num1 = ''
            num2 = ''
            while num1 != int:
                num1 = input('Введи первое число:\n')
                try:
                    num1 = int(num1)
                    break
                except ValueError:
                    print('\n___!!!_Нужно ввести цифру_!!!___\n')
                    time.sleep(1)
            while num2 != int:
                num2 = input('Введи второе число:\n')
                try:
                    num2 = int(num2)
                    break
                except ValueError:
                    print('\n___!!!_Нужно ввести цифру_!!!___\n')
                    time.sleep(1)
            print('Загаданы числа:')
            print('\na = ', num1, '\tb = ', num2)
            time.sleep(2)
            print('\nОператор\t' + 'Пример' + '\tРезультат' + '\tЧто произошло\n')
            num1 = num2
            print("=" + '\t\t\ta = b' + '\t\ta = ', num1, '\t\tПеременной а присвоилось значение переменной b: a = b')
            print('Теперь в переменных значения:')
            print('a = ', num1, '\tb = ', num2)
            num1 += num2
            print('+=' + '\t\t\ta += b' + '\t\ta = ', num1, '\t\ta = (a + b)')
            print('Теперь в переменных значения:')
            print('a = ', num1, '\tb = ', num2)
            num1 -= num2
            print('-=' + '\t\t\ta -= b' + '\t\ta = ', num1, '\t\t\ta = (a - b)')
            print('Теперь в переменных значения:')
            print('a = ', num1, '\tb = ', num2)
            num1 *= num2
            print('*=' + '\t\t\ta *= b' + '\t\ta = ', num1, '\t\ta = (a * b)')
            print('Теперь в переменных значения:')
            print('a = ', num1, '\tb = ', num2)
            num1 /= num2
            print('/=' + '\t\t\ta /= b' + '\t\ta = ', num1, '\t\ta = (a / b)')
            print('Теперь в переменных значения:')
            print('a = ', num1, '\tb = ', num2)
            num1 %= num2
            print('%=' + '\t\t\ta %= b' + '\t\ta = (a % b)', num1, '\t\ta = (a % b)')
            print('Теперь в переменных значения:')
            print('a = ', num1, '\tb = ', num2)
            print('Если не изменить числа, то далее все действия будут равны 0\nНам ведь это не интересно, давай изменим значение переменой а')
            while num1 != int:
                num1 = input('Введи число для переменной а:\n')
                try:
                    num1 = int(num1)
                    break
                except ValueError:
                    print('\n___!!!_Нужно ввести цифру_!!!___\n')
                    time.sleep(1)
            print('a = ', num1, '\tb = ', num2)
            num1 //= num2
            print('//=' + '\t\t\ta //= b' + '\t\ta = (a // b)', num1, '\t\ta = (a // b)')
            print('Теперь в переменных значения:')
            print('a = ', num1, '\tb = ', num2)
            num1 **= num2
            print('**=' + '\t\t\ta **= b' + '\t\ta = (a ** b)', num1, '\t\ta = (a ** b)')
            print('Теперь в переменных значения:')
            print('a = ', num1, '\tb = ', num2)
            time.sleep(4)
        elif main == 0:
            print(userName + ' увидимся в другой раз!')
            time.sleep(0.5)
    elif work == 2:
        print('Досвидули!')
        time.sleep(0.5)

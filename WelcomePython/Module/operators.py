# Книга Майк МакГрат Python для начинающих страница 30
# Описание того, о чем модуль
import time
userName = 'Андрей'


print('Сейчас ' + userName + ' ты узнаешь, об операторах присваивания значений.')
time.sleep(1)
print('Необходимо это, в тех случаях, когда нужно переменной присвоить значение или изменить его.')
time.sleep(1)
print('Ты уже знаешь один из операторов присваивания, это знак: = ')
time.sleep(1)
print('Теперь рассмотрим другие:')
time.sleep(1)
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
time.sleep(1)

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
print('\na = ', num1)
print('\nb = ', num2)

time.sleep(1)
print('\nОператор\t' + 'Пример' + '\tРезультат' + '\tЧто произошло\n')
num1 = num2
print("=" + '\t\t\ta = b' + '\t\ta = ', num1, '\t\tПеременной а присвоилось значение переменной b: a = b')
print('Теперь в переменных значения:')
print('a = ', num1)
print('b = ', num2)
time.sleep(3)
num1 += num2
print('+=' + '\t\t\ta += b' + '\t\ta = ', num1, '\t\ta = (a + b)')
print('Теперь в переменных значения:')
print('a = ', num1)
print('b = ', num2)
time.sleep(3)
num1 -= num2
print('-=' + '\t\t\ta -= b' + '\t\ta = ', num1, '\t\t\ta = (a - b)')
print('Теперь в переменных значения:')
print('a = ', num1)
print('b = ', num2)
time.sleep(3)
num1 *= num2
print('*=' + '\t\t\ta *= b' + '\t\ta = ', num1, '\t\ta = (a * b)')
print('Теперь в переменных значения:')
print('a = ', num1)
print('b = ', num2)
time.sleep(3)
num1 /= num2
print('/=' + '\t\t\ta /= b' + '\t\ta = ', num1, '\t\ta = (a / b)')
print('Теперь в переменных значения:')
print('a = ', num1)
print('b = ', num2)
time.sleep(3)
num1 %= num2
print('%=' + '\t\t\ta %= b' + '\t\ta = (a % b)', num1, '\t\ta = (a % b)')
print('Теперь в переменных значения:')
print('a = ', num1)
print('b = ', num2)
time.sleep(3)
print('Если не изменить числа, то далее все действия будут равны 0\nНам ведь это не интересно, давай изменим значение переменой а')
while num1 != int:
    num1 = input('Введи число для переменной а:\n')
    try:
        num1 = int(num1)
        break
    except ValueError:
        print('\n___!!!_Нужно ввести цифру_!!!___\n')
        time.sleep(1)
print('a = ', num1)
print('b = ', num2)
time.sleep(3)
num1 //= num2
print('//=' + '\t\t\ta //= b' + '\t\ta = (a // b)', num1, '\t\ta = (a // b)')
print('Теперь в переменных значения:')
print('a = ', num1)
print('b = ', num2)
time.sleep(3)
num1 **= num2
print('**=' + '\t\t\ta **= b' + '\t\ta = (a ** b)', num1, '\t\ta = (a ** b)')
print('Теперь в переменных значения:')
print('a = ', num1)
print('b = ', num2)
time.sleep(4)

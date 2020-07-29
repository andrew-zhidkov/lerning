# Книга Майк МакГрат Python для начинающих страница 28
# Описание того, о чем модуль


print('В этом модуле разберем математичесткие операторы:\n'
      '+\t' 'Сложение - Addition\n'
      '-\t' 'Вычитание - Substraction\n'
      '*\t' 'Умножение - Multiplication\n'
      '/\t' 'Деление - Division\n'
      '//\t' 'Целочисленное деление - Floor Divison\n'
      '%\t' 'Деление по модулю - Modulus\n'
      '**\t' 'Возведение в степень - Exponent\n')

print('Для того чтобы лучше понять, задумай два числа от 1 до 9.')
answer = 'Y'
while answer == 'Y':

# Запрос информации от пользователя
      num1 = ''
      num2 = ''
      #while num1.isdigit != False:
      num1=int(input('Введи первое число:\n'))

      #while num2.isdigit != True:
      num2=input('Введи второе число:\n')

      # Преобразуем значения переменных в числовой формат

      num1=(int(num1))
      num2=(int(num2))

      # Демонстрация арифметических действий и результата их выполнения

      print('\nВот результаты действий над часлами: ', num1, ' и ', num2)
      print('\nAddition:\t\t' , num1, '+', num2, '=', num1 + num2)
      print('Substraction:\t' , num1, '-', num2, '=', num1 - num2)
      print('Multiplicatin:\t' , num1, '*', num2, '=', num1 * num2)
      print('Division:\t\t', num1, '/', num2, '=', num1 / num2)
      print('Floor Division:\t', num1, '//', num2, '=', num1 // num2)
      print('Modulus:\t\t', num1, '%', num2, '=', num1 % num2)
      print('Exponent:\t\t', num1, '**', num2, "=", num1 ** num2)

      print('\n!!!Важно!!! Деление - Division всегда возвращает часло с плавающей точкой!')
      print('!!!Важно!!! Деление по модулю - Floor Divison возвращает только целое число, отбрасывая остаток!')
      print('!!!Важно!!! Целочисленное деление - Modulus возвращает остаток после деления!')

      answer = input('\nПопробовать еще раз?\n'
                           'Y/N: ')
      answer = str.upper(answer) #возводим ответ в заглавную букву

print('\nУдачного изучения!')

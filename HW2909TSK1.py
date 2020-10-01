def div(*args):
    try:
        x_val = float(input('Введите значение №1: '))
        y_val = float(input('Введите значение №2: '))
        div_value = x_val / y_val

    except ValueError:
        return 'Неверное значение!'
    except ZeroDivisionError:
        return 'Вы ввели нулевое значение!'

    return div_value


'''При выводе результата показывает большое количество знаков после точки
не пойму куда впиать raund, то есть если вписываю в эту часть div_value = div()
то раунд работает после точки 2 знака, но при попытке ввести буквы или 0
все валится с ошибкой'''

div_value = div()
print('Ваш результат:', div_value)

def calculator() -> float:

   """ Калькулятор с 4-мя математическими операциями"""

   print('Калькулятор для души')
   while True:
       try:
            a = input('Введите первое число: ')
            num1 = float(a)
            operator = input('Введите математическую операцию (+, -, *, /): ')
            if operator not in ('+', '-', '*', '/'):
                raise ValueError("Введите оператор из предложенных в списке: +, -, *, /")
            b = input('Введите второе число: ')
            num2 = float(b)

            if operator == '+':
                resultat = num1 + num2
            elif operator == '-':
                resultat = num1 - num2
            elif operator == '*':
                resultat = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError('Делить на ноль нельзя')
                resultat = num1 / num2
            print(f'Результат: {num1} {operator} {num2} = {resultat}\n')

       except ValueError:
           print(f"Ошибка ввода: {ValueError}. Попробуйте еще раз.\n")
       except ZeroDivisionError:
           print(f"Деление на ноль запрещено: {ZeroDivisionError}.\n")
       except Exception:
           print(f"Произошла непредвиденная ошибка: {Exception}.\n")


if __name__ == '__main__':
      calculator()

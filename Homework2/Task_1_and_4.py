
def input_float():
    try:
        number = input("Введите дробное число: ")
        if not number:
            raise Exception("Пустые строки вводить нельзя!!!")
        return float(number)
    except ValueError:
        print("Вы ввели не дробное число, повторите ввод")
        return input_float()

print(input_float())


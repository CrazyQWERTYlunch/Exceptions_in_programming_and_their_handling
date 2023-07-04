import Person
def added_person():
    data = input_data()
    new_person = Person.Person(data[0],data[1],data[2],data[3],data[4],data[5])
    write_file(new_person)

def input_data():
    data = list(input("Введите Фамилию, Имя, Отчество, дату рождения, номер телефона и пол: ").split())
    if len(data) < 6:
        raise Exception("Вы ввели недостаточное количество данных")
    elif len(data) > 6:
        raise Exception("Вы ввели слишком много данных")
    return check_data(data)

def write_file(new_person):
    write_person = open(f"{new_person.surname}.txt","a+")
    try:
        write_person.writelines(new_person.output_all() + "\n")
    finally:
        write_person.close()
def check_data(data):
    data[0] = check_last_name(data[0])
    data[1] = check_name(data[1])
    data[2] = check_patronymic(data[2])
    data[3] = check_date(data[3])
    data[4] = check_phone(data[4])
    check_gender(data[5])
    return data


def check_last_name(last_name):
    if last_name.capitalize().isalpha():
        return last_name.capitalize()
    else:
        if last_name.find("-"):
            last_name_one, last_name_two = last_name[:last_name.find("-")], last_name[last_name.find("-") + 1:]
            if last_name_one.capitalize().isalpha() and last_name_two.capitalize().isalpha():
                return last_name_one.capitalize() + "-" + last_name_two.capitalize()
    raise Exception("Произошла ошибка при вводе Фамилии")

def check_name(name):
    if name.capitalize().isalpha():
        return name.capitalize()
    else:
        raise Exception("Произошла ошибка при вводе Имени")

def check_patronymic(patronymic):
    if patronymic.capitalize().isalpha():
        return patronymic.capitalize()
    else:
        raise Exception("Произошла ошибка при вводе отчества")

def check_date(date):
    if len(date) > 10:
        raise Exception("Ошибка при вводе даты: Слишком много символов")
    elif len(date) < 10:
        raise Exception("Ошибка при вводе даты: Слишком мало символов")

    if date.count(".") != 2:
        raise Exception("Ошибка при вводе даты: Введите дату в формате dd.mm.yyyy")

    date_day, date_month, date_year = date.split(".")
    if 0 < int(date_month) <= 12:
        if 0 < int(date_month) <= 31:
            return date
        else:
            raise Exception("Ошибка при вводе даты: Месяц не может содержать более 31 дня")
    else:
        raise Exception("Ошибка при вводе даты: Указан не верный месяц")


def check_phone(phone_number):
    if phone_number.isdigit():
        return phone_number
    raise Exception("Произошла ошибка при вводе номера!\nНомер может состоять только из цифр!")

def check_gender(sex):
    if sex == 'f' or sex == 'm':
        return sex
    raise Exception("Пол указан не верно")


added_person()
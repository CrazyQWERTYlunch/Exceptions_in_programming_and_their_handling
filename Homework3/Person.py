class Person():
    surname = None
    name = None
    patronymic = None
    date_of_birth = None
    phone_number = None
    sex = None
    def __init__(self, surname, name, patronymic, date_of_birth, phone_number, sex):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.sex = sex

    def output_all(self):
        return f"<{self.surname}><{self.name}><{self.patronymic}><{self.date_of_birth}><{self.phone_number}><{self.sex}>"


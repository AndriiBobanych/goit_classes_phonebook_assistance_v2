from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value: str):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    pass


class Phone(Field):
    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value):
        phone_number = (
            value.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        if phone_number.isdigit() and phone_number.startswith("380") and len(phone_number) == 12:
            self._value = "+" + phone_number
        else:
            self._value = None
            print(f"Entered number '{value}' is not valid. Please use format: '+38-0XX-XXX-XX-XX'")


class Birthday(Field):
    @property
    def value(self) -> datetime.date:
        return self._value

    @value.setter
    def value(self, value):
        try:
            self._value = datetime.strptime(value, "%d-%m-%Y").date()
        except ValueError:
            print(f"Entered {value} is not correct date. Please use format: 'dd-mm-yyyy'")


class Record:

    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.name = name
        self.phone = [phone] if phone is not None else []
        self.birthday = birthday

    def add_to_phone_field(self, phone_number: Phone):
        self.phone.append(phone_number)

    def change_in_phone_field(self, old_number: Phone, new_number: Phone):
        try:
            self.phone.remove(old_number)
            self.phone.append(new_number)
        except ValueError:
            print(f"Contact does not contain such phone number: {old_number}")

    def delete_from_phone_field(self, phone: Phone):
        try:
            self.phone.remove(phone)
        except ValueError:
            print(f"Contact does not contain such phone number: {phone}")

    def days_to_birthday(self):
        current_date = datetime.now()
        if self.birthday is not None:
            birthday: datetime.date = self.birthday.value.date()
            next_birthday = datetime(year=current_date.year, month=birthday.month, day=birthday.day).date()
            if next_birthday < current_date:
                next_birthday = datetime(
                    year=next_birthday.year + 1,
                    month=next_birthday.month,
                    day=next_birthday.day,
                )
            return (next_birthday - current_date).days
        return None


class AddressBook(UserDict):

    def add_new_contact(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        new_contact = Record(name=name, phone=phone, birthday=birthday)
        self.data[name.value] = new_contact

    def __iter__(self):
        self.page = 0
        self._items_per_page = 20
        return self

    def __next__(self):
        records = list(self.data.items())
        start_index = self.page * self._items_per_page
        end_index = (self.page + 1) * self._items_per_page
        self.page += 1
        if len(records) > end_index:
            to_return = records[start_index:end_index]
        else:
            if len(records) > start_index:
                to_return = records[start_index : len(records)]
            else:
                to_return = records[:-1]
        return [{record[1]: record[0]} for record in to_return]


if __name__ == "__main__":
    my_phonebook = AddressBook()


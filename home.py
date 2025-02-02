from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Phone number must be exactly 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))
    
    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]
    
    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = Phone(new_number).value
                return
        raise ValueError("Phone number not found.")
    
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

# Приклад використання
if __name__ == "__main__":
    book = AddressBook()
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print(book)
    
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)
    
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")
    
    book.delete("Jane")
    print(book)

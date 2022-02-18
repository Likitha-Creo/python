"""You are probably familiar with the phone book on your mobile phone. The phone book contains a list of persons. For each person you can record the name, telephone numbers, email address, and perhaps other relevant data. A natural way of representing such personal data in a program is to create a class, say class Person. The data attributes of the class hold information like the name, mobile phone number, office phone number, private phone number, and email address. The constructor may initialize some of the data about a person. Additional data can be specified later by calling methods in the class. One method can print the data. Other methods can register additional telephone numbers and an email address. In addition we initialize some of the data attributes in a constructor method. The attributes that are not initialized when constructing a Person instance can be added later by calling appropriate methods. For example, adding an office number is done by calling add_office_number."""

class Person:
    def __init__(self, name):
        self.name = name
    def add_mobile_phone(self, mobile):
        self.mobile = mobile
    def add_office_phone(self, office):
        self.office = office
    def add_private_phone(self, private):
        self.private = private
    def add_email(self, email):
        self.email = email
    def printing(self):
        print(self.name, self.mobile, self.office, self.private, self.email)

p = Person("likku")
p.add_mobile_phone(123)
p.add_office_phone(456)
p.add_private_phone(789)
p.add_email("likithalikku2821@gmail.com")
p.printing()



        

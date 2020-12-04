class Student():
    def __init__(self, name, surname, age, group, course):
        self.name = name
        self.surname = surname
        self.age = age
        self.group = group
        self.course = course
        
    def set_name(self,value):
        self.name = value
    def set_surname(self,value):
        self.surname = value
    def set_age(self,value):
        self.age = value
        
    def data(self):
        return 'Имя: '+self.name+ '\nФамиля: '+self.surname+ '\nВозраст: ' +str(self.age)+ '\nГруппа: '+self.group+ "\nКурс: " + str(self.course) + "\n"


student1 = Student("Мирас", "Кусаинов", 18, "АиУп-19р/о", 1)
student2 = Student("Нурболат", "Жабасов", 18, "АиУп-19р/о", 1)
student3 = Student("Асем", "Серикова", 18, "АиУп-19р/о", 1)
student4 = Student("Сергей", "Каузов", 18, "АиУп-19р/о", 1)
student5 = Student("Дильназ", "Кубашева", 18, "АиУп-19р/о", 1)
student1.set_name("123")

print(student1.data())
print(student2.data())
print(student3.data())
print(student4.data())
print(student5.data())


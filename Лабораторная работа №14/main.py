
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        """Вывод общей информации о человеке"""
        print(f"Имя: {self.name}, Возраст: {self.age}")



class Student(Person):
    def __init__(self, name, age, group, gpa):
        super().__init__(name, age)  
        self.group = group  
        self.gpa = gpa     

    def display_info(self):
        """Переопределяем метод для вывода информации о студенте"""
        super().display_info()  
        print(f"Группа: {self.group}, Средний балл: {self.gpa}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject  

    def display_info(self):
        """Переопределяем метод для вывода информации о преподавателе"""
        super().display_info()  
        print(f"Предмет: {self.subject}")



class Admin(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position 

    def display_info(self):
        """Переопределяем метод для вывода информации о сотруднике администрации"""
        super().display_info()  
        print(f"Должность: {self.position}")


if __name__ == "__main__":
    student1 = Student("Усербай Альмири", 18, "Группа ИС24-22", 4.5)
    teacher1 = Teacher("Карашаш Жорабековна", 32, "Математика")
    admin1 = Admin("Гульзат Кашимова", 40, "Ректор")

    print("\nИнформация о студенте:")
    student1.display_info()

    print("\nИнформация о преподавателе:")
    teacher1.display_info()

    print("\nИнформация о сотруднике администрации:")
    admin1.display_info()

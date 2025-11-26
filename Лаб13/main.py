class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"


class Student(Person):
    def __init__(self, name: str, age: int, group: str, gpa: float):
        super().__init__(name, age)
        self.group = group
        self.gpa = gpa

    def display_info(self):
        return (f"Студент: {self.name}, Возраст: {self.age}, "
                f"Группа: {self.group}, Средний балл: {self.gpa}")


class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str, experience: int):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience

    def display_info(self):
        return (f"Преподаватель: {self.name}, Возраст: {self.age}, "
                f"Предмет: {self.subject}, Стаж: {self.experience} лет")


class AdminStaff(Person):
    def __init__(self, name: str, age: int, position: str, department: str):
        super().__init__(name, age)
        self.position = position
        self.department = department

    def display_info(self):
        return (f"Административный сотрудник: {self.name}, Возраст: {self.age}, "
                f"Должность: {self.position}, Отдел: {self.department}")


# -------- Демонстрация --------
if __name__ == "__main__":

    persons = [
        Student("Анна", 19, "ИС-21", 4.5),
        Teacher("Иван Петров", 45, "Математика", 20),
        AdminStaff("Светлана Крылова", 38, "Менеджер", "Учебный отдел")
    ]

    print("Демонстрация полиморфизма:\n")
    for person in persons:
        print(person.display_info())

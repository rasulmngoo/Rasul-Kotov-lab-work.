import json

class Student:
    def __init__(self, name, group, gpa):
        self.__name = name  # инкапсуляция
        self.__group = group
        self.set_gpa(gpa)  # использование метода для установки GPA с валидацией

    def __str__(self):
        return f"Студент: {self.__name}, Группа: {self.__group}, GPA: {self.__gpa}"

    def display_info(self):
        """Вывод информации о студенте."""
        print(f"Имя: {self.__name}, Группа: {self.__group}, GPA: {self.__gpa}")

    def get_name(self):
        """Геттер для имени."""
        return self.__name

    def get_group(self):
        """Геттер для группы."""
        return self.__group

    def get_gpa(self):
        """Геттер для GPA."""
        return self.__gpa

    def set_gpa(self, new_gpa):
        """Сеттер для GPA с валидацией."""
        if 0 <= new_gpa <= 5:
            self.__gpa = new_gpa
        else:
            print("Ошибка: GPA должен быть в пределах от 0 до 5.")
            self.__gpa = 0  # присваиваем значение по умолчанию в случае ошибки

    def update_gpa(self, new_gpa):
        """Метод для обновления GPA."""
        self.set_gpa(new_gpa)

class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []  # Список студентов в группе

    def add_student(self, student):
        """Добавление студента в группу."""
        self.students.append(student)

    def remove_student(self, name):
        """Удаление студента по имени."""
        self.students = [student for student in self.students if student.get_name() != name]

    def show_all(self):
        """Вывод всех студентов в группе."""
        if not self.students:
            print("В группе нет студентов.")
        for student in self.students:
            student.display_info()

    def get_top_students(self, threshold):
        """Вывод студентов с GPA выше порога."""
        top_students = [student for student in self.students if student.get_gpa() > threshold]
        if not top_students:
            print("Нет студентов с GPA выше заданного порога.")
        for student in top_students:
            student.display_info()

    def save_to_file(self, filename):
        """Сохранение списка студентов в файл JSON."""
        students_data = [{"name": student.get_name(), "group": student.get_group(), "gpa": student.get_gpa()} for student in self.students]
        with open(filename, 'w') as file:
            json.dump(students_data, file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        """Загрузка списка студентов из файла JSON."""
        try:
            with open(filename, 'r') as file:
                students_data = json.load(file)
                for student_data in students_data:
                    student = Student(student_data["name"], student_data["group"], student_data["gpa"])
                    self.add_student(student)
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
        except json.JSONDecodeError:
            print("Ошибка при чтении файла.")

if __name__ == "__main__":
    # Создание группы
    group = Group("Информатика")

    # Добавление студентов
    student1 = Student("Иванов Иван", "Информатика 1", 4.5)
    student2 = Student("Петров Петр", "Информатика 1", 3.8)
    student3 = Student("Сидоров Сидор", "Информатика 1", 4.9)

    group.add_student(student1)
    group.add_student(student2)
    group.add_student(student3)

    # Вывод всех студентов
    print("Все студенты в группе:")
    group.show_all()

    # Обновление GPA для студента
    student2.update_gpa(4.2)
    print("\nОбновлённые данные по студенту Петрову Петр:")
    student2.display_info()

    # Получение студентов с GPA выше 4.0
    print("\nСтуденты с GPA выше 4.0:")
    group.get_top_students(4.0)

    # Сохранение студентов в файл
    group.save_to_file('students.json')

    # Загрузка студентов из файла
    new_group = Group("Информатика")
    new_group.load_from_file('students.json')
    print("\nСтуденты, загруженные из файла:")
    new_group.show_all()

import json
import csv
import os
import sys

# Настройка UTF-8 для Windows
if os.name == 'nt':
    os.system('chcp 65001')
sys.stdout.reconfigure(encoding='utf-8')

# Список студентов
students = []

# Файлы
TXT_FILE = "students.txt"
JSON_FILE = "students.json"
CSV_FILE = "students.csv"

# Добавление студента
def add_student():
    try:
        name = input("Введите имя студента: ").strip()
        age = int(input("Введите возраст: "))
        gpa = float(input("Введите GPA: "))
        students.append({"name": name, "age": age, "gpa": gpa})
        print("Студент добавлен!")
    except ValueError:
        print("Ошибка: возраст и GPA должны быть числами!")

# Показ студентов по убыванию GPA
def show_students_desc():
    if not students:
        print("Список студентов пуст.")
        return
    sorted_students = sorted(students, key=lambda x: x["gpa"], reverse=True)
    print("\nСписок студентов (GPA от большего к меньшему):")
    for s in sorted_students:
        print(f"{s['name']} | Возраст: {s['age']} | GPA: {s['gpa']}")
    print()

# Показ студентов по возрастанию GPA
def show_students_asc():
    if not students:
        print("Список студентов пуст.")
        return
    sorted_students = sorted(students, key=lambda x: x["gpa"])
    print("\nСписок студентов (GPA от меньшего к большему):")
    for s in sorted_students:
        print(f"{s['name']} | Возраст: {s['age']} | GPA: {s['gpa']}")
    print()

# Сохранение в TXT
def save_txt():
    try:
        with open(TXT_FILE, "w", encoding="utf-8") as f:
            for s in students:
                f.write(f"{s['name']},{s['age']},{s['gpa']}\n")
        print("Сохранено в TXT.")
    except Exception as e:
        print(f"Ошибка при сохранении в TXT: {e}")

# Загрузка из TXT
def load_txt():
    if not os.path.exists(TXT_FILE):
        return
    try:
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            for line in f:
                name, age, gpa = line.strip().split(",")
                students.append({"name": name, "age": int(age), "gpa": float(gpa)})
    except Exception as e:
        print(f"Ошибка при загрузке из TXT: {e}")

# Сохранение в JSON
def save_json():
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(students, f, ensure_ascii=False, indent=4)
        print("Сохранено в JSON.")
    except Exception as e:
        print(f"Ошибка при сохранении в JSON: {e}")

# Загрузка из JSON
def load_json():
    if not os.path.exists(JSON_FILE):
        return
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            loaded = json.load(f)
            students.extend(loaded)
    except Exception as e:
        print(f"Ошибка при загрузке из JSON: {e}")

# Сохранение в CSV
def save_csv():
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "age", "gpa"])
            writer.writeheader()
            writer.writerows(students)
        print("Сохранено в CSV.")
    except Exception as e:
        print(f"Ошибка при сохранении в CSV: {e}")

# Загрузка из CSV
def load_csv():
    if not os.path.exists(CSV_FILE):
        return
    try:
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append({"name": row["name"], "age": int(row["age"]), "gpa": float(row["gpa"])})
    except Exception as e:
        print(f"Ошибка при загрузке из CSV: {e}")

# Меню
def menu():
    load_txt()
    load_json()
    load_csv()
    
    while True:
        print("\nМеню:")
        print("1. Добавить студента")
        print("2. Показать студентов (по убыванию GPA)")
        print("3. Сохранить студентов")
        print("4. Показать студентов (по возрастанию GPA)")
        print("5. Выйти")
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students_desc()
        elif choice == "3":
            save_txt()
            save_json()
            save_csv()
        elif choice == "4":
            show_students_asc()
        elif choice == "5":
            print("Выход...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu()
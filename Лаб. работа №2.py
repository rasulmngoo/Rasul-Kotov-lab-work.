a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
op = input("Введите операцию (==, !=, >, <, >=, <=, and, or): ")

if op == "==":
    print("Результат:", a == b)
elif op == "!=":
    print("Результат:", a != b)
elif op == ">":
    print("Результат:", a > b)
elif op == "<":
    print("Результат:", a < b)
elif op == ">=":
    print("Результат:", a >= b)
elif op == "<=":
    print("Результат:", a <= b)
elif op == "and":
    print("Результат:", bool(a) and bool(b))
elif op == "or":
    print("Результат:", bool(a) or bool(b))
else:
    print("Неизвестная операция")

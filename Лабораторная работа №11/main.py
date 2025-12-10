import logging

# Настройка логирования
logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_final_amount(P, r, n, t):
    """Функция для расчета итоговой суммы по формуле сложных процентов."""
    try:
        A = P * (1 + r / n) ** (n * t)
        return A
    except Exception as e:
        logging.error(f"Ошибка расчёта: {e}")
        raise

def get_input():
    """Функция для получения и проверки ввода от пользователя."""
    while True:
        try:
            P = float(input("Введите сумму вклада (P): "))
            if P <= 0:
                raise ValueError("Сумма вклада должна быть положительным числом.")
            r = float(input("Введите годовую процентную ставку (в процентах): ")) / 100
            if r < 0:
                raise ValueError("Процентная ставка не может быть отрицательной.")
            t = float(input("Введите срок вклада в годах (t): "))
            if t <= 0:
                raise ValueError("Срок вклада должен быть положительным числом.")
            return P, r, t
        except ValueError as ve:
            logging.error(f"Ошибка ввода данных: {ve}")
            print(f"Ошибка: {ve}. Пожалуйста, попробуйте снова.")
        except Exception as e:
            logging.error(f"Неизвестная ошибка: {e}")
            print("Произошла ошибка. Пожалуйста, попробуйте снова.")

def save_result(final_amount):
    """Функция для сохранения результата в файл result.txt."""
    try:
        with open("result.txt", "w") as file:
            file.write(f"Итоговая сумма вклада: {final_amount:.2f} руб.\n")
        print(f"Результат успешно записан в файл 'result.txt'.")
    except Exception as e:
        logging.error(f"Ошибка записи в файл: {e}")
        print("Произошла ошибка при записи в файл.")

def main():
    print("Добро пожаловать в Финансовый калькулятор!")
    P, r, t = get_input()
    n = 12  # количество начислений в год
    try:
        final_amount = calculate_final_amount(P, r, n, t)
        print(f"Итоговая сумма вклада: {final_amount:.2f} руб.")
        save_result(final_amount)
    except Exception as e:
        logging.error(f"Ошибка выполнения программы: {e}")
        print("Произошла ошибка при расчете итоговой суммы.")

if __name__ == "__main__":
    main()
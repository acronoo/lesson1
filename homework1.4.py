# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
user_digit = int(input("Введите любое число: "))
r = -1  # Задаём переменную, в которой будет хранится значение самого большого числа
while user_digit > 0.1:
    d = user_digit % 10  # В переменную d записываем значение последней цифры
    user_digit = user_digit // 10  # Целочисленно делим на 10, тем самым убирая последнюю цифру
    if d > r:
        r = d
print(f"Самое большое число: {r}")
# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

digit = input("Введите любое число: ")
print(
    f"{digit} + {digit + digit} + {digit + digit + digit} = {int(digit) + int(digit + digit) + int(digit + digit + digit)}")

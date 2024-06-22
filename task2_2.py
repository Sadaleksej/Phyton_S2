from fractions import Fraction

str1 = input("Введите первую дробь в формате a/b: ")
numbers1 = str1.split("/")
if len(numbers1) == 2:
    a1 = int(numbers1[0])
    b1 = int(numbers1[1])
    print("Число a:", a1)
    print("Число b:", b1)
    print(a1 / b1)
else:
    print("Неверный формат ввода. Пожалуйста, введите строку в формате a/b.")

str2 = input("Введите вторую дробь в формате a/b: ")
numbers2 = str2.split("/")
if len(numbers2) == 2:
    a2 = int(numbers2[0])
    b2 = int(numbers2[1])
    print("Число a:", a2)
    print("Число b:", b2)
else:
    print("Неверный формат ввода. Пожалуйста, введите строку в формате a/b.")

sum1 = (a1 * b2 + a2 * b1) / (b1 * b2)
mul1 = (a1 * a2) / (b1 * b2)

sum2 = Fraction(a1, b1) + Fraction(a2, b2)
mul2 = Fraction(a1, b1) * Fraction(a2, b2)

print(f"Сумма дробей: {sum1}")
print(f"Сумма дробей: {sum1}")
print(f"Произведение дробей: {mul1}")
print(f"Произведение дробей: {mul2}")

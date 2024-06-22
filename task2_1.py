

def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


a = int(input("Введите целое число: "))

res1 = convert_to(a, 16, True)
res2 = hex(a)

print(f"Шестнадцатиричное число: {res1}")
print(f"Шестнадцатиричное число: {res2}")


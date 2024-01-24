sqrt_and_perimeter = lambda a, b: (a**0.5 + b**0.5) * 2
compare_strings = lambda str1, str2: len(str1) == len(str2)
format_name = lambda first_name, last_name: f"{last_name}, {first_name}"
is_even = lambda num: num % 2 == 0


result1 = sqrt_and_perimeter(3, 4)
result2 = compare_strings("Привіт", "Світ")
result3 = format_name("Єгор", "Євтушенко")
result4 = is_even(10)


print(f"Периметр прямокутника: {result1}")
print(f"Порівняння строк: {result2}")
print(f"Форматоване ім'я та прізвище: {result3}")
print(f"Число парне: {result4}")

def filter_by_condition(condition_func, numbers):
    filtered_numbers = [num for num in numbers if condition_func(num)]
    return filtered_numbers


def is_even(number):
    return number % 2 == 0


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter_by_condition(is_even, numbers_list)

print("Початковий список чисел:", numbers_list)
print("Відфільтрований список за умовою парності:", filtered_numbers)

def multiply(list1, list2):
    result = [x * y for x, y in zip(list1, list2)]
    return result


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
result_multiply_lists = multiply(list1, list2)
print("Добуток пар чисел з двох списків:", result_multiply_lists)


def concatenate(str1, str2):
    result = ''.join([a + b for a, b in zip(str1, str2)])
    return result


str1 = "abc"
str2 = "abf"
result_concatenate_strings = concatenate(str1, str2)
print("З'єднання відповідних символів двох рядків:", result_concatenate_strings)


def compare(list1, list2):
    different_indices = [i for i, (a, b) in enumerate(zip(list1, list2)) if a != b]
    return different_indices


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
result_compare_lists = compare(list1, list2)
print("Індекси, де елементи відрізняються:", result_compare_lists)


def sum_columns(matrix):
    result = [sum(column) for column in zip(*matrix)]
    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


result_sum_columns = sum_columns(matrix)
print("Сума елементів кожного стовпця в матриці:", result_sum_columns)

def filter_words_starting_with_letter(words, letter):
    return list(filter(lambda word: word.startswith(letter), words))


def filter_negative_numbers(numbers):
    return list(filter(lambda num: num < 0, numbers))


def filter_strings_containing_word(strings, target_word):
    return list(filter(lambda string: target_word in string, strings))


words_list = input("Введіть слова через пробіл: ").split()
start_letter = input("Введіть літеру для фільтрації слів: ")

numbers_list = list(map(int, input("Введіть числа через пробіл: ").split()))

strings_list = input("Введіть рядки через пробіл: ").split()
target_word = input("Введіть слово для фільтрації рядків: ")

filtered_words = filter_words_starting_with_letter(words_list, start_letter)
filtered_numbers = filter_negative_numbers(numbers_list)
filtered_strings = filter_strings_containing_word(strings_list, target_word)

print("Слова, що починаються на літеру {}: {}".format(start_letter, filtered_words))
print("Від'ємні числа: {}".format(filtered_numbers))
print("Рядки, що містять слово {}: {}".format(target_word, filtered_strings))

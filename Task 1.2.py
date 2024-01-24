def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def reverse_word(word):
    return word[::-1]


celsius_temperatures = list(map(float, input("Введіть температури у градусах Цельсія через пробіл: ").split()))
words_list = input("Введіть слова через пробіл: ").split()

fahrenheit_temperatures = list(map(celsius_to_fahrenheit, celsius_temperatures))
reversed_words = list(map(reverse_word, words_list))

print("Температури в градусах Фаренгейта:", fahrenheit_temperatures)
print("Слова в зворотньому порядку:", reversed_words)

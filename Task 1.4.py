from functools import reduce


def lcm(x, y):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return abs(x * y) // gcd(x, y)


def sum_of_squares(x, y):
    return x + y ** 2


num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

numlist = list(map(int, input("Введіть числа через пробіл: ").split()))

result = reduce(lcm, [num1, num2])
sum_of_squares_result = reduce(sum_of_squares, numlist)


print("Найменший спільний кратник {}: {}".format([num1, num2], result))
print("Сума квадратів чисел {}: {}".format(numlist, sum_of_squares_result))
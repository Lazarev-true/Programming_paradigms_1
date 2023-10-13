# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imporative(numbers):
    N = len(numbers)
    for i in range(N-1):
        for j in range(N-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

numbers = [int(x) for x in input('Введите список целых чисел через пробел: ').split()]

print(sort_list_imporative(numbers))

# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    num = sorted(numbers, reverse=True)
    return num

numbers = [int(x) for x in input('Введите список целых чисел через пробел: ').split()]

print(sort_list_declarative(numbers))

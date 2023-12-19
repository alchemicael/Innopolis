def selection_sort(array):
    for i in range(len(array)):
        minimal = array[i]
        index = i
        for j in range(i + 1, len(array)):
            if array[j] < minimal:
                minimal = array[j]
                index = j
        temporary = array[i]
        array[i] = array[index]
        array[index] = temporary
    return array


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temporary = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temporary
    return array


def insertion_sort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i] <= array[j]:
                array.insert(0, array[i])
                array.pop(i + 1)
            elif array[j] <= array[i] <= array[j + 1]:
                array.insert(j + 1, array[i])
                array.pop(i + 1)
    return array


def correct_result(array):
    return array == [-1004, -113, 0, 1, 2, 8, 8, 11, 13, 14, 20, 34, 54, 67, 73, 78, 99, 101, 789, 909]


numbers = [11, 8, 34, 789, 101, 54, 13, 0, 2, 78, 99, -1004, 73, 20, 1, 67, 8, 909, -113, 14]

sorted_numbers = insertion_sort(numbers)
print('Insertion sort Test:', correct_result(sorted_numbers))
sorted_numbers = selection_sort(numbers)
print('Selection sort Test:', correct_result(sorted_numbers))
sorted_numbers = bubble_sort(numbers)
print('Bubble sort Test:', correct_result(sorted_numbers))

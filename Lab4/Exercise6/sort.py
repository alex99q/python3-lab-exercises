def bubble_sort(array):
    array_length = len(array) - 1

    for i in range(0, array_length):
        for j in range(0, array_length - i):
            if int(array[j]) > int(array[j + 1]):
                swap(array, j, j + 1)


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]
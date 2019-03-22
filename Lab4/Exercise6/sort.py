def bubble_sort(array):
    array_length = len(array) - 1

    for i in range(0, array_length):
        for j in range(0, array_length - i):
            if int(array[j]) > int(array[j + 1]):
                swap(array, j, j + 1)


def quick_sort(array):
    p_start = 1
    p_end = len(array) - 1

    pivot = array[0]
    partition(array, p_start, p_end)

    while p_start < p_end:
        pivot_index = array.index(pivot)

        partition(array, p_start, pivot_index - 1)
        partition(array, pivot_index + 1, p_end)

    return array


def partition(array, p_start, p_end):
    pivot = array[0]

    while True:

        if array[p_start] > pivot and array[p_end] < pivot:
            swap(array, p_start, p_end)

        if p_start + 1 == p_end:
            break

        p_start += 1
        p_end -= 1

    if array[p_end] < pivot:
        swap(array, array.index(pivot), p_end)
    elif array[p_start] < pivot:
        swap(array, array.index(pivot), p_start)
    elif array[p_start - 1] < pivot:
        swap(array, array.index(pivot), p_start - 1)

    return array.index(pivot)


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]
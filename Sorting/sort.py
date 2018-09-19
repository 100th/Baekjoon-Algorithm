# 퀵 정렬
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        greater = []
        lesser = []

        for element in range(1, len(array)):
            if len(array[element]) < len(pivot):
                lesser.append(array[element])
            else:
                greater.append(array[element])

        return quicksort(lesser) + [pivot] + quicksort(greater)

# 선택 정렬
def selection_sort(a):
    for i in range(len(a)-1):
        min_index = i
        for j in range(i+1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


# 버블 정렬
def swap(x,i,j):
    x[i], x[j] = x[j], x[i]

def bubble_sort(a):
    for size in reversed(range(len(a))):
        for i in range(size):
            if a[i]>a[i+1]:
                swap(a, i, i+1)
    return a


# 삽입 정렬
def insert_sort(a):
    for i in range(1, len(a)):
        j = i-1
        key = a[i]
        while a[j] > key and j >= 0:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a


# 병합 정렬
def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left,right)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right)>0:
        if len(left) > 0 and len(right) > 0:

            if left[0] <= right[0]:
                result.append(left[0])
                left=left[1:]
            else:
                result.append(right[0])
                right = right[1:]

        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

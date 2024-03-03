def merge_sort(arr: list):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def bubble_sort(arr: list):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


array_to_sort1 = [64, 34, 25, 12, 22, 11, 90]
array_to_sort2 = [64, 34, 25, 12, 22, 11, 90]
merge_sort(array_to_sort1)
bubble_sort(array_to_sort2)
print("Merge Sorted Array:", array_to_sort1)
print("Bubble Sorted Array:", array_to_sort2)

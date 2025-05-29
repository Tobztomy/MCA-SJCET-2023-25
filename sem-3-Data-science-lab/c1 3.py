print("SJC23MCA-2059 : TOBIN K TOMY")
print("Batch : MCA 2023-25")
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
           if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
elements = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", elements)
bubble_sort(elements)
print("Sorted List:", elements)
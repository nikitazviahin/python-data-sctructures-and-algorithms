import random
from time_it import time_it

@time_it
def shell_sort(arr):
    
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

        

if __name__ == "__main__":
    arr = [random.randrange(1,100) for element in range(1000000)]
    shell_sort(arr)
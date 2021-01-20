def swap(a, b, arr):
    if a!=b:
        arr[a], arr[b] = arr[b], arr[a]

def partition_hoare(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    start = pivot_index + 1
    end = len(elements) - 1

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    
    return end

def partition_lomuto(elements, start, end):
    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, p_index, elements)
            p_index += 1

    swap(p_index, end, elements)
    
    return p_index
    

def quick_sort_hoare(elements, start, end):
    if start < end:
        pi = partition_hoare(elements, start, end)
        quick_sort_hoare(elements, start, pi - 1)
        quick_sort_hoare(elements, pi+1, end)

def quick_sort_lomuto(elements, start, end):
    if len(elements) == 1:
        return
    if start < end:
        pi = partition_lomuto(elements, start, end)
        quick_sort_lomuto(elements, start, pi - 1)
        quick_sort_lomuto(elements, pi + 1, end)

if __name__ == '__main__':
    elements = [11,0,29,7,2,15,28]
    #quick_sort_hoare(elements, 0, len(elements) - 1)
    quick_sort_lomuto(elements, 0, len(elements) - 1)
    print(elements)
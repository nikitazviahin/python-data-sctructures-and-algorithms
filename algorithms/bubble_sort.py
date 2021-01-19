from time_it import time_it
import random
 
@time_it
def bubble_sort(elements, key=None):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j][key] > elements [j + 1][key]:
                tmp = elements[j][key]
                elements[j][key] = elements[j + 1][key]
                elements[j + 1][key] = tmp
                swapped = True
        if not swapped:
            break
        


if __name__=='__main__':
    #elements = [1,321,3,4,5,61,4122,144,4142,2,4122,421]
    #i = 1000
    # while i >= 500:
    #     elements.append(i)
    #     i -= 1
    # i = 0
    # for i in range(500):
    #     elements.append(i)
    #     i += 1
    elements = [
        { 'name': 'kathy',  'transaction_amount': 20000,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 123,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 4444,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 10, 'device': 'iphone-10'},
    ]

    bubble_sort(elements, 'transaction_amount')
    for element in elements:
        print(element)
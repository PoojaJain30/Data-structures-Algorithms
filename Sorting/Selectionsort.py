#implement selection sort
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def selection_sort(num):
    for i in range(len(num)):
        small = i
        temp = num[i]
        for j in range(i+1,len(num)):
            if num[j] < num[small]:
                small = j       
        num[i] = num[small]
        num[small] = temp  
    print(num)

selection_sort(numbers)
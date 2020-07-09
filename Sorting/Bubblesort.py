#implement Bubble sort
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 290]

def bubble_sort(num):
    for i in range(len(num)):
        for j in range(len(num)):
            if num[i] < num[j]:
                temp = num[i]
                num[i] = num[j]
                num[j] = temp
    print(num)
    
    
    
def bubble_sort1(num): 
    count = 0 
    while(count < len(num)):
        for i in range(len(num)-1):
            if num[i] > num[i+1]:
                temp = num[i]
                num[i] = num[i+1]
                num[i+1] = temp
        count += 1
    print(num)
    
bubble_sort1(numbers)
bubble_sort(numbers)
        
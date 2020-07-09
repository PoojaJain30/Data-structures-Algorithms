#implement insertion sort
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertion_sort(num):
    for i in range(1,len(num)):
        j = 0 
        pick = num[i]
        while(j <= i-1):
            if pick < num[j]:
                num.pop(i)
                num.insert(j,pick)
                break
            
            j += 1
    print(num)

insertion_sort(numbers)
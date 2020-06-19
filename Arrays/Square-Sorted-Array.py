#Squares of a Sorted Array Solution
#Given input sorted array , may conatin -ive values . Output should be sorted and have square of wach val.


#BIG O  is O(n^2)
def sorted_squares(ar):
    new_ar = list(map(lambda x: x**2,ar))
    j = 0
    count = 1
    while(count >= 1):
        count = 0
        for i in range(0,len(new_ar)):
            if (i < len(new_ar)-1):
                if (new_ar[i] > new_ar[i+1]):
                    j = new_ar[i]
                    new_ar[i] = new_ar[i+1]
                    new_ar[i+1] = j
                    count +=1
    return new_ar 

# Efficient solution Big O will be O(nlogn)
def sorted_squares1(ar):
    return sorted(x*x for x in ar)

print(sorted_squares1([-4,-1,0,3,10]))
                    
print(sorted_squares([-4,-1,0,3,10]))

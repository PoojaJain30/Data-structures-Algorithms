# Find Max Consecutive Ones in the input 
# Input will contain only 1's and 0's


# BIG O = O(n^2) Quadratic time
def find_max_consecutive_ones(arr):
    length = 0
    for i,v in enumerate(arr):
        #print(i,v)
        if v == 1:
            count = 0
            while(i < len(arr) and arr[i] == 1):
                count += 1
                i+=1
            if length < count:
                length = count
    return length


#More efficient solution as BIG O = O(n) Linear time
def find_max_consecutive_ones1(arr):
    length = len(arr)
    count = 0
    res = 0
    for i in range(0,length):
        if arr[i] == 0:
            count = 0
        else:
            count += 1
            res = max(count,res)
    return res

find_max_consecutive_ones1([1,1,1,1,1,0,1,1])
find_max_consecutive_ones([1,1,1,1,1,0,1,1])
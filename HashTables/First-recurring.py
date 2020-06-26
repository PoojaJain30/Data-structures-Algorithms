# Function should return first recurring char

#Given an array = [2,5,1,2,3,5,1,2,4]:should return 2
#Given an array = [2,1,1,2,3,5,1,2,4]:should return 1
#Given an array = [2,3,4,5]:should return None
#Bonus... What if we had this:[2,5,5,2,3,5,1,2,4]:return 5 because the pairs are before 2,2

#Big 0 O(n)
array1 = [2,3,4,5]
array = [2,5,5,2,3,5,1,2,4]

#using lists O(n^2) time complexity
def first_recurring_char1(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            arr[i] == arr[j]
            return arr[i]
    return None 


# using hash table incrase in time complexity but need more space
def first_recurring_char(arr):
    table = {}
    for i in range(0,len(arr)):
        if arr[i] not in table:
            table[arr[i]] = i
        else: 
            return arr[i]
    return None 


print(first_recurring_char(array1)) 
print(first_recurring_char(array)) 
print(first_recurring_char1(array1)) 
print(first_recurring_char1(array)) 
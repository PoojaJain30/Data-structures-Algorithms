#Big O in both cases = O(n)
#Iteration Method
def fact(num):
    facto = num
    while (num > 1):
        facto = facto * (num-1)
        num -= 1
    return facto
    
print(fact(5))

#Recursive Method
def factr(num):
    if num == 2:
        return 2
    return num * factr(num-1)

print(factr(5))
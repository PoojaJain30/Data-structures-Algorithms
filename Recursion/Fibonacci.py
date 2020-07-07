# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

#For example: fibonacciRecursive(6) should return 8


#Iterative Method - Big O - O(n)
def fibo(num):
    array = [0,1]
    for i in range(1,num):
        array.append(array[i]+array[i-1])
    print(array)
    return array[num]
    
fibo(11)


#Recursive Method - Big O - O(2^n) {Exponential}

def fibore(num):
    if num < 2:
        return num
    return fibore(num-1)+fibore(num-2)
fibore(11)
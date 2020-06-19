# Remove all the occurance of given value from the input array and return the new length 

def remove_ele(nums, val):
    while True:
        try:
            nums.remove(val)
        except:
            break
    #print(nums)
    return len(nums)

lis = [0,1,2,1,3,0,4,2]

remove_ele(lis,2)
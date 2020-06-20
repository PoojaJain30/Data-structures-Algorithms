
# Return the count of values that have even number of digits 
def find_num_of_even_digits(nums):
    count = 0
    for x in nums:
        if len(str(x)) % 2 == 0:
            count += 1
    return count

print(find_num_of_even_digits([12,345,2,6,7869]))
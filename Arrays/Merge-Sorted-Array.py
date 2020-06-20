# Merge two sorted arrays 

#using inbuild list methods
def merge_sorted_arrays(arr1,arr2):
    sorted_array = (arr1+arr2)
    sorted_array.sort()
    return sorted_array


# using traditional method BigO = O(a+b)
def merge_sorted_arrays1(arr1,arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1+arr2
    merge_arr = []
    i = 0
    j = 0
    while(i < len(arr1) and  j <len(arr2)):
        if arr1[i] <= arr2[j]:
            merge_arr.append(arr1[i])
            i +=1
        elif arr2[j] < arr1[i]:
            merge_arr.append(arr2[j])
            j+=1
    return merge_arr+arr1[i:]+arr2[j:]
        

print(merge_sorted_arrays1([0,3,4,31], [1,3,6,13,30,31,78]))
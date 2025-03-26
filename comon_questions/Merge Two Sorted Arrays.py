'''def merge_sorted_arrays(arr1: list, arr2: list):
    result =[]
    result = arr1 + arr2
    result.sort()
    return result

print(merge_sorted_arrays([2,4,6], [1,3,5]))'''


def merge_sorted_arrays(arr1: list, arr2: list):
    result =[]
    i, j = 0 , 0 

    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1
        else:
            result.append(arr1[i])
            i += 1
    #The extend() method is used to append these remaining elements to the result.
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
            
    
print(merge_sorted_arrays([2,4,6], [1,3,5]))
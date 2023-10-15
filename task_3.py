def biggest(arr):
    max_of = arr[0]
    for ele in arr:
        if ele > max_of:
           max_of = ele
    return max


list1 = [1, 4, 5, 2, 6, 3]
result = biggest(list1)
print(result)
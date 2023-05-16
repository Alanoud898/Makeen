"""def equal_sum_partition(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    target_sum = total_sum // 2
    current_sum = 0
    subset = []
    for num in arr:
        current_sum += num
        subset.append(num)
    if current_sum == target_sum:
        return True

    return False
arr = input("Enter array element: ").split(',')
arr = [int(num) for num in arr]
result = equal_sum_partition(arr)
if result:
    print("True")
    print("it is equal")
else:
    print("False")
    print("it is not equal")"""



def split_array_equal_sum(arr):
    total_sum = sum(arr)  
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == total_sum - current_sum:
            return True
    return False
arr = [2, 6, 1, 9]
result = split_array_equal_sum(arr)
print(result)




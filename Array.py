def rotate_array_left(arr, rotations):
    rotations = rotations % len(arr)  
    arr = arr[rotations:] + arr[:rotations]  
    return arr

array = [1, 2, 3, 4, 5]
rotations = int(input("Enter the number of rotations: "))
rotated_array = rotate_array_left(array, rotations)
print("Rotated array:", rotated_array)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def get_number_list():
    nums = input("Enter a list of numbers, separated by spaces: ").split()
    nums = [int(num) for num in nums]
    return nums


def continue_program():
    choice = input("continue? (y/n): ")
    return choice.lower() == 'y'


while True:
    nums = get_number_list()

    
    print("Choose a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. QuickSort")
    algorithm = input("Enter the number corresponding to your choice: ")

 
    if algorithm == "1":
        bubble_sort(nums)
        algorithm_name = "Bubble Sort"
    elif algorithm == "2":
        selection_sort(nums)
        algorithm_name = "Selection Sort"
    elif algorithm == "3":
        numbers = quick_sort(nums)
        algorithm_name = "QuickSort"
    else:
        print("Invalid choice. Please try again.")
        continue

  
    print(f"\nSorted list using {algorithm_name}: {nums}")

  
    if not continue_program():
        break

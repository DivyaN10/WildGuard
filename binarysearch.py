def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half
            
    return -1  # Target not found

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search_iterative(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

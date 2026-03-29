import random

def randomized_partition(arr, low, high):
    """
    Selects a random pivot from the subarray, swaps it with the last element,
    and then performs the standard Lomuto partition.
    """
    # Choose a random index between low and high (inclusive)
    rand_index = random.randint(low, high)
    
    # Swap the randomly chosen pivot with the last element
    arr[rand_index], arr[high] = arr[high], arr[rand_index]
    
    # Standard Lomuto partition logic
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Swap the pivot into its correct final position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1

def quicksort_randomized(arr, low, high):
    """
    Main function for randomized Quicksort.
    """
    if low < high:
        # Get the partitioning index using the randomized approach
        pi = randomized_partition(arr, low, high)

        # Recursively sort the subarrays on the left and right
        quicksort_randomized(arr, low, pi - 1)
        quicksort_randomized(arr, pi + 1, high)

# --- Test Block ---
if __name__ == "__main__":
    # 1. Create a test array
    test_array = [10, 7, 8, 9, 1, 5, 2, 15, 3]
    print(f"Original Array: {test_array}")
    
    # 2. Call the function (it sorts the array in-place)
    quicksort_randomized(test_array, 0, len(test_array) - 1)
    
    # 3. Print the sorted array
    print(f"Randomized Sort: {test_array}")
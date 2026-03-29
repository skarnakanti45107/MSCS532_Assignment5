import random

# ==========================================
# 1. Deterministic Quicksort
# ==========================================

def partition(arr, low, high):
    """
    Standard Lomuto partition scheme.
    Selects the last element as the pivot and places it in its correct sorted position.
    """
    pivot = arr[high]  # Choosing the last element as the deterministic pivot
    i = low - 1        # Pointer for the greater element

    # Traverse through all elements and compare each with the pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            # If element is smaller than pivot, swap it with the greater element pointed by i
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the greater element specified by i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the position from where partition is done
    return i + 1

def quicksort_deterministic(arr, low, high):
    """
    Main function that implements deterministic Quicksort.
    """
    if low < high:
        # Find pivot element such that elements smaller than pivot are on the left
        # and elements greater than pivot are on the right
        pi = partition(arr, low, high)

        # Recursively sort the subarrays on the left and right of the pivot
        quicksort_deterministic(arr, low, pi - 1)
        quicksort_deterministic(arr, pi + 1, high)


# ==========================================
# 2. Randomized Quicksort
# ==========================================

def randomized_partition(arr, low, high):
    """
    Randomized partition scheme.
    Selects a random pivot, swaps it with the last element, and then calls standard partition.
    """
    # Choose a random index between low and high (inclusive)
    rand_pivot_index = random.randint(low, high)
    
    # Swap the randomly chosen pivot with the last element
    arr[rand_pivot_index], arr[high] = arr[high], arr[rand_pivot_index]
    
    # Now use the standard deterministic partition logic
    return partition(arr, low, high)

def quicksort_randomized(arr, low, high):
    """
    Main function that implements randomized Quicksort.
    """
    if low < high:
        # Get the partitioning index using the randomized approach
        pi = randomized_partition(arr, low, high)

        # Recursively sort the subarrays
        quicksort_randomized(arr, low, pi - 1)
        quicksort_randomized(arr, pi + 1, high)


# ==========================================
# 3. Helper Functions for Testing
# ==========================================

def run_sort(arr, use_randomized=False):
    """
    Helper function to wrap the sorting calls and return a newly sorted array,
    leaving the original array intact for testing purposes.
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    if n > 0:
        if use_randomized:
            quicksort_randomized(arr_copy, 0, n - 1)
        else:
            quicksort_deterministic(arr_copy, 0, n - 1)
    return arr_copy

# --- Quick Test Block ---
if __name__ == "__main__":
    test_data = [10, 7, 8, 9, 1, 5, 2, 15, 3]
    print(f"Original Array: {test_data}")
    print(f"Deterministic Sort: {run_sort(test_data, use_randomized=False)}")
    print(f"Randomized Sort:    {run_sort(test_data, use_randomized=True)}")
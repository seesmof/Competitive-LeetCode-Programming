# This is the bubbleSort function that takes a list as its argument
def bubbleSort(arr):
    # Determine the length of the array and store it in the variable 'n'
    n = len(arr)

    # Loop through the array. 'i' works as a counter for the number of passes required for the bubble sort algorithm
    for i in range(n):
        # Loop through the array from the start to 'n-i-1'.
        # As the largest number(if any) is already at the end after the first pass, we reduce the range by 'i' with each pass
        for j in range(0, n - i - 1):
            # Check if the current element is larger than the next one
            if arr[j] > arr[j + 1]:
                # If the current element is larger than the next one,
                # swap their positions to sort the elements in ascending order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Return the sorted array
    return arr

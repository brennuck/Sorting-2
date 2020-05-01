# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): # starts at 0 and ends at the length of the array-1
        smallest_index = i # 0
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)): # starts at 1 ends at the length of the array
            if arr[smallest_index] > arr[j]: # If the starting spot is greater than one of the elements in j
                smallest_index = j # switch the smallest_index to the new smallest element
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)): # prints a [] with the length of the array
        for j in range(0, len(arr) - i - 1): # prints a [] that starts with a 0, goes thru the length of the array - i - 1
            if arr[j] > arr[j+1]: # if the element found is greater
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
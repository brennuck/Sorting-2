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

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
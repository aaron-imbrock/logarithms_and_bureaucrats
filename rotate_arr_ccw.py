#Rotating an array counter clockwise around a given index
# Something is wrong. I think there's an off-by-1 error in rev_sub_arr() which in turn affects rotate_array().
# Adapted from readings of https://dotkay.github.io/2018/04/08/rotate-array-ccw/

def rev_array_in_place(arr, n):
    i = 0
    while (i < (n/2)):
        arr[i], arr[n - i - 1] = arr[n - i -1], arr[i]
        i = i + 1
    return arr

def rev_sub_arr(arr, start, end):
    mid = start + ((end - start)/2)
    i = start
    while (i <= mid):
        print(f"i is {i}, start is {start}")
        arr[i], arr[end - (i - start)] = arr[end - (i - start)], arr[start]
        i = i + 1
    return arr

def rotate_array(arr, size, pivot):
    rrev_sub_arr(arr, 0, pivot)
    rev_sub_arr(arr, pivot+1, size-1)
    rev_sub_arr(arr, 0, size-1)
    return arr

#array = [1,2,3,4,5,6,7,8]
#In [59]: rotate_array(array, 8, 3)
#Out[59]: [5, 4, 5, 4, 5, 5, 5, 8]

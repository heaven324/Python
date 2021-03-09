'''
1. lower_bound

2. upper_bound

3. sum_list
'''


def lower_bound(arr, target):
    start_ind, end_ind = 0, len(arr)
    while start_ind != end_ind:
        mid_ind = int((start_ind + end_ind) / 2)
        if arr[mid_ind] < target: start_ind = mid_ind + 1
        else: end_ind = mid_ind
    return arr[start_ind] # return value
    # return start_ind      # return index

     
def upper_bound(arr, target):
    start_ind, end_ind = 0, len(arr)
    while start_ind != end_ind:
        mid_ind = int((start_ind + end_ind) / 2)
        if arr[mid_ind] <= target: start_ind = mid_ind + 1
        else: end_ind = mid_ind
    return arr[start_ind] # return value
    # return start_ind      # return index


def sum_list(lst, res = 0):
    for i in lst:
        if type(i) == list:
            res += sum_list(i)
        else:
            res += i
    return res



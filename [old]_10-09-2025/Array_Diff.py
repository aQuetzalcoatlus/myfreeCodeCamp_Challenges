""" 
Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.

The returned array should be sorted in alphabetical order.

"""

def array_diff(arr1, arr2):

    set1: set = set(arr1)
    set2: set = set(arr2)
    
    symm_diff: set = set1 ^ set2

    req_arr: list = list(symm_diff)
    req_arr.sort()

    return req_arr
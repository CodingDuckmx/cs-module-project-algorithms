'''
Input: a List of integers
Returns: a List of integers
'''
# import numpy as np
# def product_of_all_other_numbers(arr):
#     # Your code here

#     # Plan

#     # Pop the first element, multiply the others, append the popped number.
#     # Append the result to a new list.
#     # Do this len(arr) times.

#     lst = []

#     for _ in range(0,len(arr)):
#         popped = arr.pop(0)
#         lst.append(np.prod(arr))
#         arr.append(popped)

#     return lst


#### Improved version ###

def product_of_all_other_numbers(arr):

    lst = []

    # all numbers get multiply by the previous numbers
    p = 1   
    for i in range(len(arr)):

        lst.append(p)

        p = p * arr[i]

    # all numbers get multiply by the following numbers

    p = 1
    for i in range(len(arr)-1, -1,-1):

        lst[i] = lst[i] * p
        p = p * arr[i]

    return lst



if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

import collections

# def sliding_window_max(nums, k):
#     # Your code here

#     # Plan

#     # make temporary arrays and calculate its maximum.
#     # Move the limits of the temporary arrays, while posible.

#     left = 0
#     right = k
#     lst = []

#     while right <= len(nums):

#         lst.append(max(nums[left:right]))
#         left +=1
#         right +=1

#     return lst

def sliding_window_max(nums, k):

    # Set a queue
    deque = collections.deque()

    # built the return list
    lst = []

    for i, n in enumerate(nums):

        # dequeue all elements lower than the comming element
        while deque and nums[deque[-1]] < n:

            deque.pop()
        
        # append the index of the new maximum
        deque.append(i)
        
        # remove not (anymore) useful indexes from the queue
        if deque[0] == i - k:
            
            deque.popleft()
        
        # Add the maximum value to the return list
        if i >= k -1:

            lst.append(nums[deque[0]])
    
    return lst




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

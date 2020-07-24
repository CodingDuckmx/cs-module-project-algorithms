'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    # Get the unique values.

    # Pop those values from the array.

    # Compare the left array and the set of unique values.

    unique = set(arr)

    for i in unique:
        arr.pop(arr.index(i))

    return unique.symmetric_difference(arr).pop()



# def single_number(arr):

#     # Make a dictionar for counting the values on the original array.
#     nums = {k:0 for k in arr}

#     # count the arrays in the array
#     for i in arr:
#         nums[i] +=1

#     # find that element that appears just once.
#     for k,v in nums.items():
#         if v == 1:
#             return k

##### Improved version to O(1) of space complexity #####

# def single_number(arr):

#     for item in arr:
#         if arr.count(item) == 1:

#             return item



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
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

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
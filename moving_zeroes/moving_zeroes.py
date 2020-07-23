'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    # Create a new list with non zero values, and count the values of the original array.

    lst = []
    count =0

    for i in range(0,len(arr)):
        if arr[i] !=0:
            lst.append(arr[i])
        else:
            count +=1

    return lst + [0] * count


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
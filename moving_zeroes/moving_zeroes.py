'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
# #     # Your code here

# #     # Create a new list with non zero values, and count the values of the original array.

#     lst = []
#     count = 0

#     for i in range(0,len(arr)):
#         if arr[i] != 0:
#             lst.append(arr[i])
#         else:
#             count += 1

#     return lst + [0] * count


###### Improved version ######

def moving_zeroes(arr):

    left = 0
    right = len(arr) -1 

    while left < right:

        # if arr[left] == 0 and arr[right] != 0:
        #     arr[left], arr[right] = arr[right], arr[left]
        #     left += 1
        #     right -= 1

        # elif arr[left] !=0 and arr[right] == 0:
        #     left +=1

        # elif arr[left] == 0 and arr[right] == 0:
        #     right -=1
        # else:
        #     right -=1

        #### or ####

        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        if arr[left] !=0:
            left +=1

        if arr[right] == 0:
            right -=1


    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
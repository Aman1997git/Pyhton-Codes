# Python 3 code for finding number of rotation in a rotated array


def find_rotation(arr, beg, leng):
    left = int(beg)
    right = int(leng)
    mid = int(left + (right - left)/2)

    if arr[left] < arr[mid] and arr[left] < arr[right]:
        return print(' Array not rotated')


    if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]:
        return mid

    if arr[mid] < arr[right] and arr[mid - 1] < arr[mid]:
        right = mid + 1
        return find_rotation(arr,left, right)

    else:
        left = mid
        return find_rotation(arr, mid, right)

    
# Driver code

while True:
    leng = int(input("Enter the amount of element you want to enter in array"))
    arr = []

    for i in range(leng):
        data = int(input('enter element'))
        arr.append(data)
    rotation = find_rotation(arr, 0, leng - 1)
    print(' Number of rotation is ', rotation)
    choice = input(print("do you want to continue..press 'y' for yes otherwise press any key to exit"))[0]
    print(choice)
    if (choice != 'y'):
        break
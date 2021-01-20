# Python 3 code for finding number of rotation in a rotated array


def find_mini(arr, beg, leng):
    left = int(beg)
    right = int(leng)
    mid = int(left + (right - left) / 2)

    if arr[left] < arr[mid] and arr[left] < arr[right]:
        return arr[left]

    if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]:
        return arr[mid]

    if arr[mid - 1] < arr[mid] and arr[mid] < arr[right]:
        return find_mini(arr, left, mid + 1)

    else:
        return find_mini(arr, mid, right)


# Driver code

while True:
    leng = int(input("Enter the amount of element you want to enter in array"))
    arr = []

    for i in range(leng):
        data = int(input('enter element'))
        arr.append(data)
    mini = find_mini(arr, 0, leng - 1)
    print(' Minimum number is ', mini)
    choice = input(print("do you want to continue..press 'y' for yes otherwise press any key to exit"))[0]
    print(choice)
    if choice != 'y':
        break
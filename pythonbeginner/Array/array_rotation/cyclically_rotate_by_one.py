
def rotate(arr, leng, n):

    for i in range(n):
        left_shift(arr, leng-1)
    return arr


def left_shift(arr, leng):
    temp = arr[0]
    for i in range(leng):
        arr[i] = arr[i+1]
    arr[leng] = temp
    return arr

# Driver code


leng = int(input("Enter the amount of element you want to enter in array"))
arr = []

for i in range(leng):
    data = int(input('enter element'))
    arr.append(data)
arr.sort()
while True:
    n = int(input("Enter the number of times you want to rotate array"))
    arr = rotate(arr, leng, n)
    print(arr)
    choice = input(print("do you want to continue..press 'y' for yes othewise press any key to exit"))[0]
    print(choice)
    if(choice != 'y'):
        break
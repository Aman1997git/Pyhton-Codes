# python 3 code for finding multipal rotations

# Function to rotate array multipal times
def rotate(arr, end):
    rotation = int(input(print(' How many times you want to rotate')))
    for i in range(rotation):
        arr = shift(arr, end)
        print(arr)
        print('Rotation {} : {} '.format((i + 1), arr))


# Function to shift position of elements in array
def shift(arr, end):
    shift1 = int(input(print(' Upto which position you want to shift ')))
    shift1 = shift1 % end
    gcd = g_c_d(end, shift1)
    for i in range(gcd):
        temp = arr[i]
        a = i
        while True:
            c = shift1 + a
            if c >= end:
                c = c - end
            if c == i:
                break
            arr[a] = arr[c]
            a = c
        arr[a] = temp
    return arr


# Function to calculate GCD
def g_c_d(a, b):
    if b == 0:
        return a
    else:
        return g_c_d(b, a % b)


# Driver code
while True:
    leng = int(input("Enter the amount of element you want to enter in array"))
    arr = []
    for i in range(leng):  # Taking elements of array from user
        data = int(input('enter element'))
        arr.append(data)
    rotate(arr, leng)
    choice = input(print("do you want to continue..press 'y' for yes otherwise press any key to exit"))[0]
    print(choice)
    if choice != 'y':
        break
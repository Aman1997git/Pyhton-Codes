# find pair in a sorted array : Ex :- ( 3,4,5,6,,7,3,1). find 11 ,output =true( 5+6 =11 )
def find_pair(arr, leng, key):
    for i in range(leng):  # first pointer

        for j in range(0, leng):  # second pointer
            if i == j:
                continue
            if key == arr[i] + arr[j]:  # this will check weather pair is avialable in
                                        # list or not by adding values of both pointers
                prnt(i, arr[i], j, arr[j])
                return 1
    else:
        return -1


def prnt(index1, value1, index2, value2):
    print('pair found')
    print("index of element is index={} ,index={} and value={},value={}".format(index1, index2, value1, value2))
    print(arr)

# Driver code


leng = int(input("Enter the amount of element you want to enter in array"))
arr = []
for i in range(leng):
    data = int(input('enter element'))
    arr.append(data)
arr.sort()
while True:
    key = int(input("Enter the pair you want to find"))
    result1 = find_pair(arr, leng, key)
    if result1 == -1:
        print('pair not found')

    choice = input(print("do you want to continue..press 'y' for yes or press any key to exit"))[0]
    if choice != 'y':
        break
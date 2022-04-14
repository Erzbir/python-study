cheboard = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], ]


def cheker(arr):
    if arr is None:
        return 0
    if len(arr) == 1:
        return 1
    for i in range(len(arr[0])):
        arr[0][i] = 1
    for i in range(len(arr)):
        arr[i][0] = 1
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
    return arr[len(arr) - 1][len(arr[0]) - 1]


a = cheker(cheboard)
print(f"需要的次数:{a}")

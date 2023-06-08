arr = [[0, 2, 3, 4, 5], [2, 3, 4, 5, 6]]

A = arr[0:2]
print(A)
N = 3

for i in range(N):
    for j in range(N):
        if i == j:
            print('A', i, j)
            flag = True
            continue

        print('B', i, j)
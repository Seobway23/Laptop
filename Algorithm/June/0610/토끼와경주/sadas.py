B = [[1,2], [1,9], [1,4], [1,8], [1,2]]

next_list = sorted(B, key=lambda x: (x[0], -x[1]))
print(B)
print(next_list)
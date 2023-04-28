a = [{'a':1}, {'b':13},{'c':2},{'d':4}]

a.sort(key=lambda x:x[1])
print(a)
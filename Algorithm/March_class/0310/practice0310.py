my_list=[(1,2,3),(4,5,6),(7,8,9)]
# 튜플을 리스트로 바꾸는 법
my_list = [list(x) for x in my_list]
#print(my_list)
a = list(map(list, my_list))
print(a)


my_list = [list(x) for x in my_list]
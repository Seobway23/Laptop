'''
# 0000 -> 4자리 빈자리에도 0 이 있어야 함
0~9
# A(10), B(11), C(12), D(13), E(14), F(15)
'''
def Bbit_print(i):
    global output
    for j in range(3, -1, -1):
        output += "1" if i & (1<< j) else "0"



    #return output


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for test_case in range(1, T+1):
    N, str1 = input().split()
    str1_t = []
    for i in str1:
        if i.isdigit():
            str1_t.append(int(i))
        else:
            str1_t.append(int(dic[i]))

    output = ""

    #이진수 판별
    for k in str1_t:
        Bbit_print(k)

    print(f"#{test_case} {output}")






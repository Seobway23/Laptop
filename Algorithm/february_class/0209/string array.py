import sys
from pprint import pprint
sys.stdin =open("input.txt","r",encoding='UTF8')
#encoding= UTF 8 필수


T = 10
for test_case in range(1, T + 1):
    t = int(input())
    cnt = 0
    str2 = input()
    str1 = input()
    A=len(str1)-len(str2)

    for i in range(A+1):
        cnt2 = 0
        B=str1[i]
        C=str2[0]
        if B == C:
            for j in range(len(str2)):
                D=str1[i + j]
                F=str2[j]
                if D == F:
                    cnt2 += 1

            if cnt2 == len(str2):
                cnt += 1

    print(f"#{t} {cnt}")


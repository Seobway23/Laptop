import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    target = list(input());
    #최소, 최대값 설정
    mnn = ''
    for K in target:
        mnn += K
    mn = int(mnn); mx = int(mnn);

    i = 0
    while i < len(target)-1:
        j = i + 1
        while j < len(target):
            # a deepcopy
            a = []
            for b in target:
                a.append(b)

            if a[0]!= '0' or i != '0' and a[j] !='0':
                a[i], a[j] = a[j], a[i]
            #str로 변환
            str1 = ''
            for b in a:
                str1 += b

            if str1[0] =='0':
                i += 1
                continue

            if int(str1) == 0:
                mn, mx = 0, 0
                break

            # mn, mx 갱신
            if int(str1) > mx:
                mx = int(str1)

            if int(str1) < mn:
                mn = int(str1)


            j += 1

        i += 1


    print(f"#{test_case} {mn} {mx}")

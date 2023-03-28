#6개의 숫자를 모든 경우의 수로 배열시킨 후
#반을 나눠서 triplet, run 판별

def perm(i,k):
    global cnt
    if i == k:
        print(*p)
        cnt += 1

    else:
        for j in range(1, k):
            p[i],p[j] = p[j], p[i]
            perm(i + 1, k)
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)

cnt = 0
p = [1,2,3,4,5,6]
perm(0,4)
print(cnt)

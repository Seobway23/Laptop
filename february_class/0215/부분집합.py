def btk(i,k):
    if i==k:
        print(bit)

    else:
        bit[i]=0
        btk(i+1,k)
        bit[i]=1
        btk(i+1,k)

A=[1,2,3]
N=len(A)
bit=[0]*(N)
btk(0, N)


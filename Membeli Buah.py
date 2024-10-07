N,K = map(int,input().split())
A   = list(map(int,input().split()))

buah = 0
jenis =[]
for i in range(N):
    if A[i] <= K:
        buah += 1

print(buah)

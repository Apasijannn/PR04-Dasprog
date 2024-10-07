N, M = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
hasil = 0
P.sort()
C.sort()

if P[0] > 0 and C[0] > 0:  
    hasil -= (min(C) + max(P))
    
elif P[-1] < 0 and C[-1] < 0:
    hasil += sum(C) - max(P)
    
elif (P[0] > 0 and C[-1] < 0) or (P[-1] < 0 and C[0] > 0):
    if P < C:
        hasil == 0
else:
    beli = 0
    bayar = 0
    for i in P:
        if(i > 0):
            beli += i
    for j in C:
        if(j < 0):
            bayar += j
    hasil = bayar - beli 
print(hasil)
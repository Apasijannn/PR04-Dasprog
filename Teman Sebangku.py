N, r, c = map(int, input().split())
posisi={}

for i in range(N):
    x,a,b = map(int,input().split())
    posisi[(a,b)] = x 
    
for j in range(1, N + 1):
    a, b = -1, -1
    for (x, y), murid in posisi.items():
        if murid == j:
            a, b = x, y
            break
    if (a, b - 1) in posisi:
        print(posisi[(a, b - 1)])
    elif (a, b + 1) in posisi:
        print(posisi[(a, b + 1)])
    else:
        print(0)
        
            
            
    
 
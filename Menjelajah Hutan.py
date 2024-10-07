r, c, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(r)]
n = input()

i, j = 0, 0
emas = A[i][j]
valid = True
for gerak in n:
    if gerak == 'L' and j > 0:
        j -= 1
        A[i][j] = 0
        emas += A[i][j] - 2
    elif gerak == 'R' and j < c - 1:
        j += 1
        A[i][j] = 0
        emas += A[i][j] + 3
    elif gerak == 'D' and i < r - 1:
        i += 1
        A[i][j] = 0
        emas += A[i][j] - 2
    elif gerak == 'U' and i > 0:
        i -= 1
        A[i][j] = 0
        emas += A[i][j] + 3
    else:
        valid = False
        break

if not valid or len(n) != N:
    print(emas)
    print("gerakanmu salah bung!")
else:
    print(emas)



    


        
        
    

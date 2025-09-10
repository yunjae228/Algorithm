N , B = input(), list(map(int, input().split()))

A = [B[0]]


for i in range(1,N):
    A.append(B[i]*(i+1)- sum(A))


# 수열 A = 3 1 5 11
# 수열 A = 

# 수열 B = 3 2 3 5
# 수열 B = 3/1, (3+1)/2 , (3+1+5)/3, (3+1+5+11)/4


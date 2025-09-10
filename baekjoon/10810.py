'''
1. N 크기의 배열을 생성 [0] * N
2. M번 만큼 반복
3. a,b,c = list(map(int, input().split()))
4. a-1 ~ b-1의 인덱스에 대한 값을 c로 채운다.
5. 만약, a-1 ~ b-1인덱스에 값이 존재한다면, 
6. a-1, b-1 인덱스에 해당하는 값을 c로 바꾼다. 
[ 0 0 0 0 0]


N , M = map(int, input().split())
bucket = [0] * (N + 1)

for _ in range(M):
    a , b, c = map(int, input().split())
    for z in (a, b+1):
        bucket[z] = c

for i in range(1, len(bucket)):
    print(bucket[i], end=' ')
'''
N, M = map(int, input().split())
basket = [0] * (N+1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        basket[n] = k 

for i in range(1, N+1):
    print(basket[i], end = ' ')    

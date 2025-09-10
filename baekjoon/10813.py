N , M = map(int, input().split())

bucket = [j for j in range(1, N+1)]

for i in range(M):
    a, b = map(int, input().split())
    temp = bucket[a-1]
    bucket[a-1] = bucket[b-1]
    bucket[b-1] = temp
    print(bucket)


for j in range(len(bucket)):
    print(bucket[j], end=' ')
N, M = map(int,input().split())
lst = list(map(int, input().split()))
number = []


for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if M < lst[i] + lst[j] + lst[k]:
                continue
            else:
                number.append(lst[i] + lst[j] + lst[k])
print(max(number))


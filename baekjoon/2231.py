n = int(input())
cnt = 0

for i in range(1, n+1):
    num = list(map(int, str(i)))
    sum_num = sum(num) + i
    if sum_num == n:
        print(i)
        break
    if i == n:
        print(0)
S = int(input())


for _ in range(S):
    n , m = input().split(' ')
    for i in m:
        print(i * int(n), end='')
    print()
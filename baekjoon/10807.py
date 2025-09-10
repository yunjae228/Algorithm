A = int(input())
B = list(map(int, input().split()))
C = int(input())

count = 0

for i in range(A):
    if B[i] == C:
        count += 1

print(count)
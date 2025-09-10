A = int(input())
B = int(input())
result = 0

for i in range(B):
    C, D = map(int, input().split())
    result += C * D

if A == result:
    print("Yes")
else:
    print("No")
import sys

result = []


for i in range(9):
    result.append(int(sys.stdin.readline()))

max = max(result)
print(max)
print(result.index(max)+1)
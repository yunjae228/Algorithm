"""
입력으로는 막대기의 갯수를 나타내는 N 이 주어진다.
출력으로는 우측의 막대보다 길이가 큰 막대의 갯수를 출력한다. 단, 동일한 숫자는 카운트 되지 않는다.

"""

import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    stack.append(int(input()))

last = stack[-1]
count = 1

for i in reversed(range(N)):
    if stack[i] > last:
        count += 1
        last = stack[i]

print(count)
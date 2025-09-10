import sys

A = int(input())

for i in range(1, A+1):
    B, C = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {B} + {C} = {B+C}")
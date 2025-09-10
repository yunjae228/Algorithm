A, B, C = map(int, input().split())

if A == B and B == C:
    print(f"{10000+(A*1000)}")

elif A == B or A == C:
    print(f"{1000+(A*100)}")

elif B == C:
    print(f"{1000+(B*100)}")

else:
    print(max(A, B, C)*100)
from itertools import combinations

short = [int(input()) for _ in range(9)]

for pepole in combinations(short, 7):
    if sum(pepole) == 100:
        seven = list(pepole)
    else:    
        continue

seven.sort()

for i in range(len(seven)):
     print(seven[i])
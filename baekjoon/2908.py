N, M = input().split()

reversedN = int(str(N)[::-1])
reversedM = int(str(M)[::-1])

if reversedM > reversedN:
    print(reversedM)
else:
    print(reversedN)
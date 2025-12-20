dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
input = input()
ret = 0
for i in range(len(input)):
    for j in dial:
        if input[i] in j:
            ret += dial.index(j)+3
print(ret)

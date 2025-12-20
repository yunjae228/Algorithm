cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

s = input()



for i in cro:
    s = s.replace(i, "*")

print(len(s))

'''

1. cro의 각 요소들이 s에 있다면 해당 값 그대로 추출

2. 만약 없다면, 비교

모두 추출 한뒤, 문자열 배열로 저장

'''
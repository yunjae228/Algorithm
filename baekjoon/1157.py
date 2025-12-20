s = input().upper()

set_dupl = list(set(s))

l = []

for j in set_dupl:
   j = s.count(j)
   
   # l은 입력받은 문자열 s에서 겹치는 값의 갯수 모음
   # [ 4, 4, 1, 1 ]
   l.append(j)


# list.count(a) 는 요소안에 a가 얼마나 있는지 반환 해줌
# max(list) 는 list안에 최댓값을 찾아줌

# 고로, l안에는 겹치는 값의 갯수 모음이고, 이 모음 중 가장 큰 값의 갯수가 2개 이상이면
# 가장 많이 겹치는 문자가 2개 이상 있다는 것이니 ? 를 반환
if l.count(max(l)) >= 2:
   print("?")

else:
   print(set_dupl[l.index(max(l))])
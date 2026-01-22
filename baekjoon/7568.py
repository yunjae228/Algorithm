"""
1. 입력 받은 학생들의 모든 순위를 매겨야 하기에 완전탐색을 해야함

2. 첫째줄 입력 수 만큼 반복을 진행.

3. 첫번째 요소의 0번째 인덱스, 1번째 인덱스와 두번째 ~ n번째 요소의 0번째 인덱스, 1번째 인덱스를 비교함

4. 만약 n번째 요소의 0번째 인덱스, 1번째 인덱스의 값이 n+1번째 인덱스보다 클 경우, grade 등급을 1 증가

5. 탐색이 끝난 후, 본인의 등수를 정하기 위해 +1 을 카운트.

"""

n = int(input())

student = [list(map(int, input().split())) for _ in range(n)]

ans = []

for i in range(len(student)):
    count = 0
    for j in range(len(student)):
        if student[i][0] < student[j][0] and student[i][1] < student[j][1]:
            count += 1
    ans.append(count+1)

for i in ans:
    print(i, end=' ')
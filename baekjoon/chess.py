'''
체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.

동혁이가 발견한 흰색 피스의 개수가 주어졌을 때, 몇 개를 더하거나 빼야 올바른 세트가 되는지 구하는 프로그램을 작성하시오.

'''
success_chess = [1, 1, 2, 2, 2, 8]
chess = list(map(int, input().split()))

# chess 리스트를 리스트 크기 만큼 for문 돌며 킹, 퀸, 룩, 비숍, 나이트 , 폰
# success 리스트의 각 인덱스와 비교
# 만약 값이 일치하지 않는다면, success key의 value - find_chess의 value 로 수정

result = []
for i in range(len(chess)):
    print(success_chess[i] - chess[i], end=' ')
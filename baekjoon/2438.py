N = int(input())

'''
1일때는 별 1개
2일때는 별 2개
3일때는 별 3개

(문자열)* * N
'''

for i in range(1, N+1):
    print(f"*"* i)
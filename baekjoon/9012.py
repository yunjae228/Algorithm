'''


1. 입력은 T개의 테스트 데이터로 주어진다.

2. 입력 괄호문자열이 올바른 괄호 문자열이면 YES , 아니면 NO

3. 올바른 괄호 문자열을 판별하기 위해 stack을 사용하며, 변수 check_list 를 빈 배열로 초기화 한다.

4. 들어오는 문자열이 "("일 경우, check_list에 append를 한다.

key point
 - "(" ")" 가 만날경우 check_list에 쌓인 "(" 를 제거한다.
 - "(" 만 check_list에 쌓아서, 검증한다.
 - 각 문자열에 대한 반복이 끝났을때, check_list에 아무것도 없는경우 YES를 출력한다.
 - 그리고 check_list의 크기가 0이 아닐때도 NO를 출력한다
 - 크기를 0으로 초기화한다. -> 는 없어도 될듯 다음 반복문에 초기화됨.
 - 첫 문자열로 ) 가 들어올경우, 바로 NO를 출력하고 continue 한다.

'''

S = int(input())

for _ in range(S):
    vps = input()
    check_list = []

    for i in vps:
        if i == "(":
            check_list.append(i)
        elif i == ")":
            if check_list:
                check_list.pop()
            else:
                print("NO")
                break
    else:
        if check_list:
            print("NO")
        else:
            print("YES")

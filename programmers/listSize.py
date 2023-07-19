'''
정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. mylist에 들은 각 원소의 길이를 담은 리스트를 리턴하도록 solution 함수를 작성해주세요.

제한 조건
mylist의 길이는 100 이하인 자연수입니다.
mylist 각 원소의 길이는 100 이하인 자연수입니다.

'''

def solution(mylist):
    # 블로그 포스팅때 썼던 리스트 컴프리헨션을 사용해보아따
    answer = [len(n) for n in mylist]
    print(answer)
    return answer

"""
1. 입력 : 전공과목 학점 과목평점 -> 20개

2. 출력 : (학점 * 과목평점) + ( 학점 * 과목평점) ... / 학점 총합

3. 과목 평점을 저장하기 위한 딕셔너리 타입 변수 computer_science 선언한다.

4. 학점 총합을 계산하기 위한 변수 total 을 0으로 초기화 한다.

5. 학점 * 과목평점 값을 저장하기 위한 변수 grade을 0으로 초기화 한다.

6. 반복문안에서 공백을 기준으로 자른뒤, 첫번째 값 ( 학점 ) 과 두번째 값 ( 등급) 을 곱한값을 grade 변수에 더한다.

6-1. 두번째 값 ( 등급)을 key로 삼아, 두번째 값 ( 등급) 에 해당하는 value값을 가져온다.

6-2. 두번째 값 ( 등급 )이 P일 경우 computer_science 딕셔너리에 키가 없으니, get을 할때 기본값은 0으로 준다.
 ( dict.get(key, 0))

7. 모든 계산이 끝난뒤 grade / total 을 리턴한다.

"""

total = 0

grade = 0

computer_science = {
    'A+': 4.5 ,
    'A0': 4.0 ,
    'B+': 3.5 ,
    'B0': 3.0 ,
    'C+': 2.5 ,
    'C0': 2.0 ,
    'D+': 1.5 ,
    'D0': 1.0 ,
    'F': 0.0    
}

for _ in range(20):
    s = input().split(' ')
    if s[2] == 'P':
        continue
    total += float(s[1])

    grade += float(s[1]) * float(computer_science.get(s[2], 0))

print( grade / total )

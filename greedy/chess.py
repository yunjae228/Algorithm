'''
주어진 8 X 8 체스판에서 , 특정한 좌표가 주어졌을 때,
나이트가 이동 가능한 경로의 경우의 수를 출력 하시오.

나이트는
수평으로 두칸 이동한 뒤에 수직으로 한 칸 이동하거나,
수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동할 수 있습니다.

행의 좌표는 1~8 까지로 표시하며, 열의 좌표는 a~h 까지로 표시합니다.
'''


def chess():
    count = 0
    information = input()
    row = int(information[1])
    # 열의 값은 a~h 까지의 문자로 주어지므로 아스키 코드로 변경 후 (예 : a = 97) a로 빼고 1을 더하면 해당 열의 값을 구할 수 있다.
    # information[0]가 c일 경우는 99 이므로, a=97을 뺀후 , 1을 더하면 열의 좌표인 3이 된다.
    colunm = int(ord(information[0])) - int(ord('a')) + 1

    # 나이트가 이동가능한 좌표를 튜플 리스트로 저장해놓는다.
    # ex) x 좌표가 -2 가 된다는 것은 위로 이동한다는 것, 또한 y 좌표가 1 이 되는 것은 오른쪽으로 이동
    steps = [(-2, 1), (-2, -1), (-1, 2), (1, 2), (2, -1), (2, 1), (1, -2), (-1, -2)]

    for step in steps:
        # 나이트가 이동 가능한지 체크
        # 들어온 행 값 ( information[1])에 x좌표를 더해 계산함
        next_row = row + step[0]
        # 들어온 열 값 ( information[1])에 y좌표를 더해 계산함
        next_colunm = colunm + step[1]

        # 이동 가능한 스텝은 체스 판 8x8 크기 안에 있어야 함.
        if 1 <= next_row <= 8 and 1 <= next_colunm <= 8:
            count += 1
    print(count)


chess()

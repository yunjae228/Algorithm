'''
<음료수 얼려먹기>
N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 있는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.

이때, 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

문제 해결 아이디어 ?
연결된 요소 찾기 문제 .
DFS , BFS로 해결이 가능.

1. 특정 지점의 주변 상,하,좌,우를 방문한 뒤, 값이 0이면서 아직 방문하지 않았다면 해당 지점을 방문.

2. 방문한 지점에서 다시 1번과정을 반복하면, 연결된 모든 지점을 방문 가능

3. 방문하지 않은 지점의 수를 카운트 .
'''

# N, M(행, 열) 입력
n, m = map(int, input().split())

# 주어진 배열 리스트 초기화
graph = []


def main():
    # N, M 크기 얼음틀 생성
    for i in range(n):
        graph.append(list(map(int, input())))

    result = 0
    # 모든 노드에 대하여 탐색
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

    print(result)


def dfs(x, y):
    # 이동하려는 노드가 범위 밖일 시, 바로 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 이동한 노드가 구멍이 뚫려 있다면
    if graph[x][y] == 0:
        # 방문 체크
        graph[x][y] = 1
        # 인접한 모든 노드 (상,하,좌,우) 탐색
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    # 이동한 노드가 구멍이 뚫려있지 않다면 바로 종료
    return False


main()

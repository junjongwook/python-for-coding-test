#-*- coding: utf-8 -*-
from collections import deque

# N, M을 공백으로 구분하여 입력받기
N, M = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우는 무시
            if not (0 <= nx < M and 0 <= ny < N):
                continue
            # 벽인 경우도 무시
            if graph[ny][nx] == 0:
                continue
            # 해당 노드를 처음 방문할 경우에만 최단 거리 기록
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[N-1][M-1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
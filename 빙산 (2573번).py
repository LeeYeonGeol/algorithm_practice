import sys
from collections import deque

input = sys.stdin.readline

# 행, 열
N, M = map(int, input().split())

# 지도 입력
bingsan = []
for _ in range(N):
    bingsan.append(list((map(int, input().split()))))

# 초기 빙산 개수
bingsan_cnt = 0
for i in range(N):
    bingsan_cnt += sum(bingsan[i])

# 동서남북
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

years = 0
while 1:
    # 갈라졌는지 체크
    q = deque()
    checked = 0

    visited = [[0]*M for _ in range(N)]

    for a in range(N):
        for b in range(M):
            if bingsan[a][b] != 0:
                q.append((a, b))
                checked = bingsan[a][b]
                visited[a][b] = 1
                break
            if q:
                break

    # 빙산이 쪼개지지 않고 녹아버리는 경우
    if checked == 0:
        years = 0
        break

    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and bingsan[nx][ny] != 0 and visited[nx][ny] == 0:
                checked += bingsan[nx][ny]
                q.append((nx, ny))
                visited[nx][ny] = 1

    # 쪼개진 경우 break
    if checked != bingsan_cnt:
        break

    melting = [[0]*M for _ in range(N)]
    melts = 0
    for x in range(N):
        for y in range(M):
            cnt = 0
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < M and bingsan[nx][ny] == 0 and bingsan[x][y] != 0:
                    cnt += 1
                    melts += 1
            melting[x][y] = cnt


    for x in range(N):
        for y in range(M):
            if bingsan[x][y] > melting[x][y]:
                bingsan[x][y] -= melting[x][y]
                bingsan_cnt -= melting[x][y]
            else:
                bingsan_cnt -= bingsan[x][y]
                bingsan[x][y] = 0

    years += 1

print(years)

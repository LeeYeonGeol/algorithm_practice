from collections import deque

# 가로, 세로 길이
N, M = map(int ,input().split())


maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

times = 0

# 방향 설정 
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

melting = []
while 1:
    # 다 녹았는지 체크
    sums = 0
    for idx in range(N):
        sums += sum(maps[idx])

    if sums == 0:
        break

    # BFS 실행
    melting = []

    visited = [[0]*M for _ in range(N)]

    # q 생성
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        visited[x][y] = 1

        # 0 -> 1만 필터링
        if maps[x][y] == 1:
            continue

        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if  maps[nx][ny] == 1:
                    melting.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

        for a, b in melting:
            maps[a][b] = 0
    
    times += 1

print(times)
print(len(melting))

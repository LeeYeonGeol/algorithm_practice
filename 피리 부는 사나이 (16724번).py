from collections import deque, defaultdict

# 행, 열
N, M = map(int, input().split())

# 지도 입력
maps = []
for _ in range(N):
    maps.append(list(input()))

# visit check
visited = [[0]*M for _ in range(N)]

cnt = 0
excluded = 0
for a in range(N):
    for b in range(M):
        # 방문여부 확인
        if visited[a][b] != 0:
            continue
        
        cnt += 1
        q = deque()
        q.append((a, b))

        while q:
            x, y = q.popleft()
            visited[x][y] = cnt

            # 다음 목적지 고려
            nx, ny = 0, 0
            if maps[x][y] == 'D':
                nx, ny = x+1, y 
            elif maps[x][y] == 'U':
                nx, ny = x-1, y
            elif maps[x][y] == 'L':
                nx, ny = x, y-1
            else:
                nx, ny = x, y+1
            
            # boundary & 지나친적 없는 경우만
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                elif visited[nx][ny] == cnt:
                    visited[x][y] = visited[nx][ny] 
                else:
                    excluded += 1
                                 
print(cnt-excluded)

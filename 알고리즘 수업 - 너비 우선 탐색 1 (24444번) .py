from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int ,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)

q = deque()
q.append(R)
visited[R] = 1

cnt = 2

answer = []

while q:
    vert = q.popleft()
    answer.append(vert)
    for next_v in sorted(graph[vert]):
        if visited[next_v] == 0:
            visited[next_v] = cnt
            cnt += 1
            q.append(next_v)

for v in visited[1:]:
    print(v)

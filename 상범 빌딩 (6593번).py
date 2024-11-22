import sys
from collections import deque

input = sys.stdin.readline

while 1:
    # L = 층수, R, C = 행 & 열
    L, R, C = map(int, input().split())

    # 종료 조건
    if L == 0 and R == 0 and C == 0:
        break

    buildings = []
    building = []
    while 1:
        sentence = list(input().rsplit())
        if sentence:
            building.append(list(sentence[0]))
        else:
            buildings.append(building)
            building = []

        if len(buildings) == L:
            break

    sb, sx, sy = 0, 0, 0
    tb, tx, ty = 0, 0, 0

    for a in range(L):
        for b in range(R):
            for c in range(C):
                if buildings[a][b][c] == "S":
                    sb, sx, sy = a, b, c
                elif buildings[a][b][c] == "E":
                    tb, tx, ty = a, b, c

    visited = []

    for _ in range(L):
        visited.append([[0]*C for _ in range(R)])

    direction = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0,-1, 0), (1, 0, 0), (-1, 0, 0)]

    q = deque()
    q.append((sb, sx, sy, 0))

    visited[sb][sx][sy] = 1

    while q:
        b, x, y, minute = q.popleft()
        if b == tb and x == tx and y == ty:
            print(f"Escaped in {minute} minute(s).")
            break

        for db, dx, dy in direction:
            nb, nx, ny = b+db, x+dx, y+dy
            if 0 <= nb < L and 0 <= nx < R and 0 <= ny < C and visited[nb][nx][ny] == 0 and buildings[nb][nx][ny] in [".", "E"]:
                visited[nb][nx][ny] = 1
                q.append((nb, nx, ny, minute+1))
    else:
        print("Trapped!")


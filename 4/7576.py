from collections import deque

m, n = map(int, input().split())
tomatoes = []
ripe = []
for i in range(n):
    tomatoes.append(list(map(int, input().split())))
    for j in range(m):
        if tomatoes[i][j] == 1:
            ripe.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque(ripe)
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and tomatoes[nx][ny] == 0:
            tomatoes[nx][ny] = tomatoes[x][y] + 1
            q.append((nx, ny))

answer = 0
is_finished = False
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 0:
            print(-1)
            is_finished = True
            break
        answer = max(answer, max(tomatoes[i]))
    if is_finished:
        break
else:
    print(answer - 1)

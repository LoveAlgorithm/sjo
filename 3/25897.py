def check(grid, word, x, y, dir, r, c):
    l = 2
    while True:
        if l == len(word):
            return x, y, dir
        nx = (x + dx[dir]) % r
        ny = (y + dy[dir]) % c
        if grid[nx][ny] == word[l]:
            x = nx
            y = ny
            l += 1
        else:
            break
    return -1, -1, -1


n = int(input())
dx = [0, 0, 1, -1]  # 동, 서, 남, 북
dy = [1, -1, 0, 0]
dir_str = ['R', 'L', 'D', 'U']

for i in range(1, n + 1):
    r, c = map(int, input().split())    # row, column
    grid = []   # 퍼즐 판
    for _ in range(r):
        grid.append(list(map(str, input())))

    s = int(input())    # 찾을 단어의 개수
    words = []  # 찾을 단어 리스트
    for _ in range(s):
        words.append(input())

    if i > 1:
        print()
    print(f'Word search puzzle #{i}:')

    for word in words:
        for i in range(r):
            for j in range(c):
                if grid[i][j] == word[0]:
                    for k in range(4):
                        ni = (i + dx[k]) % r
                        nj = (j + dy[k]) % c
                        if grid[ni][nj] == word[1]:
                            x, y, k = check(grid, word, ni, nj, k, r, c)
                            if k != -1:
                                print(dir_str[k], i + 1, j + 1, word)
                                break

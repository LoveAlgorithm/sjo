months = [0] * 13
n = int(input())
for _ in range(n):
    birthday = list(map(str, input().split()))[1]
    d, m, y = map(int, birthday.split('/'))
    months[m] += 1

for i in range(1, 13):
    print(i, months[i])

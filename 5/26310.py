n = int(input())
regionals = []
for _ in range(6):
    country, pt, pu, rt, ru, f = map(str, input().split())
    regionals.append([country, int(pt), int(pu), int(rt), int(ru), int(f)])


for i in range(6):
    country, pt, pu, rt, ru, f = regionals[i]
    score = (0.56 * ru) + (0.24 * rt) + (0.14 * pu) + (0.06 * pt) + (00.3 * f)
    regionals[i].append(score)

regionals = sorted(regionals, key=lambda x: x[6], reverse=True)

answer = 0
for i in range(6):
    if regionals[i][0] == 'Taiwan':
        answer += n // 6
        if i < n % 6:
            answer += 1
        print(answer)
        break
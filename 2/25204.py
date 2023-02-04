from functools import cmp_to_key

def compare(x, y):
    i = 0
    min_len = min(len(x), len(y))

    while i < min_len and x[i] == y[i]:
        i += 1
    
    if i == len(x):
        return -1
    if i == len(y):
        return 1
    if x[i] == '-' and y[i] != '-':
        return 1
    if y[i] == '-' and x[i] != '-':
        return -1
    if x[i].lower() == y[i].lower():
        return -1 if x[i].isupper() else 1
    return -1 if x[i].lower() < y[i].lower() else 1


t = int(input())

for _ in range(t):
    words = []
    n = int(input())
    for _ in range(n):
        words.append(input())
    words = sorted(words, key=cmp_to_key(compare))
    for word in words:
        print(word)
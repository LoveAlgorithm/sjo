a = input()
b = input()

alpha = [0] * 26
for c in a:
    alpha[ord(c) - 97] += 1
for c in b:
    alpha[ord(c) - 97] += 1

for i in range(26):
    for _ in range(alpha[i]):
        print(chr(i + 97), end="")
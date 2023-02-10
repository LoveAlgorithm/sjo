emoji = input()
colon = 0
underBar = 0

for c in emoji:
    if c == ':':
        colon += 1
    elif c == '_':
        underBar += 1

print(len(emoji) + colon + underBar * 5)
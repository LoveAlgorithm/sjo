n, m, a, c, x0 = map(int, input().split())

sequence = []
prev = x0

# sequence 담기
for _ in range(n):
    x = (a * prev + c) % m
    sequence.append(x)
    prev = x


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


answer = 0
for num in sequence:
    if binary_search(sequence, num, 0, n - 1) != -1:
        answer += 1

print(answer)
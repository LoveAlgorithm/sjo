operators = ['+', '-', '*', '/']
nums = list(map(int, input().split()))
candidates = []

def calculate(i, num):
    if i == 3:
        if num >= 0:
            candidates.append(num)
        return
    calculate(i + 1, num + nums[i])
    calculate(i + 1, num - nums[i])
    calculate(i + 1, num * nums[i])
    if num % nums[i] == 0:
        calculate(i + 1, num // nums[i])


calculate(1, nums[0])
print(min(candidates))
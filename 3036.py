import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


def GCD(x, y):
    return GCD(y, x%y) if y else x


for i in range(1, n):
    gcd = GCD(arr[0], arr[i])
    lcm = arr[0] * arr[i] // gcd
    print(f"{lcm//arr[i]}/{lcm//arr[0]}")
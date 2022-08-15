import sys
T = int(sys.stdin.readline())


def Sol_1():
    ans = [1, 2, 4]
    for i in range(4, 11):
        ans.append(sum(ans[-3:]))
    for _ in range(T):
        n = int(sys.stdin.readline())
        print(ans[n - 1])


class Sol_2:
    def __init__(self):
        self.arr = [0 for i in range(12)]

    def func(self, x):
        if x <= 2: return x
        if x == 3: return 4
        if self.arr[x] == 0: self.arr[x] = self.func(x-1)+self.func(x-2)+self.func(x-3)
        return self.arr[x]

    def exe(self):
        for _ in range(T):
            n = int(sys.stdin.readline())
            print(self.func(n))
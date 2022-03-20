from numpy import prod

memo = {}


def solve(t):
    a, b = map(int, input().split(' '))
    count = 0
    for i in range(a, b + 1):
        cur = [int(x) for x in str(i)]
        cur.sort()
        tup = "".join(map(str,cur))
        if memo.get(tup) is not None:
            if memo[tup] == True:
                count += 1
            continue
        p = prod(cur)
        s = sum(cur)
        if p % s == 0:
            count += 1
            memo[tup] = True
        else:
            memo[tup] = False
    print('Case #' + str(t) + ': ' + str(count))


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        solve(i)


def f():
    n, k, q = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    
    ans = 0
    len = 0
    for i in range(n):
        if a[i] <= q:
            len += 1
        else:
            if len >= k:
                ans += (len - k + 1) * (len - k + 2) // 2
            len = 0
    
    if len >= k:
        ans += (len - k + 1) * (len - k + 2) // 2
    print(ans)
if __name__ == '__main__':
    for _ in range(int(input())):
        f()

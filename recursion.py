#C(n, k) = C(n - 1, k) + C(n - 1, k - 1)

def C(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1
    return C(n - 1, k) + C(n - 1, k - 1)

n, k = map(int, input().split())
print(C(n, k))
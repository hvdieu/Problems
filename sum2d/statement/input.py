import random

random.seed(17121997)

def randrange(l, r, x = 0):
    res = random.randrange(l, r)
    for i in xrange(x):
        res = max(res, random.randrange(l, r))
    for i in xrange(-x):
        res = min(res, random.randrange(l, r))
    return res

for test in xrange(1, 21):
    limit1 = max(3, int(2 * (10 ** (test / (20 / 2.0))) + 1))
    limit2 = max(5, int(10 ** (test / (20 / 9.0)) + 1))
    limit3 = max(5, int(4 * (10 ** (test / (20 / 4.0))) + 1))
    m = randrange(1, limit1, test - 1)
    n = randrange(1, limit1, test - 1)
    a = [[randrange(-limit2 + 1, limit2) for x in xrange(n)] for y in xrange(m)]
    f = [[0] * (n + 1) for y in xrange(m + 1)]
    for i in xrange(m):
        for j in xrange(n):
            f[i + 1][j + 1] = f[i][j + 1] + f[i + 1][j] - f[i][j] + a[i][j]
    k = randrange(1, limit3, test - 1)
    queries = []
    for i in xrange(k):
        x = randrange(0, m)
        y = randrange(x, m)
        p = randrange(0, n)
        q = randrange(p, n)
        queries.append((x, p, y, q))
    with open("%02d.in" % test, "w") as fi:
        print >> fi, m, n, k
        print >> fi, "\n".join(" ".join(map(str, x)) for x in a)
        print >> fi, "\n".join("%d %d %d %d" % (x[0] + 1, x[1] + 1, x[2] + 1, x[3] + 1) for x in queries)
    with open("%02d.a" % test, "w") as fi:
        for x, y, z, t in queries:
            print >> fi, f[z + 1][t + 1] - f[z + 1][y] - f[x][t + 1] + f[x][y]
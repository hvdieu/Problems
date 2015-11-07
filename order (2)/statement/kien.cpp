#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define long long long
const int oo = 0x3c3c3c3c, N = 100005;
int n, x[N];
long F[2][N][52];
bool FF[2][N][52];
#define C p<q][p][abs(p-q)

long f(int u, int p, int q) {
	if (u==n+1) return 0;
	if (abs(q-p)>=50) return 1LL*oo*oo;
	if (FF[C]++) return F[C];
	long F1 = f(u+1, u, q) + abs(x[p]-x[u]);
	long F2 = f(u+1, p, u) + abs(x[q]-x[u]);
	//printf("f(%d, %d, %d) = %lld, %lld\n", u, p, q, F1, F2);
	return F[C] = min(F1, F2);
}

main() {
//	freopen("order.inp", "r", stdin)&&
//	freopen("order.out", "w", stdout);

	scanf("%d", &n);
	for (int i=1; i<=n; i++)
	scanf("%d", &x[i]);
	for (int i=n; i>=1; i--)
	for (int j=0; j<=50; j++)
	if (i-1+j<=n) {
		f(i, i-1, i-1+j);
		f(i, i-1+j, i-1);
	}
	cout << f(1, 0, 0) << endl;
}

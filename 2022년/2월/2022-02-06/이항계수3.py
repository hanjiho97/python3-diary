import sys
input = sys.stdin.readline

#분할정복 거듭제곱 함수
def mul(a, b, mod):
    if b==1:
        return a%mod
    m=mul(a, b//2, mod)
    if b%2:
        return m*m*a%mod
    else:
        return m*m%mod

#모듈러 연산을 이항계수의 정의식에 적용할 수 없다.
#(n!/k!(n-k)!)%P != n!%P/k!(n-k)!%P

N, K = map(int, input().split())

dp=[1]*(N+1)
MOD=1000000007

for i in range(2, N+1):
    dp[i]=i*dp[i-1]%MOD

#페르마 소정리를 이용
# (k!(n-k)!)^(p-1)=1 (mod p)
# (k!(n-k)!)^(p-2)=1/(k!(n-k)!) (mod p)
#(n!/k!(n-k)!)%P == ((n!%P)*((k!(n-k)!)^(p-2)%P))%P
den = mul(dp[N-K]*dp[K], MOD-2, MOD)

print(dp[N]*den%MOD)
import sys
input = sys.stdin.readline
formula=input().rstrip().split('-')

ans=sum(map(int, formula[0].split('+')))
for i in range(1, len(formula)):
    ans-=sum(map(int, formula[i].split('+')))
print(ans)
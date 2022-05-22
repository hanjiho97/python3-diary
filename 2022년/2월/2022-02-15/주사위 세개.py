import sys
input = sys.stdin.readline
one, two, three = map(int, input().split())
if one==two and two==three:
    print(10000+one*1000)
elif one==two or two==three:
    print(1000+two*100)
elif three==one:
    print(1000+one*100)
else:
    print(max([one, two, three])*100)
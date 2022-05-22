import sys
input = sys.stdin.readline

a, b = map(int, input().split())

while a and b:
    if not b%a:
        print("factor")
    elif not a%b:
        print("multiple")
    else:
        print("neither")
    a, b = map(int, input().split())
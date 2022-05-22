from audioop import reverse
import sys
input = sys.stdin.readline

data=(sorted(input().rstrip(), reverse=True))
print(''.join(data))
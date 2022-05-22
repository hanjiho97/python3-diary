import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n, *ack = map(int, input().split())
party = [list(map(int, input().split()))[1:] for _ in range(M)]

result=[0]
ans=0

def counting(start, ack, nack):
    global ans
    if not checking(ack, nack): return
    for i in range(start, M):
        if checking(party[i], ack):
            ans+=1
            counting(i+1, ack, adding(party[i], nack))
            ans-=1
            counting(i+1, adding(party[i], ack), nack)
        else: ack=adding(party[i], ack)
    if checking(ack, nack):
        result.append(ans)
    return

def checking(A, B):
    for a in A:
        if a in B:
            return False
    return True

def adding(A,B):
    C=B.copy()
    for a in A:
        C.add(a)
    return C

counting(0, set(ack), set())
print(max(result))
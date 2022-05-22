import sys
input = sys.stdin.readline

N = int(input())
crains = sorted(map(int, input().split()), reverse=True)
n = int(input())
boxes = sorted(map(int, input().split()), reverse=True)

#박스를 못 드는 경우
if(boxes[0]>crains[0]):
    print(-1)
else:
    #불필요한 크레인 제거 
    num = 0
    for i in range(-1, -len(crains)-1, -1):
        if(crains[i+num]<boxes[-1]):
            crains.pop()
            num+=1
        else:
            break

    #greedy algorithm
    total = 0
    while(boxes):
        cur=0
        for crain in crains:
            for i in range(cur, len(boxes)):
                if(crain>=boxes[i]):
                    boxes.remove(boxes[i])
                    break
                else:
                    cur+=1
        total+=1
    print(total)
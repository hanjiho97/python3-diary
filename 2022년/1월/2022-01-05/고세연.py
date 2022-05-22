n = int(input())
crains = list(map(int,input().split()))
m = int(input())
boxes = list(map(int,input().split()))
crains.sort(reverse=True)
boxes.sort(reverse=True)
maxweight = max(crains)
ans=0
for box in boxes:
    if box> maxweight:
        ans = -1
        break
if ans == -1:
    print(ans)
else:
    i=0
    cur = 0
    while i<=len(boxes)-1:
        j=0
        while (j<=len(crains)-1) and (i<=len(boxes)-1):
            if boxes[i]<=crains[j]:
                i+=1
                j+=1
                cur=i
            else:
                i+=1
        i = cur
        ans+=1
    print(ans)
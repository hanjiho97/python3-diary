import sys
input=sys.stdin.readline

R,C,M=map(int,input().split())
sea=[[0]*C for _ in range(R)]
shark=[]
for i in range(M):
    shark.append(list(map(int,input().split())))
    shark[i][0],shark[i][1]=shark[i][0]-1,shark[i][1]-1
    if R!=1 and (shark[i][3]==1 or shark[i][3]==2): 
        shark[i][2]%=((R-1)*2)
        if shark[i][2]>=R:
            shark[i][2]=2*(R-1)-shark[i][2]
            shark[i][3]=3-shark[i][3]
    elif C!=1 and (shark[i][3]==3 or shark[i][3]==4): 
        shark[i][2]%=((C-1)*2)
        if shark[i][2]>=C:
            shark[i][2]=2*(C-1)-shark[i][2]
            shark[i][3]=7-shark[i][3]
    sea[shark[i][0]][shark[i][1]]=shark[i][4]

dir=[0,(-1,0),(1,0),(0,1),(0,-1)]
def moveall(shark):
    temp=[[0]*C for _ in range(R)]
    idx=0
    while idx<len(shark):
        tar=0
        r,c,s,d,z=shark[idx]
        nr,nc,d=move(r,c,s,d)
        if temp[nr][nc]<z:
            tar=temp[nr][nc]
            temp[nr][nc]=z
            shark[idx][0],shark[idx][1],shark[idx][3]=nr,nc,d
            if tar:
                for i in range(idx):
                    if shark[i][4]==tar: 
                        shark.pop(i)
                        break
                continue
        else: shark.pop(idx); continue
        idx+=1
    return temp

def move(r,c,s,d):
    nr=r+dir[d][0]*s
    nc=c+dir[d][1]*s
    if nr<0:
        nr=-nr
        d=3-d
    elif nr>=R:
        nr=2*(R-1)-nr
        d=3-d
    elif nc<0:
        nc=-nc
        d=7-d
    elif nc>=C:
        nc=2*(C-1)-nc
        d=7-d
    return [nr,nc,d]

def catch(sea, fisherman):
    tar=0
    for i in range(R):
        if sea[i][fisherman[0]]:
            tar=sea[i][fisherman[0]]
            sea[i][fisherman[0]]=0
            fisherman[1]+=tar
            break
    if tar:
        for i in range(len(shark)):
            if shark[i][4]==tar: 
                shark.pop(i)
                break
    return

fisherman=[-1,0]
while fisherman[0]<C-1:
    fisherman[0]+=1
    catch(sea, fisherman)
    sea=moveall(shark)

print(fisherman[1])
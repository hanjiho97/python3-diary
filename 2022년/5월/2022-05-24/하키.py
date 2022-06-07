W,H,X,Y,P=map(int, input().split())
R=H//2
num=0
for _ in range(P):
    x,y=map(int, input().split())
    if X<=x<=X+W and Y<=y<=Y+H: num+=1
    elif (x-X)**2+(y-(Y+R))**2<=R**2: num+=1
    elif (x-(X+W))**2+(y-(Y+R))**2<=R**2: num+=1
print(num)

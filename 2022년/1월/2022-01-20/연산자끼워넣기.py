import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
operator = list(map(int, input().split()))

min = 1000000000
max = -1000000000

def calculate(start, count, plus, minus, multi, divi):
    global max
    global min
    if count==N-1:
        if data[-1]>max:
            max=data[-1]
        if data[-1]<min:
            min=data[-1]
        return
    for i in range(start, len(data)-1):
        a = data[i]
        b = data[i+1]
        if plus:
            data[i+1]+=data[i]
            plus-=1
            calculate(i+1, count+1, plus, minus, multi, divi)
            plus+=1
            data[i]=a
            data[i+1]=b
        if minus:
            data[i+1]=data[i]-data[i+1]
            minus-=1
            calculate(i+1, count+1, plus, minus, multi, divi)
            minus+=1
            data[i]=a
            data[i+1]=b
        if multi:
            data[i+1]*=data[i]
            multi-=1
            calculate(i+1, count+1, plus, minus, multi, divi)
            multi+=1
            data[i]=a
            data[i+1]=b
        if divi:
            if data[i]<0 and data[i+1]>0:
                data[i+1]=-((-data[i])//data[i+1])
            else:
                data[i+1]=data[i]//data[i+1]
            divi-=1
            calculate(i+1, count+1, plus, minus, multi, divi)
            divi+=1
            data[i]=a
            data[i+1]=b
calculate(0, 0, *operator)
print(max)
print(min)
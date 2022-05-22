import sys
input = sys.stdin.readline

sentence=input().rstrip()
while sentence!='.':
    bracket=[]
    for c in sentence:
        if c=='(' or c=='[':
            bracket.append(c)
        elif c==')':
            if not bracket:
                bracket.append(c)
                break
            elif bracket[-1]=='(':
                bracket.pop()
            else:
                break
        elif c==']':
            if not bracket:
                bracket.append(c)
                break
            elif bracket[-1]=='[':
                bracket.pop()
            else:
                break 
    if bracket:
        print('no')
    else:
        print('yes')
    sentence=input().rstrip()
a, b = input().strip().split(' ')
b = int(b)
if len(a)>=1 and len(a)<=10 and b>=1 and b<=5:
    c = a*b
    print(c)
else:
    print("다시")
p=(0,0)

for i in range(1,6):
    values =input().split()
    for j,value in enumerate(values):
        x=int(value)
        if x==1:
            p=(i,j+1)
print(abs(p[0]-3)+abs(p[1]-3))

a=240
b=150
def mapping(x,y):
    LocateX=[240,260,280,300,320,340,360,380]
    LocateY=[170,175,180,185,190,195]
    resultX=[]
    resultY=[]
    for a in LocateX:
        resultX.append((x-a)**2)
    for b in LocateY:
        resultY.append((y-b)**2)
    a=LocateX[resultX.index(min(resultX))]
    b=LocateY[resultY.index(min(resultY))]
    return a,b
    
a,b=mapping(a,b)
print(a,b)

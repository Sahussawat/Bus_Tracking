a=1336
b=240
def Mapping(x,y):
    LocateX=[253 ,285 ,326 ,360 ,415 ,471 ,465 ,516 ,556
            ,604 ,660 ,720 ,776 ,832 ,881 ,884 ,950 ,985
            ,1026,1087,1162,1220,1219,1267,1268,1311,1309
            ,1352,1400,1460,1520,1585,1634,1659,1657,1649
            ,1615,1585,1550,1503,1462,1427,1375,1336,1338,1336]

    LocateY=[172 ,180 ,188 ,195 ,205 ,197 ,215 ,228 ,254
            ,285 ,290 ,292 ,294 ,292 ,268 ,295 ,264 ,213
            ,180 ,164 ,162 ,152 ,168 ,154 ,169 ,154 ,172
            ,163 ,168 ,170 ,167 ,168 ,168 ,181 ,219 ,255 
            ,252 ,255 ,252 ,253 ,252 ,251 ,254 ,248 ,217 ,185]
    resultX=[]
    resultY=[]
    FinalResult =[]
    for a in LocateX:
        resultX.append((x-a)**2)
    for b in LocateY:
        resultY.append((y-b)**2)
    for x in range(len(resultX)):
        FinalResult.append(resultX[x]+resultY[x])
    MappedPositionX=LocateX[FinalResult.index(min(FinalResult))]
    MappedPositionY=LocateY[FinalResult.index(min(FinalResult))]
    return  MappedPositionX,MappedPositionY
    
a,b=Mapping(a,b)
print(a,b)
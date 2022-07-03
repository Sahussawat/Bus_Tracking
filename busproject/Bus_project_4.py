import tkinter as tk
window = tk.Tk() 
window.title("Bus Project")
window.geometry("1862x550") #กำหนดหน้าต่างโปรแกรม 88pixelsสำหรับพื้นที่Buttonต่างๆ

import socket
serverAddressPort = ("udpserver.bu.ac.th", 5005)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
import time

campusImage = tk.PhotoImage(file="MapBu_3.0.png") #1862x422 pixels 
campusMap = tk.Canvas(window, width=campusImage.width(), height=campusImage.height()) #นำเข้ารูปภาพMAP
campusMap.pack()
campusMap.create_image(0, 0, anchor="nw", image=campusImage) #สร้างMAP

mapWidth, mapHeight = 1862, 422     #ความกว้างยาวของpixelsในรูปภาพ
xLeft, xRight = 100.600194, 100.616234   #ตำแหน่งซ้ายสุดและขวาสุดในแนวแกนX
yTop, yBottom = 14.041133, 14.037986     #ตำแหน่งบนสุดและล่างสุดในแนวแกนY

XBusA, YBusA  =  100.603305, 14.039886    #inputจากGPS

BusStop= tk.PhotoImage(file="iconbus_stop.png")  #นำเข้ารูปภาพBusStop

XMapBusA, YMapBusA = (XBusA-xLeft)/0.00000861439, (yTop-YBusA)/0.00000745734   
#สมการการMapping โดยตัวหารของแกนXและYมาจากการเทียบบัญญัติไตรยางค์ของpixel:latitude

Bus1= tk.PhotoImage(file="iconbus.png") #นำเข้ารูปภาพIconBus
Busred= tk.PhotoImage(file="iconbusred.png")
#campusMap.create_image(XMapBusA, YMapBusA-17,image=Bus1) #Simulation ตำแหน่งของรถบัสโดยสมมุติพิกัดขึ้นมาเองครับ
#campusMap.create_image(361, 167-17,image=Bus1) 

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

def update_once():

  campusMap.delete("all")
  campusMap.create_image(0, 0, anchor="nw", image=campusImage)

  messageToSend = str.encode("GET,bus01")
  UDPClientSocket.sendto(messageToSend, serverAddressPort)
  msgFromServer = UDPClientSocket.recvfrom(bufferSize)
  msg = "Message from Server: {}".format(msgFromServer[0])
  print(msg)
  yBus, xBus = float(msg[32:41]), float(msg[52:62])
  X_UnMapBusA, Y_UnMapBusA = (xBus-xLeft)/0.00000861439, (yTop-yBus)/0.00000745734   
  MappedXBusA,MappedYBusA =Mapping(X_UnMapBusA,Y_UnMapBusA)
  campusMap.create_image(X_UnMapBusA-7,Y_UnMapBusA-15,image=Busred)
  campusMap.create_image(MappedXBusA-7,MappedYBusA-15,image=Bus1)

  '''
  messageToSend = str.encode("GET,bus02")
  UDPClientSocket.sendto(messageToSend, serverAddressPort)
  msgFromServer = UDPClientSocket.recvfrom(bufferSize)
  msg = "Message from Server: {}".format(msgFromServer[0])
  print(msg)
  yBus, xBus = float(msg[32:41]), float(msg[52:62])
  X_UnMapBusB, Y_UnMapBusB = (xBus-xLeft)/0.00000861439, (yTop-yBus)/0.00000745734   
  MappedXBusB,MappedYBusB =Mapping(X_UnMapBusB,Y_UnMapBusB)
  campusMap.create_image(MappedXBusB-7,MappedYBusB-15,image=Bus1)
  '''


def update_callback():
  update_once()
  window.after(1500, update_callback)

tk.Button(window, text="update", bg="#dddddd", pady=0, command=update_callback).pack(side="top", fill="x")
'''
campusMap.create_image(253,172-17,image=Bus1)
campusMap.create_image(285,180-17,image=Bus1)
campusMap.create_image(326,188-17,image=Bus1)
campusMap.create_image(360,195-17,image=Bus1)
campusMap.create_image(415,205-17,image=Bus1)
campusMap.create_image(471,197-17,image=Bus1)
campusMap.create_image(465,215-17,image=Bus1)
campusMap.create_image(516,228-17,image=Bus1)
campusMap.create_image(556,254-17,image=Bus1)
campusMap.create_image(604,285-17,image=Bus1)
campusMap.create_image(660,290-17,image=Bus1)
campusMap.create_image(720,292-17,image=Bus1)
campusMap.create_image(776,294-17,image=Bus1)
campusMap.create_image(832,292-17,image=Bus1)
campusMap.create_image(881,268-17,image=Bus1)
campusMap.create_image(884,295-17,image=Bus1)
campusMap.create_image(950,264-17,image=Bus1)
campusMap.create_image(985,213-17,image=Bus1)
campusMap.create_image(1026,180-17,image=Bus1)
campusMap.create_image(1087,164-17,image=Bus1)
campusMap.create_image(1162,162-17,image=Bus1)
campusMap.create_image(1220,152-17,image=Bus1)
campusMap.create_image(1219,168-17,image=Bus1)
campusMap.create_image(1267,154-17,image=Bus1)
campusMap.create_image(1268,169-17,image=Bus1)
campusMap.create_image(1311,154-17,image=Bus1)
campusMap.create_image(1309,172-17,image=Bus1)
campusMap.create_image(1352,163-17,image=Bus1)
campusMap.create_image(1400,168-17,image=Bus1)
campusMap.create_image(1460,170-17,image=Bus1)
campusMap.create_image(1520,167-17,image=Bus1)
campusMap.create_image(1585,168-17,image=Bus1)
campusMap.create_image(1634,168-17,image=Bus1)
campusMap.create_image(1659,181-17,image=Bus1)
campusMap.create_image(1657,219-17,image=Bus1)
campusMap.create_image(1649,255-17,image=Bus1)
campusMap.create_image(1615,252-17,image=Bus1)
campusMap.create_image(1585,255-17,image=Bus1)
campusMap.create_image(1550,252-17,image=Bus1)
campusMap.create_image(1503,253-17,image=Bus1)
campusMap.create_image(1462,252-17,image=Bus1)
campusMap.create_image(1427,251-17,image=Bus1)
campusMap.create_image(1375,254-17,image=Bus1)
campusMap.create_image(1336,248-17,image=Bus1)
campusMap.create_image(1338,217-17,image=Bus1)
campusMap.create_image(1336,185-17,image=Bus1)
'''



def BusStop_Icon(): 
    global BS1,BS2,BS3,BS4,BS5,BS6,BS7,BS8,BS9,BS10,BS11,BS12,BS13 
    #!!!ปัญหาคือการประกาศGlobalตรงนี้มีการขีดเส้นใต้สีเหลือง แต่ทำงานได้ปกติ!!! 
    #ผมคิดว่าอาจจะมีวิธีอื่นในการประกาศตัวแปล แต่ผมไม่รู้Solutionครับ
    BS1=campusMap.create_image(1675,211,image=BusStop)#หน้าม.
    BS2=campusMap.create_image(1585,150,image=BusStop)#หน้าตึกยาว
    BS3=campusMap.create_image(1550,270,image=BusStop)#หน้าตึกเชฟ
    BS4=campusMap.create_image(1375,270,image=BusStop)#หน้าapple
    BS5=campusMap.create_image(1395,150,image=BusStop)#ข้างjarome
    BS6=campusMap.create_image(1155,145,image=BusStop)#หน้าตึกวิศวะ
    BS7=campusMap.create_image(1155,185,image=BusStop)#ตรงข้ามตึกวิศวะ
    BS8=campusMap.create_image(880,250,image=BusStop)#หน้าหอสมุด
    BS9=campusMap.create_image(880,310,image=BusStop)#ตรงข้ามหอสมุด
    BS10=campusMap.create_image(610,265,image=BusStop)#หน้าตึกนิเทศ
    BS11=campusMap.create_image(590,300,image=BusStop)#ตรงข้ามตึกนิเทศ
    BS12=campusMap.create_image(470,177,image=BusStop)#หน้าตึกมีเดีย
    BS13=campusMap.create_image(465,235,image=BusStop)#ตรงข้ามตึกมีเดีย,หน้าสนามบอล
    #ผมคิดว่าน่าจะมีวิธีเขียนที่ดีกว่าcode 13บรรทัดด้านบนนี้
    Button1['state'] = tk.DISABLED #ทำให้ถ้ากดแล้วจะกดอีกไม่ได้ต้องกดRemoveก่อน   
Button1=tk.Button(window, text="BUSSTOP", bg="#dddddd", pady=0,command=lambda:BusStop_Icon()) #สร้างปุ่มBusStop
Button1.pack(side="top",fill="x")    

def Remove_Icon():
    campusMap.itemconfig(BS1,state='hidden')#ซ่อนIconBusStop
    campusMap.itemconfig(BS2,state='hidden')
    campusMap.itemconfig(BS3,state='hidden')
    campusMap.itemconfig(BS4,state='hidden')
    campusMap.itemconfig(BS5,state='hidden')
    campusMap.itemconfig(BS6,state='hidden')
    campusMap.itemconfig(BS7,state='hidden')
    campusMap.itemconfig(BS8,state='hidden')
    campusMap.itemconfig(BS9,state='hidden')
    campusMap.itemconfig(BS10,state='hidden')
    campusMap.itemconfig(BS11,state='hidden')
    campusMap.itemconfig(BS12,state='hidden')
    campusMap.itemconfig(BS13,state='hidden')
    Button1['state'] = tk.NORMAL #ทำให้กดปุ่มBusStopได้อีกครั้งหลังจากRemove
    
tk.Button(window, text="Remove", bg="#dddddd", pady=0, command=Remove_Icon).pack(side="top", fill="x") #สร้างปุ่มRemove
def Exit():
  window.destroy() #จบการทำงาน
tk.Button(window, text="Exit", bg="#dddddd", pady=0, command=Exit).pack(side="top", fill="x") #สร้างปุ่มปิด

window.mainloop()
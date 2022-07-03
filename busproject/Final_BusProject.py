import tkinter as tk
import socket
import time

#สร้างwindow
window = tk.Tk() 
window.title("Bus Project")
window.geometry("1862x550") #กำหนดหน้าต่างโปรแกรม 88pixelsสำหรับพื้นที่Buttonต่างๆ


serverAddressPort = ("udpserver.bu.ac.th", 5005)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.setblocking(0) 

#นำเข้ารูปภาพต่างๆ
campusImage = tk.PhotoImage(file="MapBu_3.0.png") #1862x422 pixels 
campusMap = tk.Canvas(window, width=campusImage.width(), height=campusImage.height()) #นำเข้ารูปภาพMAP
campusMap.pack()
campusMap.create_image(0, 0, anchor="nw", image=campusImage) #สร้างMAP
BusStop= tk.PhotoImage(file="iconbus_stop.png")  #นำเข้ารูปภาพBusStop
Bus1= tk.PhotoImage(file="iconbus.png") #นำเข้ารูปภาพIconBus
Busred= tk.PhotoImage(file="iconbusblue.png") #นำเข้ารูปภาพIconBusสีน้ำเงิน

#สมการสำหรับใช้Mapping
mapWidth, mapHeight = 1862, 422     #ความกว้างยาวของpixelsในรูปภาพ
xLeft, xRight = 100.600194, 100.616234   #ตำแหน่งซ้ายสุดและขวาสุดในแนวแกนX
yTop, yBottom = 14.041133, 14.037986     #ตำแหน่งบนสุดและล่างสุดในแนวแกนY

#Function สำหรับ Mapping จากตำแหน่งสีแดงให้อยู่ในจุดที่กำหนด
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

#Function สำหรับ การUpdate ตำแหน่งของรถบัส
def update_once():
  campusMap.delete("all")                                               #ลบภาพเก่าออกทั้งหมด
  campusMap.create_image(0, 0, anchor="nw", image=campusImage)          #สร้างMapใหม่
  BusStop_Icon()                                                        #สร้างIcon BusStop

  messageToSend = str.encode("GET,bus01")                               #รับmessage จากServer
  UDPClientSocket.sendto(messageToSend, serverAddressPort)
  try: #modified by Poompat                                             #ถ้าสำเร็จจะเกิดการMappingและแสดงผลตำแหน่งของรถบัส
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server: {}".format(msgFromServer[0])
    print(msg)
    yBus, xBus = float(msg[32:41]), float(msg[52:62])
    X_UnMapBusA, Y_UnMapBusA = (xBus-xLeft)/0.00000861439, (yTop-yBus)/0.00000745734   
    MappedXBusA,MappedYBusA =Mapping(X_UnMapBusA,Y_UnMapBusA)
    campusMap.create_image(X_UnMapBusA-7,Y_UnMapBusA-15,image=Busred)
    campusMap.create_image(MappedXBusA-7,MappedYBusA-15,image=Bus1)
  except:                                                               #ถ้าไม่สำเร็จจะปฏิเสธการทำงาน
    print("unable to receive from server")

  messageToSend = str.encode("GET,bus02")                              #รับmessageที่2 จากServer
  UDPClientSocket.sendto(messageToSend, serverAddressPort)
  try: #modified by Poompat                                            #ถ้าสำเร็จจะเกิดการMappingและแสดงผลตำแหน่งของรถบัส
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server: {}".format(msgFromServer[0])
    print(msg)
    yBus, xBus = float(msg[32:41]), float(msg[52:62])
    X_UnMapBusA, Y_UnMapBusA = (xBus-xLeft)/0.00000861439, (yTop-yBus)/0.00000745734   
    MappedXBusA,MappedYBusA =Mapping(X_UnMapBusA,Y_UnMapBusA)
    campusMap.create_image(X_UnMapBusA-7,Y_UnMapBusA-15,image=Busred)
    campusMap.create_image(MappedXBusA-7,MappedYBusA-15,image=Bus1)
  except:                                                              #ถ้าไม่สำเร็จจะปฏิเสธการทำงาน
    print("unable to receive from server")

#Function สำหรับการทำซ้ำการUpdate แบบ Recursive
def update_callback():
  update_once()
  window.after(1500, update_callback)

#สร้างปุ่มสำหรับUpdate
tk.Button(window, text="Start", bg="#dddddd", pady=0, command=update_callback).pack(side="top", fill="x")

#Function สำหรับสร้างIconBusstop
def BusStop_Icon(): 
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

#Function สำหรับจบการทำงานของProgram
def Exit():
  window.destroy() #จบการทำงาน

#สร้างปุ่มสำหรับExit
tk.Button(window, text="Exit", bg="#dddddd", pady=0, command=Exit).pack(side="top", fill="x") #สร้างปุ่มปิด

window.mainloop()
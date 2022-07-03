import tkinter as tk
window = tk.Tk() 
window.title("Bus Project")
window.geometry("1862x500") #กำหนดหน้าต่างโปรแกรม 88pixelsสำหรับพื้นที่Buttonต่างๆ

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

XBusA, YBusA  =  100.612951, 14.039625    #inputจากGPS

BusStop= tk.PhotoImage(file="iconbus_stop.png")  #นำเข้ารูปภาพBusStop
XMapBusA, YMapBusA = (XBusA-xLeft)/0.00000861439, (yTop-YBusA)/0.00000745734   
#สมการการMapping โดยตัวหารของแกนXและYมาจากการเทียบบัญญัติไตรยางค์ของpixel:latitude
Bus1= tk.PhotoImage(file="iconbus.png") #นำเข้ารูปภาพIconBus

#campusMap.create_image(XMapBusA-7, YMapBusA-15,image=Bus1) #Simulation ตำแหน่งของรถบัสโดยสมมุติพิกัดขึ้นมาเองครับ

def update_once():
  campusMap.delete("all")
  campusMap.create_image(0, 0, anchor="nw", image=campusImage)
  messageToSend = str.encode("GET,bus01")
  UDPClientSocket.sendto(messageToSend, serverAddressPort)
  msgFromServer = UDPClientSocket.recvfrom(bufferSize)
  msg = "Message from Server: {}".format(msgFromServer[0])
  print(msg)
  
  yBus, xBus = float(msg[32:39]), float(msg[52:60])
  XMapBusA, YMapBusA = (xBus-xLeft)/0.00000861439, (yBus-YBusA)/0.00000745734   
  campusMap.create_image(XMapBusA-7,YMapBusA-15,image=Bus1)

  messageToSend = str.encode("GET,bus02")
  UDPClientSocket.sendto(messageToSend, serverAddressPort)
  msgFromServer = UDPClientSocket.recvfrom(bufferSize)
  msg = "Message from Server: {}".format(msgFromServer[0])
  print(msg)
  yBus, xBus = float(msg[32:39]), float(msg[52:60])
  XMapBusA, YMapBusA = (xBus-xLeft)/0.00000861439, (yBus-YBusA)/0.00000745734   
  campusMap.create_image(XMapBusA-7,YMapBusA-15,image=Bus1)

def update_callback():
  update_once()
  window.after(5000, update_callback)

tk.Button(window, text="update", bg="#dddddd", pady=0, command=update_callback).pack(side="top", fill="x")

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
    #ผมคิดว่าน่าจะมีวิธีเขียนที่ดีกว่าcode 13บรรทัดด้านบนนี้
    Button1['state'] = tk.DISABLED #ทำให้ถ้ากดแล้วจะกดอีกไม่ได้ต้องกดRemoveก่อน
    
       
Button1=tk.Button(window, text="BUSSTOP", bg="#dddddd", pady=0,command=lambda:BusStop_Icon()) #สร้างปุ่มBusStop
Button1.pack(side="top",fill="x")    


def Exit():
  window.destroy() #จบการทำงาน
tk.Button(window, text="Exit", bg="#dddddd", pady=0, command=Exit).pack(side="top", fill="x") #สร้างปุ่มปิด

window.mainloop()


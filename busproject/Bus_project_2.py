import tkinter as tk
window = tk.Tk() 
window.title("Bus Project")
window.geometry("1862x500") #กำหนดหน้าต่างโปรแกรม 88pixelsสำหรับพื้นที่Buttonต่างๆ

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
#campusMap.create_image(XMapBusA, YMapBusA-17,image=Bus1) #Simulation ตำแหน่งของรถบัสโดยสมมุติพิกัดขึ้นมาเองครับ
#campusMap.create_image(361, 167-17,image=Bus1) 

campusMap.create_image(240,170-17,image=Bus1)
campusMap.create_image(260,175-17,image=Bus1)
campusMap.create_image(280,180-17,image=Bus1)
campusMap.create_image(300,185-17,image=Bus1)
campusMap.create_image(320,185-17,image=Bus1)
campusMap.create_image(340,190-17,image=Bus1)
campusMap.create_image(360,195-17,image=Bus1)
campusMap.create_image(380,195-17,image=Bus1)
campusMap.create_image(400,200-17,image=Bus1)
campusMap.create_image(420,205-17,image=Bus1)
campusMap.create_image(440,210-17,image=Bus1)
campusMap.create_image(470,195-17,image=Bus1)#มี2ตำแหน่ง
campusMap.create_image(470,220-17,image=Bus1)#มี2ตำแหน่ง
campusMap.create_image(490,220-17,image=Bus1)
campusMap.create_image(510,225-17,image=Bus1)
campusMap.create_image(530,235-17,image=Bus1)
campusMap.create_image(550,250-17,image=Bus1)
campusMap.create_image(570,265-17,image=Bus1)
campusMap.create_image(590,280-17,image=Bus1)
campusMap.create_image(610,287-17,image=Bus1)
campusMap.create_image(630,290-17,image=Bus1)
campusMap.create_image(650,290-17,image=Bus1)
campusMap.create_image(670,290-17,image=Bus1)
campusMap.create_image(690,290-17,image=Bus1)
campusMap.create_image(710,290-17,image=Bus1)
campusMap.create_image(730,290-17,image=Bus1)
campusMap.create_image(750,290-17,image=Bus1)
campusMap.create_image(770,290-17,image=Bus1)
campusMap.create_image(790,290-17,image=Bus1)
campusMap.create_image(810,290-17,image=Bus1)
campusMap.create_image(830,290-17,image=Bus1)
campusMap.create_image(850,290-17,image=Bus1)
campusMap.create_image(880,265-17,image=Bus1)#มี2ตำแหน่ง
campusMap.create_image(890,290-17,image=Bus1)#มี2ตำแหน่ง
campusMap.create_image(910,285-17,image=Bus1)
campusMap.create_image(930,275-17,image=Bus1)
campusMap.create_image(950,260-17,image=Bus1)
campusMap.create_image(970,240-17,image=Bus1)
campusMap.create_image(990,210-17,image=Bus1)
campusMap.create_image(1010,195-17,image=Bus1)





def Mapping(positionX,positionY):
    a=1

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
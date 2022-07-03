import tkinter as tk
window = tk.Tk()
window.title("Bus Project")
window.geometry("1862x500")

campusImage = tk.PhotoImage(file="MapBu_3.0.png") #1862x422 pixels
campusMap = tk.Canvas(window, width=campusImage.width(), height=campusImage.height())
campusMap.pack()
campusMap.create_image(0, 0, anchor="nw", image=campusImage)

mapWidth, mapHeight = 1862, 422     #ความกว้างยาวของpixelsในรูปภาพ
xLeft, xRight = 100.600194, 100.616234   #ตำแหน่งซ้ายสุดและขวาสุดในแนวแกนX
yTop, yBottom = 14.041133, 14.037986     #ตำแหน่งบนสุดและล่างสุดในแนวแกนY

XBusA, YBusA  =  100.612578, 14.039902      #inputจากGPS
Count=0
BusStop= tk.PhotoImage(file="iconbus_stop.png")
XMapBusA, YMapBusA = (XBusA-xLeft)/0.00000861439, (yTop-YBusA)/0.00000745734   
#สมการการMapping โดยตัวหารของแกนXและYมาจากการเทียบบัญญัติไตรยางค์ของpixel:latitude
Bus1= tk.PhotoImage(file="iconbus.png")
campusMap.create_image(XMapBusA-7, YMapBusA-15,image=Bus1)

def BusStop_Icon(): 
    global BS1,BS2,BS3,BS4,BS5,BS6,BS7,BS8,BS9,BS10,BS11,BS12,BS13
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
    Button1['state'] = tk.DISABLED #ทำให้ถ้ากดแล้วจะกดอีกไม่ได้ต้องกดRemoveก่อน
    
       
Button1=tk.Button(window, text="BUSSTOP", bg="#dddddd", pady=0,command=lambda:BusStop_Icon()) #สร้างปุ่มBusStop
Button1.pack(side="top",fill="x")    

def Remove_Icon():
    campusMap.delete(BS1)#ลบBusStop
    campusMap.delete(BS2)
    campusMap.delete(BS3)
    campusMap.delete(BS4)
    campusMap.delete(BS5)
    campusMap.delete(BS6)
    campusMap.delete(BS7)
    campusMap.delete(BS8)
    campusMap.delete(BS9)
    campusMap.delete(BS10)
    campusMap.delete(BS11)
    campusMap.delete(BS12)
    campusMap.delete(BS13)
    Button1['state'] = tk.NORMAL #ทำให้กดปุ่มBusStopได้อีกครั้งหลังจากRemove
tk.Button(window, text="Remove", bg="#dddddd", pady=0, command=Remove_Icon).pack(side="top", fill="x") #สร้างปุ่มRemove
def Exit():
  window.destroy() #จบการทำงาน
tk.Button(window, text="Exit", bg="#dddddd", pady=0, command=Exit).pack(side="top", fill="x") #สร้างปุ่มปิด

window.mainloop()

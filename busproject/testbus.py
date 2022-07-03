import tkinter as tk
window = tk.Tk()
window.title("Bus tracking")
campusImage = tk.PhotoImage(file="map.png") #1884x326 pixels
campusMap = tk.Canvas(window, width=campusImage.width(), height=campusImage.height())
campusMap.pack()
campusMap.create_image(0, 0, anchor="nw", image=campusImage)
mapWidth, mapHeight = 1884, 326
xLeft, xRight = 100.600000, 100.616050
yTop, yBottom = 14.040900, 14.038180
xBus, yBus = 100.610343, 14.040406

import socket
serverAddressPort = ("udpserver.bu.ac.th", 5005)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

import time

############################################################################################
def update_once():
  campusMap.delete("all")
  campusMap.create_image(0, 0, anchor="nw", image=campusImage)
  messageToSend = str.encode("GET,bus01")
  UDPClientSocket.sendto(messageToSend, serverAddressPort)
  msgFromServer = UDPClientSocket.recvfrom(bufferSize)
  msg = "Message from Server: {}".format(msgFromServer[0])
  print(msg)
  yBus, xBus = float(msg[30:39]), float(msg[50:60])
  xCircle = (xBus-xLeft)/(xRight-xLeft) * mapWidth
  yCircle = (1 - (yBus-yBottom)/(yTop-yBottom)) * mapHeight
  campusMap.create_oval(xCircle-10, yCircle-10, xCircle+10, yCircle+10, width=2, outline="red", fill="red")

  messageToSend = str.encode("GET,bus02")
  UDPClientSocket.sendto(messageToSend, serverAddressPort)
  msgFromServer = UDPClientSocket.recvfrom(bufferSize)
  msg = "Message from Server: {}".format(msgFromServer[0])
  print(msg)
  yBus, xBus = float(msg[30:39]), float(msg[50:60])
  xCircle = (xBus-xLeft)/(xRight-xLeft) * mapWidth
  yCircle = (1 - (yBus-yBottom)/(yTop-yBottom)) * mapHeight
  campusMap.create_oval(xCircle-10, yCircle-10, xCircle+10, yCircle+10, width=2, outline="blue", fill="blue")

############################################################################################
def update_callback():
  update_once()
  window.after(5000, update_callback)

tk.Button(window, text="update", bg="#dddddd", pady=0, command=update_callback).pack(side="top", fill="x")

#########################################################################
def quit_callback():
  window.destroy()

tk.Button(window, text="quit", bg="#dddddd", pady=0, command=quit_callback).pack(side="top", fill="x")

window.mainloop()

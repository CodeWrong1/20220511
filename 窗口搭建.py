import tkinter

import tkinter as tk

import tkinter.messagebox as msgbox

mainWindow = tk.Tk()
mainWindow.geometry("1000x600+200+100")
mainWindow.title("操作系统")
lblname1 = tk.Label(mainWindow, text="欢迎使用")
lblname1.pack(fill="x", ipady=10)

def btn1_Click():
    msgbox.showinfo("警告", "程序已启动！")

def btn2_Click():
    mainWindow.destroy()

def btn3_Click():
    import serial
    import time
    ser = serial.Serial("COM10", 9600, timeout=50, stopbits=1)
    a = [0x55, 0xAA, 0x03, 0x01, 0x04]
    time.sleep(1)
    result = ser.write(a)
    print("55 AA 03 01 04:", result)
    ser.close()

def btn4_Click():
    import serial
    import time
    ser = serial.Serial("COM10", 9600, timeout=50, stopbits=1)
    b = [0x55, 0xAA, 0x03, 0x00, 0x03]
    time.sleep(1)
    result = ser.write(b)
    print("55 AA 03 00 03:", result)
    ser.close()

def btn5_Click():
    import serial
    import time
    c = entryNummer.get()
    thon = hex(int(c))
    d = int(thon, 16) >> 8
    e = int(thon, 16) & 0xff
    f = 5 + 4 + d + e
    g = [0x55, 0xAA, 0x05, 0x04, d, e, f]

    ser = serial.Serial("COM10", 9600, timeout=50, stopbits=1)
    time.sleep(1)
    result = ser.write(g)
    ser.close()


btn1 = tk.Button(mainWindow, text="打开程序", height=3, width=100, bg="gray", command=btn1_Click)
btn2 = tk.Button(mainWindow, text="关闭程序", height=3, width=100, bg="gray", command=btn2_Click)
btn3 = tk.Button(mainWindow, text="激光启动", height=3, width=100, bg="gray", command=btn3_Click)
btn4 = tk.Button(mainWindow, text="激光关闭", height=3, width=100, bg="gray", command=btn4_Click)
btn5 = tk.Button(mainWindow, text="激光输出", height=3, width=100, bg="gray", command=btn5_Click)

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()

lblname2 = tk.Label(mainWindow, text="输入电流")
lblname2.pack()

entryNummer = tk.Entry(mainWindow)
entryNummer.pack()

mainWindow.mainloop()
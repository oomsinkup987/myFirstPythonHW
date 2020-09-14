import tkinter as tk
from tkinter import ttk
import requests as re
from tkinter.ttk import Combobox
from suds.client import Client
import xml.etree.ElementTree as ET
client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
OilPrice = client.service.CurrentOilPrice(Language='thai')
tree = ET.fromstring(OilPrice)
# ขนาดหน้าต่างโปรแกรม
H = 500
W = 800
root = tk.Tk()
root.title("PTT oil")
var = tk.StringVar()
canvas = tk.Canvas(root, height=H, width=W)
canvas.pack()
# ขนาดของ frame
frame2 = tk.Frame(root, bg='gray', bd=5)
frame2.place(relx=0.19, rely=0.01, relwidth=0.30, relheight=0.55, anchor='n')

# label สำหรับการแสดงข้อมูลน้ำมัน
labe_oil = tk.Label(frame2, text='Gasoline 95 price 29.16\nGasoline 91 price 25.30\nGasohol 91 price 21.68\n Gasohol E20 price 20.2\nGasohol 95 price 21.2\nDiesel price 21.1', font=(
    'Courier', 14), fg='white', bg='orange')
labe_oil.pack(side=tk.TOP)
choice = tk.Label(frame2, text="Choose type", fg="black",
                  bg="pink", font=('Courier', 15)).pack(side=tk.TOP)
# ComboBox สำหรับการเลือกประเภทที่ต้องการแปลงค่า
cbo_oil = ttk.Combobox(
    frame2, values=['Money to Oil', 'Oil to Money'], font=('', 20))
cbo_oil.pack(side=tk.TOP)

mlabel = tk.Label(frame2, text="Money or Litre:", fg="pink",
                  bg="black", font=('Courier', 15)).pack(side=tk.TOP)

# ใส่จำนวณ เงิน หรือ จำนวณลิตรที่ต้องการแปลงค่า
entry = tk.Entry(frame2, font=('Courier', 20))
entry.pack(side=tk.TOP)

oillabel = tk.Label(frame2, text="Oiltype:", fg="orange",
                    bg="black", font=('Courier', 15)).pack(side=tk.TOP)
# ComboBox สำหรับเลือกชนิดของน้ำมัน
oiltype = ttk.Combobox(frame2, values=['Gasoline 95', 'Gasoline 91',
                                       'Gasohol 91', 'Gasohol E20', 'Gasohol 95', 'Diesel'], font=('', 15))
oiltype.pack(side=tk.TOP)
# ปุ่ม
button = tk.Button(frame2, text='Enter', font=(
    "", 15), command=lambda: func_Oil())
button.pack(side=tk.TOP)

button3 = tk.Button(frame2, text='Reset', font=(
    "", 15), command=lambda: clear())
button3.pack(side=tk.TOP)

# Function สำหรับปุ่ม Reset
def clear():
    cbo_oil.set('')
    entry.delete(0, 'end')
    oiltype.delete(0, 'end')
    prt.set('')


prt = tk.StringVar()

# Function การคำนวณ
def func_Oil():
    cbo = str(cbo_oil.get())
    a = str(oiltype.get())
# เงื่อนไข สำหรับการคำนวณจาก เงิน แปลงเป็นลิตร
    if cbo == 'Money to Oil':
        if a == 'Gasoline 95':
            price = int(entry.get()) / 29.16
            prt.set("Litre: %.2f" % price,)
        elif a == 'Gasoline 91':
            price = int(entry.get()) / 25.30
            prt.set("Litre: %.2f" % price,)
        elif a == 'Gasohol 91':
            price = int(entry.get()) / 21.68
            prt.set("Litre: %.2f" % price,)
        elif a == 'Gasohol E20':
            price = int(entry.get()) / 20.2
            prt.set("Litre: %.2f" % price,)
        elif a == 'Gasohol 95':
            price = int(entry.get()) / 21.2
            prt.set("Litre: %.2f" % price,)
        elif a == 'Diesel':
            price = int(entry.get()) / 21.1
            prt.set("Litre: %.2f" % price,)
    # เงื่อนไข สำหรับการคำนวณจากลิตรแปลงเป็นเงิน
    if cbo == 'Oil to Money':
        if a == 'Gasoline 95':
            price = int(entry.get()) * 29.16
            prt.set("Pay: %.2f" % price,)
        elif a == 'Gasoline 91':
            price = int(entry.get()) * 25.30
            prt.set("Pay: %.2f" % price,)
        elif a == 'Gasohol 91':
            price = int(entry.get()) * 21.68
            prt.set("Pay: %.2f" % price,)
        elif a == 'Gasohol E20':
            price = int(entry.get()) * 20.2
            prt.set("Pay: %.2f" % price,)
        elif a == 'Gasohol 95':
            price = int(entry.get()) * 21.2
            prt.set("Pay: %.2f" % price,)
        elif a == 'Diesel':
            price = int(entry.get()) * 21.1
            prt.set("Pay: %.2f" % price,)

#Frame ที่สองสำหรับแสดงค่าที่คำนวณ และ แสดงข้อมูลที่ดึงมาจาก Website
lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.67, rely=0.01, relwidth=0.6,
                  relheight=0.9, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18),
                 anchor='nw', justify='left')
label.place(relwidth=1, relheight=1)

#Label สำหรับแสดง ค่าที่คำนวณ
f3_l2 = tk.Label(lower_frame, textvariable=prt)
f3_l2.config(font=("", 24))
f3_l2.pack()

ol = tk.StringVar()
li = ""
for kirito in tree:
    oil = ""
    for i in kirito:
        oil += i.text + " \t "
        li += oil + "\n"
#Label สำหรับแสดงข้อมูลที่ดึงมาจาก Website
ol.set(li)
pr3 = tk.Label(lower_frame, textvariable=ol)
pr3.config(font=("", 14))
pr3.place(relx=0.50, rely=0.10, anchor='n')

button2 = tk.Button(frame2, text='Close', font=("", 15), command=root.destroy)
button2.pack(side=tk.TOP)
root.mainloop()

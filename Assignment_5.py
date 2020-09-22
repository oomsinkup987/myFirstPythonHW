import json  # import json เข้ามาใช้แปลงจาก Dict เป็น json
import xmltodict  # แปลง xml ให้เป็น Dict
import subprocess as sp
from suds.client import Client  # เข้าไปอ่านไฟล์จาก Website
import os
client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
OilPrice = client.service.CurrentOilPrice(Language='thai')
OilPrice1 = xmltodict.parse(OilPrice)
Price = eval(json.dumps(OilPrice1))
op = dict()
w, h = os.get_terminal_size()
print(w, h)


def func():
    # แสดงข้อมูลราคาและชนิดน้ำมัน
    sp.call('clear', shell=True)
    oil_li = [{"name": "1.Gasoline 95  ","price": 29.16},
          {"name": "2.Gasoline 91  ", "price": 25.30},
          {"name": "3.Gassohol 91  ", "price": 21.68},
          {"name": "4.Gassohol E20 ", "price": 20.20},
          {"name": "5.Gassohol 95  ", "price": 21.00},
          {"name": "6.Gassohol 95  ", "price": 21.10}]


    sp.run('', shell=True)
    print("#"*int(w-1))
    for oil in Price.get("PTTOR_DS").get("FUEL"):
        if(oil.get("PRICE_DATE").split()[0].split("/")[2] == "2020"):
            op[oil.get("PRODUCT")] = oil.get("PRICE")
            pn = (list(oil.values())[1:3])
            ps = str(pn)
        print("" + "#" + (" " *int((w//2.5))) +'\0337', end="")
        print(" " * int((w//1.70)) + "#" + '\0338', end="")
        print(ps)
    print(("#"*int(w - 1)) + "\n")
    print("#"*int(w - 1))
    for y in oil_li:
        a = "Oiltype: " + y["name"]+"\tprice: "+"%.2f"%(y["price"])
        print("#" + (" " *int((w // 2.5))) +'\0337' , end="")
        print(" " * int((w // 1.7)) + "#" + '\0338' , end="")
        print(a)
    print("#"*int(w-1))
    typ = print(int(input("Choose Type Oil: ")))

    print("#"*int(w-1))
    s1 = str("Function: 1.Money to Litre or 2.Litre to Money")
    print("#"+ (" " *int((w//3))) +'\0337' ,end="")
    print(" " * int((w//1.54)) + "#" + '\0338' ,end="")
    print(s1)
    print("#"*int(w-1))
    f = int(input(" Choose Function: "))
    # วนลูปการทำงานค่าน้ำมัน
    if typ == 1:
        if f == 1:
            x1(29.16)
        else:
            x2(29.16)
    elif typ == 2:
        if f == 1:
            x1(25.30)
        else:
            x2(25.30)
    elif typ == 3:
        if f == 1:
            x1(21.68)
        else:
            x2(21.68)
    elif typ == 4:
        if f == 1:
            x1(20.2)
        else:
            x2(20.2)
    elif typ == 5:
        if f == 1:
            x1(21.2)
        else:
            x2(21.2)
    else:
        if f == 1:
            x1(21.1)
        else:
            x2(21.1)


def x1(i):
    print("#"* int(w - 1))
    print("#" + (" " *int((w// 2.5))) +'\0337' , end="")
    print(" " * int((w// 1.7)) + "#" + '\0338' , end="")
    oil = float(input("PRICE (BAHT):"))
    print("#" + (" " *int((w// 2.5))) +'\0337' , end="")
    print(" " * int((w//1.7)) + "#" + '\0338' , end="")
    print(" BAHT = ", ' %.2f ' %
          (oil / i), 'LITER')
    print("#"*int(w-1))


def x2(i):
    print("#"*int(w-1))
    print("#" + (" " *int((w//2.5))) +'\0337' ,end="")
    print(" " * int((w//1.7)) + "#" + '\0338' ,end="")
    oil = float(input("OIL (Litre):"))
    print("#" + (" " *int((w//2.5))) +'\0337' ,end="")
    print(" " * int((w//1.7)) + "#" + '\0338' ,end="")
    print(" BAHT = ", ' %.2f ' %
          (oil * i), 'LITER')
    print("#"*int(w-1))


while True:
    a = str(input("Continue or Exit:"))
    if a == "Exit":
        break
    else:
        func()
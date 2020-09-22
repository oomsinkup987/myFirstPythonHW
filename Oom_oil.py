import json  # import json เข้ามาใช้แปลงจาก Dict เป็น json
import xmltodict  # แปลง xml ให้เป็น Dict
import subprocess as sp
from suds.client import Client # เข้าไปอ่านไฟล์จาก Website
client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
OilPrice = client.service.CurrentOilPrice(Language='thai')
OilPrice1 = xmltodict.parse(OilPrice)
Price = eval(json.dumps(OilPrice1))
op = dict()
for oil in Price.get("PTTOR_DS").get("FUEL"):
    if(oil.get("PRICE_DATE").split()[0].split("/")[2] == "2020"):
        op[oil.get("PRODUCT")] = oil.get("PRICE")

def func():
    # แสดงข้อมูลราคาและชนิดน้ำมัน
    sp.call('clear', shell=True)
    oil_li = [{"name": "1.Gasoline 95 ","price": 29.16},
          {"name": "2.Gasoline 91  ","price": 25.30},
          {"name": "3.Gassohol 91  ","price": 21.68},
          {"name": "4.Gassohol E20 ","price": 20.20},
          {"name": "5.Gassohol 95  ","price": 21.00},
          {"name": "6.Gassohol 95  ","price": 21.10}]


    sp.run('', shell=True)
    print("#"*80)
    for oil in Price.get("PTTOR_DS").get("FUEL"):
        if(oil.get("PRICE_DATE").split()[0].split("/")[2] == "2020"):
            op[oil.get("PRODUCT")] = oil.get("PRICE")
            pn = (list(oil.values())[1:3])
            ps = str(pn)
        print("#"+" " *int(56/2)+" \0337" + " " * int(99/2) + "#",end="")
        print("\n"+ '#' * 80 + '\0338',end="")
        print(ps)
    for t in range(3):
        print("#" +" " * 78 + "#")
    for i in oil_li:
        a = "Oiltype: " + i["name"]+"\tprice: \t"+"%.2f"%(i["price"])
        if (int(len(a)/2) != len(a)/2):
            a1,a2 = len(a)/2 - 1, len(a)/2
        else:
            a1,a2 = len(a)/2, len(a)/2

        print("#"+(" " * int(72/2 - a1)) + a + (" " * int(72/2 - a2)) + "#")
        print("#" +" " * 78 + "#")
        print("#" +" " * 78 + "#")
    print("#"+" " * int(44/2) + "1. Litre to Money 2. Money to Litre" + " " * int(43/2)+"#")
    print("#"+" " *int(56/2)+" \0337" + " " * int(99/2) + "#",end="")
    print("\n"+ '#' * 80 + '\0338',end="")      

    typ = int(input(">>>Choose list : "))

    print("#"*120)
    for k in range(4):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 55) + "Function" + (" " * 55) + "#")
    print("#" + (" " * 47) + "1.Price  ------>   Liter" + (" " * 47) + "#")
    print("#" + (" " * 47) + "2.Liter   ------>  Price" + (" " * 47) + "#")
    for k in range(4):
        print("#" + (" " * 118) + "#")
    print("#"*120)
    fc1 = int(input(">>>Choose function : "))
    # วนลูปการทำงานค่าน้ำมัน
    if typ == 1:
        if fc1 == 1:
            x1(29.16)
        else:
            x2(29.16)
    elif typ == 2:
        if fc1 == 1:
            x1(25.30)
        else:
            x2(25.30)
    elif typ == 3:
        if fc1 == 1:
            x1(21.68)
        else:
            x2(21.68)
    elif typ == 4:
        if fc1 == 1:
            x1(20.2)
        else:
            x2(20.2)
    elif typ == 5:
        if fc1 == 1:
            x1(21.2)
        else:
            x2(21.2)
    else:
        if fc1 == 1:
            x1(21.1)
        else:
            x2(21.1)

def x1(i):
    print("#"*120)
    for k in range(3):
        print("#" + (" " * 118) + "#")
    oil = float(
        input("#" + (" " * int(115/2)) + "PRICE (BAHT):"))
    for k in range(3):
        print("#" + (" " * 118) + "#")
    print("#"*120)

    print("#"*120)
    for k in range(3):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + " BAHT = ", ' %.2f ' %
          (oil / i), 'LITER' + (" " * 52) + "#")
    for k in range(3):
        print("#" + (" " * 118) + "#")
    print("#"*120)


def x2(i):
    print("#"*120)
    for k in range(3):
        print("#" + (" " * 118) + "#")
    oil = float(
        input("#" + (" " * int(115/2)) + "LITER (BATH): "))

    for k in range(3):
        print("#" + (" " * 118) + "#")
    print("#"*120)

    print("#"*120)
    for k in range(3):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + " LITER = ", ' %.2f ' %
          (oil * i,), ' BATH' + (" " * 48) + "#")
    for k in range(3):
        print("#" + (" " * 118) + "#")
    print("#"*120)


while True:
    a = str(input("Continue or Exit:"))
    if a == "Exit":
        break
    else:
        func()
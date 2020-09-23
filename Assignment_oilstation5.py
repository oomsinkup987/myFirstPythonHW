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


def func_main():
    # แสดงข้อมูลราคาและชนิดน้ำมัน
    sp.call('clear', shell=True)
    oil_li = [{"name": "1.Gasoline 95  ", "price": 29.16},
              {"name": "2.Gasoline 91  ", "price": 25.30},
              {"name": "3.Gassohol 91  ", "price": 21.68},
              {"name": "4.Gassohol E20 ", "price": 20.20},
              {"name": "5.Gassohol 95  ", "price": 21.00},
              {"name": "6.Gassohol 95  ", "price": 21.10}]

    sp.run('', shell=True)
    space_up()
    for oil in Price.get("PTTOR_DS").get("FUEL"):
        if(oil.get("PRICE_DATE").split()[0].split("/")[2] == "2020"):
            op[oil.get("PRODUCT")] = oil.get("PRICE")
            pn = (list(oil.values())[1:3])
            ps = str(pn)
        print("" + "#" + (" " * int((w//2.5))) + '\0337', end="")
        print(" " * int((w//1.70)) + "#" + '\0338', end="")
        print(ps)
    space_down()
    space_up()
    for y in oil_li:
        a = y["name"]+"price: "+"%.2f" % (y["price"])
        print("#" + (" " * int((w // 2.5))) + '\0337', end="")
        print(" " * int((w // 1.7)) + "#" + '\0338', end="")
        print(a)
    space_down()
    canvas_1()
    typ = int(input("Choose Type Oil: "))
    space_down()
    canvas_1()
    print("Function: 1.Money to Litre\n" + "#"+(" "*int(w//2.44) ) + "2.Litre to Money")
    space_down() 

    canvas_1()
    f = int(input(" Choose Function: "))
    space_down()
    # วนลูปการทำงานค่าน้ำมัน
    if typ == 1:
        if f == 1:
            func_1(29.16)
        else:
            func_2(29.16)
    elif typ == 2:
        if f == 1:
            func_1(25.30)
        else:
            func_2(25.30)
    elif typ == 3:
        if f == 1:
            func_1(21.68)
        else:
            func_2(21.68)
    elif typ == 4:
        if f == 1:
            func_1(20.2)
        else:
            func_2(20.2)
    elif typ == 5:
        if f == 1:
            func_1(21.2)
        else:
            func_2(21.2)
    else:
        if f == 1:
            func_1(21.1)
        else:
            func_2(21.1)


def func_1(i):
    canvas_1()
    money = float(input("Money (BAHT):"))
    print("#" + (" " * int((w // 2.8))) + " Oil = ", ' %.2f ' %
          (money / i), 'Litre')
    space_down()


def func_2(i):
    canvas_1()
    oil = float(input("OIL (Litre):"))
    print("#" + (" " * int((w // 2.8))) + " BAHT = ", ' %.2f ' %
          (oil * i), 'BAHT')
    space_down()


def space_up():    
    print("#"*int(w))
    for can in range(2):
        print("#" + (" "*int(w-2)) + "#")


def space_down():    
    for can in range(2):
        print("#" + (" "*int(w-2)) + "#")
    print("#"*int(w))


def canvas_1():
    space_up()
    print("#" + (" " * int((w//2.5))) + '\0337', end="")
    print(" " * int((w//1.7)) + "#" + '\0338', end="")


while True:
    a = str(input("Continue or Exit:"))
    if a == "Exit":
        break
    else:
        func_main()
import json
import xmltodict
from suds.client import Client
client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
OilPrice = client.service.CurrentOilPrice(Language='thai')
# หากต้องการใช้ GetOilPrice ให้แก้เป็น
# client.service.GetOilPrice(รายละเอียดตามเอกสาร)
OilPrice1 = xmltodict.parse(OilPrice)  # ได้ผลลัพธ์เป็น json ในสตริง
Price = eval(json.dumps(OilPrice1))  # เรียกใช้งาน json ในสตริง
# คำนวนค่าน้ำมัน


def main_func():
    # เมนูหลัก
    op = dict()
    for Nummun in Price.get("PTTOR_DS").get("FUEL"):
        if(Nummun.get("PRICE_DATE").split()[0].split("/")[2] == "2020"):
            op[Nummun.get("PRODUCT")] = Nummun.get("PRICE")
            li_oil = (list(Nummun.values())[1:3])
            st_oil = str(li_oil)
        print(li_oil)
    print("#"*120)
    for k in range(3):
        print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + "HELLO THIS IS GAS STATION" + (" " * 48) + "#")
    for k in range(3):
        print("#" + (" " * 118) + "#")
    print("#"*120)


    oiltyp = 0
    print("#"*120)
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 57) + "list" + (" " * 57) + "#")
    print("#" + (" " * 40) + "1.Gasoline 95     ราคา   29.16  BATH" + (" " * 42) + "#")
    print("#" + (" " * 40) + "2.Gasoline 91     ราคา   25.30  BATH" + (" " * 42) + "#")
    print("#" + (" " * 40) + "3.Gasohol  91     ราคา   21.68  BATH" + (" " * 42) + "#")
    print("#" + (" " * 40) + "4.Gasohol  E20    ราคา   20.2   BATH" + (" " * 42) + "#")
    print("#" + (" " * 40) + "5.Gasohol  95     ราคา   21.2   BATH" + (" " * 42) + "#")
    print("#" + (" " * 40) + "6.Diesel          ราคา   21.1   BATH" + (" " * 42) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#"*120)

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
        main_func()
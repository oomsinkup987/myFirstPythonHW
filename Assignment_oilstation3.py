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
    oil_li = [{"name": "Gasoline 95 ","price": 29.16},
          {"name": "Gasoline 91 ","price": 25.30},
          {"name": "Gassohol 91 ","price": 21.68},
          {"name": "Gassohol E20","price": 20.20},
          {"name": "Gassohol 95 ","price": 21.00},
          {"name": "Gassohol 95 ","price": 21.10}]


    sp.run('', shell=True)
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

        print("#"+" " * int(72/2 - a1) + a + " " * int(72/2 - a2)+"#")
        print("#" +" " * 78 + "#")
        print("#" +" " * 78 + "#")
    print("#"+" " * int(44/2) + "1. Litre to Money 2. Money to Litre" + " " * int(43/2)+"#")
    print("#"+" " *int(56/2)+" \0337" + " " * int(99/2) + "#",end="")
    print("\n"+ '#' * 80 + '\0338',end="")      
    t = int(input('เลือกประเภทที่ต้องการคำนวณ:'))
    print('#' * 80)
    a = 'Gasoline95'
    b = 'Gasoline91'
    c = 'Gasohol91'
    d = 'GasoholE20'
    e = 'Gasohol95'
    f = 'Diesel'
    # เงื่อนไข สำหรับการคำนวณจากเงินแปลงเป็นลิตร
    if t == 1:
        price_in = int(input("ใส่จำนวณเงิน: ").strip())
        oiltype = input("OilType: ").split(" ")
        print("#"*80)
        for ot in oiltype:
            if ot == a:
                price = price_in / 29.16
                for k in range(5):
                    print("#"+(" "*78)+"#")
                print("#"+(" "*25)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*35)+"#")
                for k in range(5):
                    print("#"+(" "*78)+"#")
            elif ot == b:
                price = price_in / 25.30
                for k in range(5):
                    print("#"+(" "*78)+"#")
                print("#"+(" "*25)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*35)+"#")
                for k in range(5):
                    print("#"+(" "*78)+"#")
            elif ot == c:
                price = price_in / 21.68
                for k in range(5):
                    print("#"+(" "*78)+"#")
                print("#"+(" "*25)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*35)+"#")
                for k in range(5):
                    print("#"+(" "*78)+"#")
            elif ot == d:
                price = price_in / 20.2
                for k in range(5):
                    print("#"+(" "*78)+"#")
                print("#"+(" "*25)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*35)+"#")
                for k in range(5):
                    print("#"+(" "*78)+"#")
            elif ot == e:
                price = price_in / 21.2
                for k in range(5):
                    print("#"+(" "*78)+"#")
                print("#"+(" "*25)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*35)+"#")
                for k in range(5):
                    print("#"+(" "*78)+"#")
            elif ot == f:
                price = price_in / 21.1
                for k in range(5):
                    print("#"+(" "*78)+"#")
                print("#"+(" "*25)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*35)+"#")
                for k in range(5):
                    print("#"+(" "*78)+"#")
            else:
                print('Error')
    # เงื่อนไข สำหรับการคำนวณจากลิตรแปลงเป็นเงิน
    if t == 2:
        Oil_in = int(input("ใส่จำนวณลิตร: ").strip())
        oiltype = input("OilType: ").split(" ")
        print("#"*80)
        for ot in oiltype:
            if ot == a:
                price = Oil_in * 29.16
                for k in range(5):
                    print("#"+(" "*78)+"#")
                print("#"+(" "*25)+'จำนวณเงิน %.2f' %
                      (price), 'BAHT'+(" "*31)+"#")
                for k in range(5):
                    print("#"+(" "*78)+"#")
            elif ot == b:
                price = Oil_in * 25.30
                for k in range(5):
                    print("#"+(" "*78)+"#")
                print("#"+(" "*25)+'จำนวณเงิน %.2f' %
                      (price), 'BAHT'+(" "*31)+"#")
                for k in range(5):
                    print("#"+(" "*78)+"#")
            elif ot == c:
                price = Oil_in * 21.68
                for k in range(5):
                    print("#"+(" "*78)+"#")
                print("#"+(" "*25)+'จำนวณเงิน %.2f' %
                      (price), 'BAHT'+(" "*31)+"#")
                for k in range(5):
                    print("#"+(" "*78)+"#")
            elif ot == d:
                price = Oil_in * 20.2
                for k in range(5):
                    print("#"+(" "*78)+"#")
                print("#"+(" "*25)+'จำนวณเงิน %.2f' %
                      (price), 'BAHT'+(" "*31)+"#")
                for k in range(5):
                    print("#"+(" "*78)+"#")
            elif ot == e:
                price = Oil_in * 21.2
                for k in range(5):
                    print("#"+(" "*78)+"#")
                print("#"+(" "*25)+'จำนวณเงิน %.2f' %
                      (price), 'BAHT'+(" "*31)+"#")
                for k in range(5):
                    print("#"+(" "*34)+"#")
            elif ot == f:
                price = Oil_in * 21.1
                for k in range(5):
                    print("#"+(" "*78)+"#")
                print("#"+(" "*25)+'จำนวณเงิน %.2f' %
                      (price), 'BAHT'+(" "*31)+"#")
                for k in range(5):
                    print("#"+(" "*78)+"#")
            else:
                print('Error')

    print("#"*80)
    input(" Press Enter to continue...")


# loop สำหรับการทำซ้ำใหม่
while True:
    func()

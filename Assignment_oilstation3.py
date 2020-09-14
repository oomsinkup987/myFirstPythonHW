import json # import json เข้ามาใช้แปลงจาก Dict เป็น json
import xmltodict # แปลง xml ให้เป็น Dict
from suds.client import Client
client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')# เข้าไปอ่านไฟล์จาก Website
OilPrice = client.service.CurrentOilPrice(Language='thai')
OilPrice1 = xmltodict.parse(OilPrice)
Price = eval(json.dumps(OilPrice1))
op = dict()
for oil in Price.get("PTTOR_DS").get("FUEL"):
    if(oil.get("PRICE_DATE").split()[0].split("/")[2] == "2020"):
        op[oil.get("PRODUCT")] = oil.get("PRICE")
    print(op)


def func():
    # แสดงข้อมูลราคาและชนิดน้ำมัน
    print("#"*50)
    for i in range(2):
        print("#"+(" "*48)+"#")
    print("#"+(" "*15)+'Gasoline95 price 29.16'+(" "*20)+"#")
    for i in range(2):
        print("#"+(" "*48)+"#")
    print("#"+(" "*15)+'Gasoline95 price 29.16'+(" "*20)+"#")
    for i in range(2):
        print("#"+(" "*48)+"#")
    print("#"+(" "*15)+'Gasoline95 price 29.16'+(" "*20)+"#")
    for i in range(2):
        print("#"+(" "*48)+"#")
    print("#"+(" "*15)+'Gasoline95 price 29.16'+(" "*20)+"#")
    for i in range(2):
        print("#"+(" "*48)+"#")
    print("#"+(" "*15)+'Gasoline95 price 29.16'+(" "*20)+"#")
    for i in range(2):
        print("#"+(" "*48)+"#")
    print("#"+(" "*15)+'Gasoline95 price 29.16'+(" "*20)+"#")
    for i in range(2):
        print("#"+(" "*48)+"#")
    print("#"*50)
    print("#"*112)
    for i in range(8):
        print("#"+(" "*110)+"#")
    # เลือกประเภทที่ต้องการคำนวณ
    print("#" + (" " * 25) +
          'เลือกว่าจะคำนวณจากเงินเป็นลิตรพิม 1 หรือ จำนวณลิตรเป็นเงินพิม 2' +
          (" "*33) + "#")
    for i in range(8):
        print("#"+(" "*110)+"#")
    print("#"*112)
    t = int(input('เลือกประเภทที่ต้องการคำนวณ:'))
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
        print("#"*112)
        for ot in oiltype:
            if ot == a:
                price = price_in / 29.16
                for k in range(5):
                    print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*44)+"#")
                for k in range(5):
                    print("#"+(" "*110)+"#")
            elif ot == b:
                price = price_in / 25.30
                for k in range(5):
                    print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*44)+"#")
                for k in range(5):
                    print("#"+(" "*110)+"#")
            elif ot == c:
                price = price_in / 21.68
                for k in range(5):
                    print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*44)+"#")
                for k in range(5):
                    print("#"+(" "*110)+"#")
            elif ot == d:
                price = price_in / 20.2
                for k in range(5):
                    print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*44)+"#")
                for k in range(5):
                    print("#"+(" "*110)+"#")
            elif ot == e:
                price = price_in / 21.2
                for k in range(5):
                    print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*44)+"#")
                for k in range(5):
                    print("#"+(" "*110)+"#")
            elif ot == f:
                price = price_in / 21.1
                for k in range(5):
                    print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*44)+"#")
                for k in range(5):
                    print("#"+(" "*110)+"#")
            else:
                print('Error')
    # เงื่อนไข สำหรับการคำนวณจากลิตรแปลงเป็นเงิน            
    if t == 2:
        Oil_in = int(input("#"+(" "*15)+"ใส่จำนวณลิตร: ").strip())
        oiltype = input("OilType: ").split(" ")
        print("#"*112)
        for ot in oiltype:
            if ot == a:
                price = Oil_in * 29.16
                for k in range(5):
                    print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณเงิน %.2f' %
                      (price), 'BAHT'+(" "*44)+"#")
                for k in range(5):
                    print("#"+(" "*110)+"#")
            elif ot == b:
                price = Oil_in * 25.30
                for k in range(5):
                    print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณเงิน %.2f' %
                      (price), 'BAHT'+(" "*44)+"#")
                for k in range(5):
                    print("#"+(" "*110)+"#")
            elif ot == c:
                price = Oil_in * 21.68
                for k in range(5):
                    print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณเงิน %.2f' %
                      (price), 'BAHT'+(" "*43)+"#")
                for k in range(5):
                    print("#"+(" "*110)+"#")
            elif ot == d:
                price = Oil_in * 20.2
                for k in range(5):
                    print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณเงิน %.2f' %
                      (price), 'BAHT'+(" "*43)+"#")
                for k in range(5):
                    print("#"+(" "*110)+"#")
            elif ot == e:
                price = Oil_in * 21.2
                for k in range(5):
                    print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณเงิน %.2f' %
                      (price), 'BAHT'+(" "*43)+"#")
                for k in range(5):
                    print("#"+(" "*110)+"#")
            elif ot == f:
                price = Oil_in * 21.1
                for k in range(5):
                    print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณเงิน %.2f' %
                      (price), 'BAHT'+(" "*43)+"#")
                for k in range(5):
                    print("#"+(" "*110)+"#")
            else:
                print('Error')

    print("#"*112)
    input(" Press Enter to continue...")


# loop สำหรับการทำซ้ำใหม่
while True:
    func()

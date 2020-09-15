import json  # import json เข้ามาใช้แปลงจาก Dict เป็น json
import xmltodict  # แปลง xml ให้เป็น Dict
from suds.client import Client
# เข้าไปอ่านไฟล์จาก Website
client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
OilPrice = client.service.CurrentOilPrice(Language='thai')
OilPrice1 = xmltodict.parse(OilPrice)
Price = eval(json.dumps(OilPrice1))
op = dict()
for oil in Price.get("PTTOR_DS").get("FUEL"):
    if(oil.get("PRICE_DATE").split()[0].split("/")[2] == "2020"):
        op[oil.get("PRODUCT")] = oil.get("PRICE")
        print(list(oil.values())[1:3])


def func():
    # แสดงข้อมูลราคาและชนิดน้ำมัน
    print("#"*80)
    for i in range(2):
        print("#"+(" "*78)+"#")
    print("#"+(" "*27)+'Gasoline95 price 29.16'+(" "*29)+"#")
    for i in range(2):
        print("#"+(" "*78)+"#")
    print("#"+(" "*27)+'Gasoline95 price 29.16'+(" "*29)+"#")
    for i in range(2):
        print("#"+(" "*78)+"#")
    print("#"+(" "*27)+'Gasoline95 price 29.16'+(" "*29)+"#")
    for i in range(2):
        print("#"+(" "*78)+"#")
    print("#"+(" "*27)+'Gasoline95 price 29.16'+(" "*29)+"#")
    for i in range(2):
        print("#"+(" "*78)+"#")
    print("#"+(" "*27)+'Gasoline95 price 29.16'+(" "*29)+"#")
    for i in range(2):
        print("#"+(" "*78)+"#")
    print("#"+(" "*27)+'Gasoline95 price 29.16'+(" "*29)+"#")
    for i in range(2):
        print("#"+(" "*78)+"#")
    print("#"*80)
    print("#"*80)
    for i in range(8):
        print("#"+(" "*78)+"#")
    # เลือกประเภทที่ต้องการคำนวณ
    print("#" + (" " * 10) +
          'เลือกว่าจะคำนวณจากเงินเป็นลิตรพิม 1 หรือ จำนวณลิตรเป็นเงินพิม 2' +
          (" "*16) + "#")
    for i in range(8):
        print("#"+(" "*78)+"#")
    print("#"*80)
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

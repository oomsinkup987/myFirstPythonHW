def func():
    # ข้อมูลน้ำมัน
    print('Gasoline95 price 29.16')
    print('Gasoline95 price 29.16')
    print('Gasoline95 price 29.16')
    print('Gasoline95 price 29.16')
    print('Gasoline95 price 29.16')
    print('Gasoline95 price 29.16')
    # เลือกประเภทที่ต้องการคำวณ
    print('เลือกว่าจะคำนวณจากเงินเป็นลิตรพิม 1 หรือ จำนวณลิตรเป็นเงินพิม 2')
    t = int(input('เลือกประเภทที่ต้องการคำนวณ:'))
    print
    a = 'Gasoline95'
    b = 'Gasoline91'
    c = 'Gasohol91'
    d = 'GasoholE20'
    e = 'Gasohol95'
    f = 'Diesel'
    # Function สำหรับการคำนวณจากเงินแปลงเป็นลิตร
    if t == 1:
        price_in = int(input("ใส่จำนวณเงิน: ").strip())
        oiltype = input("OilType: ").split(" ")
        for ot in oiltype:
            if ot == a:
                price = price_in / 29.16
                print('จำนวณลิตร %.2f' % (price), 'ลิตร')
            elif ot == b:
                price = price_in / 25.30
                print('จำนวณลิตร %.2f' % (price), 'ลิตร')
            elif ot == c:
                price = price_in / 21.68
                print('จำนวณลิตร %.2f' % (price), 'ลิตร')
            elif ot == d:
                price = price_in / 20.2
                print('จำนวณลิตร %.2f' % (price), 'ลิตร')
            elif ot == e:
                price = price_in / 21.2
                print('จำนวณลิตร %.2f' % (price), 'ลิตร')
            elif ot == f:
                price = price_in / 21.1
                print('จำนวณลิตร %.2f' % (price), 'ลิตร')
            else:
                print('Error')
    # Function สำหรับการคำนวณจากลิตรแปลงเป็นเงิน
    if t == 2:
        Oil_in = int(input("ใส่จำนวณลิตร: ").strip())
        oiltype = input("OilType: ").split(" ")
        for ot in oiltype:
            if ot == a:
                price = Oil_in * 29.16
                print('จำนวณเงิน %.2f' % (price), 'BAHT')
            elif ot == b:
                price = Oil_in * 25.30
                print('จำนวณเงิน %.2f' % (price), 'BAHT')
            elif ot == c:
                price = Oil_in * 21.68
                print('จำนวณเงิน %.2f' % (price), 'BAHT')
            elif ot == d:
                price = Oil_in * 20.2
                print('จำนวณเงิน %.2f' % (price), 'BAHT')
            elif ot == e:
                price = Oil_in * 21.2
                print('จำนวณเงิน %.2f' % (price), 'BAHT')
            elif ot == f:
                price = Oil_in * 21.1
                print('จำนวณเงิน %.2f' % (price), 'BAHT')
            else:
                print('Error')
    input(" Press Enter to continue...")


# Function สำหรับการทำซ้ำใหม่
while True:
    func()

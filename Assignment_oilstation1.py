def func():
    print("#"*112)
    for i in range(2):
        print("#"+(" "*110)+"#")
    print("#"+(" "*48)+'Gasoline95 price 29.16'+(" "*40)+"#")
    for i in range(2):
        print("#"+(" "*110)+"#")
    print("#"+(" "*48)+'Gasoline95 price 29.16'+(" "*40)+"#")
    for i in range(2):
        print("#"+(" "*110)+"#")
    print("#"+(" "*48)+'Gasoline95 price 29.16'+(" "*40)+"#")
    for i in range(2):
        print("#"+(" "*110)+"#")
    print("#"+(" "*48)+'Gasoline95 price 29.16'+(" "*40)+"#")
    for i in range(2):
        print("#"+(" "*110)+"#")
    print("#"+(" "*48)+'Gasoline95 price 29.16'+(" "*40)+"#")
    for i in range(2):
        print("#"+(" "*110)+"#")
    print("#"+(" "*48)+'Gasoline95 price 29.16'+(" "*40)+"#")
    for i in range(2):
        print("#"+(" "*110)+"#")
    print("#"*112)
    print("#"*112)
    for i in range(8):
        print("#"+(" "*110)+"#")
    print("#"+(" "*25)+'เลือกว่าจะคำนวณจากเงินเป็นลิตรพิม 1 หรือ จำนวณลิตรเป็นเงินพิม 2'+(" "*33)+"#")
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
    if t == 1:
        price_in = int(input("#"+(" "*15)+"ใส่จำนวณเงิน: ").strip())
        oiltype = input("OilType: ").split(" ")
        for ot in oiltype:
            print("#"*112)
            if ot == a:
                price = price_in / 29.16
                for k in range(5):
                     print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณลิตร %.2f' %
                      (price), 'ลิตร'+(" "*44)+"#")
                for k in range(5):
                     print("#"+(" "*110)+"#")
            elif ot == b:
                 for k in range(5):
                     print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณลิตร %.2f' %(price),'ลิตร'+(" "*44)+"#")
                for k in range(5):
                     print("#"+(" "*110)+"#")
            elif ot == c:
                for k in range(5):
                     print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณลิตร %.2f' %(price),'ลิตร'+(" "*44)+"#")
                for k in range(5):
                     print("#"+(" "*110)+"#")
            elif ot == d:
                for k in range(5):
                     print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณลิตร %.2f' %(price),'ลิตร'+(" "*44)+"#")
                for k in range(5):
                     print("#"+(" "*110)+"#")
            elif ot == e:
                 for k in range(5):
                     print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณลิตร %.2f' %(price),'ลิตร'+(" "*44)+"#")
                for k in range(5):
                     print("#"+(" "*110)+"#")
            elif ot == f:
                 for k in range(5):
                     print("#"+(" "*110)+"#")
                print("#"+(" "*48)+'จำนวณลิตร %.2f' %(price),'ลิตร'+(" "*44)+"#")
                for k in range(5):
                     print("#"+(" "*110)+"#")
            else:
                print('Error')
    if t == 2:
        Oil_in = int(input("ใส่จำนวณลิตร: ").strip())
        oiltype = input("OilType: ").split(" ")
        print("#"*112)
        for ot in oiltype:
            if ot == a:
                price = Oil_in * 29.16
                print('จำนวณเงิน %.2f' %(price),'BAHT')
            elif ot == b:
                price = Oil_in * 25.30
                print('จำนวณเงิน %.2f' %(price),'BAHT')
            elif ot == c:
                price = Oil_in * 21.68
                print('จำนวณเงิน %.2f' %(price),'BAHT')
            elif ot == d:
                price = Oil_in *20.2
                print('จำนวณเงิน %.2f' %(price),'BAHT')
            elif ot == e:
                price = Oil_in *21.2
                print('จำนวณเงิน %.2f' %(price),'BAHT')
            elif ot == f:
                price = Oil_in * 21.1
                print('จำนวณเงิน %.2f' %(price),'BAHT')
            else:
                print('Error')           
    input(" Press Enter to continue...")
while True: 
    func()


# In[ ]:





# In[ ]:





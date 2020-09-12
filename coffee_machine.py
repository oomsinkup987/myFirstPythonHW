def func_main():
    # ข้อมูลของเครื่องทำกาแฟ
    print('#' * 120)
    for i in range(3):
        print('#' + (" " * 118) + "#")
    print("#" + (' ' * 40) + 'The coffee machine has:' + (' ' * 55) + "#")
    print("#" + (' ' * 40) + '400 of water' + (' ' * 66) + "#")
    print("#" + (' ' * 40) + '540 of milk' + (' ' * 67) + "#")
    print("#" + (' ' * 40) + '120 of coffee beans' + (' ' * 59) + "#")
    print("#" + (' ' * 40) + '9 of disposable' + (' ' * 63) + "#")
    print("#" + (' ' * 40) + '550 of money' + (' ' * 66) + "#")
    for i in range(3):
        print('#' + (" " * 118) + "#")
    print('#' * 120)
    # เลือกประเภทที่ต้องการทำรายการ
    print('#' * 120)
    for i in range(3):
        print('#' + (" " * 118) + "#")
    print("#" + (' '*40) + 'Write action (buy, fill, take):' + (' '*47) + "#")
    for i in range(3):
        print('#' + (" " * 118) + "#")
    print('#' * 120)
    # ตัวแปรที่จะเลือกใช้สำหรับเงื่อนไข
    f = 'fill'
    bb = 'buy'
    t = 'take'
    a = input()
    # เงื่อนไขการเรียกใช้ Function
    if a == 'buy':
        func_buy()
    elif a == 'fill':
        func_fill()
    elif a == 'take':
        func_take()
    input('Press Enter to continue...')


def func_buy():
    print('What dod you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    b = input()
    # เงื่อนไข สำหรับเงื่อนไขการ ซื้อกาแฟ  Espresso
    if b == '1':
        print('#' * 120)
        for i in range(2):
            print('#' + (" " * 118) + "#")
        print("#" + (' ' * 40) + 'The coffee machine has:' + (' ' * 55) + "#")
        print("#" + (' ' * 40) + '150 of water' + (' ' * 66) + "#")
        print("#" + (' ' * 40) + '540 of milk' + (' ' * 67) + "#")
        print("#" + (' ' * 40) + '104 of coffee beans' + (' ' * 59) + "#")
        print("#" + (' ' * 40) + '8 of disposable' + (' ' * 63) + "#")
        print("#" + (' ' * 40) + '554 of money' + (' ' * 66) + "#")
        for i in range(2):
            print('#' + (" "*118) + "#")
        print('#'*120)
    elif b == '2':
        # เงื่อนไข สำหรับเงื่อนไขการ ซื้อกาแฟ Latte
        print('#' * 120)
        for i in range(2):
            print('#' + (" " * 118) + "#")
        print("#" + (' ' * 40) + 'The coffee machine has:' + (' ' * 55) + "#")
        print("#" + (' ' * 40) + '50 of water' + (' ' * 67) + "#")
        print("#" + (' ' * 40) + '465 of milk' + (' ' * 67) + "#")
        print("#" + (' ' * 40) + '100 of coffee beans' + (' ' * 59) + "#")
        print("#" + (' ' * 40) + '8 of disposable' + (' ' * 63) + "#")
        print("#" + (' ' * 40) + '557 of money' + (' ' * 66) + "#")
        for i in range(2):
            print('#' + (" " * 118) + "#")
        print('#' * 120)
    elif b == '3':
        # เงื่อนไข สำหรับเงื่อนไขการ ซื้อกาแฟ Cappuciino
        print('#' * 120)
        for i in range(2):
            print('#' + (" " * 118) + "#")
        print("#" + (' ' * 40) + 'The coffee machine has:' + (' ' * 55) + "#")
        print("#" + (' ' * 40) + '200 of water' + (' ' * 66) + "#")
        print("#" + (' ' * 40) + '440 of milk' + (' ' * 67) + "#")
        print("#" + (' ' * 40) + '108 of coffee beans' + (' ' * 59) + "#")
        print("#" + (' ' * 40) + '8 of disposable' + (' ' * 63) + "#")
        print("#" + (' ' * 40) + '556 of money' + (' ' * 66) + "#")
        for i in range(2):
            print('#' + (" " * 118) + "#")
        print('#' * 120)
    else:
        print("ERROR")


def func_fill():
    # Function สำหรับเงื่อนไขการ เติมส่วนประกอบ  fill
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    c = int(input('Write how many ml of water do you want to add:\n'))
    wc = water + c
    d = int(input('Write how many ml of milk do you want to add:\n'))
    md = milk + d
    f = int(input('Write how many grams of coffee beans do you want to add:\n'))
    gb = beans + f
    g = int(input('Write how many disposable cups of coffee do you want to add:\n'))
    cc = cups + g
    print('#' * 120)
    for i in range(3):
        print('#' + (" " * 118) + "#")
    print("#" + (' ' * 40) + 'The coffee machine has:' + (' ' * 55) + "#")
    print("#" + (' ' * 40), wc, 'of water' + (' ' * 64) + "#")
    print("#" + (' ' * 40), md, 'of milk' + (' ' * 65) + "#")
    print("#" + (' ' * 40), gb, 'of coffee beans' + (' ' * 58) + "#")
    print("#" + (' ' * 40), cc, 'of disposable cups' + (' ' * 56) + "#")
    print("#" + (' ' * 40) + '550 of money' + (' ' * 66) + "#")
    for i in range(3):
        print('#' + (" " * 118) + "#")
    print('#' * 120)


def func_take():
    # Function take
    print('I gave you $550')
    print('#' * 120)
    for i in range(3):
        print('#' + (" " * 118) + "#")
    print("#" + (' ' * 40) + 'The coffee machine has:' + (' ' * 55) + "#")
    print("#" + (' ' * 40) + '400 of water' + (' ' * 66) + "#")
    print("#" + (' ' * 40) + '540 of milk' + (' ' * 67) + "#")
    print("#" + (' ' * 40) + '120 of coffee beans' + (' ' * 59) + "#")
    print("#" + (' ' * 40) + '9 of disposable' + (' ' * 63) + "#")
    print("#" + (' ' * 40) + '0 of money' + (' ' * 68) + "#")
    for i in range(3):
        print('#' + (" " * 118) + "#")
    print('#' * 120)


while True:
    func_main()

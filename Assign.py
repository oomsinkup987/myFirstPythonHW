import subprocess as sp
sp.call('clear', shell=True)
oil_li = [{"name": "Gasoline 95 ","price": 29.16},
          {"name": "Gasoline 91 ","price": 25.30},
          {"name": "Gassohol 91 ","price": 21.68},
          {"name": "Gassohol E20","price": 20.20},
          {"name": "Gassohol 95 ","price": 21.00},
          {"name": "Gassohol 95 ","price": 21.10}]


sp.run('', shell=True)
print('#' * 80)
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
print("#"+" " *int(65/2)+"Enter 1 or 2:\0337" + " " * int(66/2) + "#",end="")
print("\n"+ '#' * 80 + '\0338',end="")      
a = input()
print('#' * 80)
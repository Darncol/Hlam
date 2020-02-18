import os

def crypt():
    key = int(input("Ключь:"))
    
    beg_cry = input('Текст для шифрования:')
    bukvi = list(beg_cry)
    wifrovanie = []
    razwifrovanie = []
    
    for bukva in bukvi:
        a = bukva
        b = ord(a)
        c = b + key
        wifrovanie.append(c)

    for bukva1 in wifrovanie:
        a = bukva1
        b = chr(a)
        razwifrovanie.append(b)
    
    final_txt = ''.join(razwifrovanie)
    
    f = open('Test.txt','w')
    f.write(final_txt)
    f.close

    return final_txt

def uncrypt():
    wifr = []
    un_wifr = []
    fin_wifr = []

    key = int(input("Ключь:"))

    f = open('Test.txt')
    a = f.read()
    wifr = list(a)
    f.close

    for bukva in wifr:
        a = bukva
        a = ord(a)
        b = a - key
        un_wifr.append(b)

    for bukva1 in un_wifr:
        a = bukva1
        a = chr(a)
        fin_wifr.append(a)
    
    print(''.join(fin_wifr))

    return

os.system('clear')
vvod = input('1.Зашифровать\n2.Расшифровать\n>')

if vvod == "1":
    print(crypt())

elif vvod == "2":
    uncrypt()

else:
    print('Что-то пошло не так!')
def zapisatknigu():

    newknigaN = input("nazvanie:")
    newknigaC = input("Cena:")

    f = open("Biblioteka.txt", "a")
    gotstr = newknigaN + ".," + newknigaC + "\n"
    f.write(gotstr)
    print("zapisano")
    f.close()

def pokazatknigi():
    spisokknig = vernutspisok()
    spisokknig = "\n".join(spisokknig)
    spisokknig = spisokknig.replace(".,"," ")
    print("Vse knigi:\n" + spisokknig  + "\n")
    return

def pokazatcenu():
    spisokknig = vernutspisok()

    nazvknigi = input("Nazvanie: ")

    knigi = []
    ceni = []

    for stroka in spisokknig:
        stroka = stroka.split(" ")
        knigi.append(stroka[0])
        ceni.append(int(stroka[1]))


    if nazvknigi in knigi:
        takniga = knigi.index(nazvknigi)
        print(str(ceni[takniga])+"\n")

    else:
        print("Knigi netu\n")

    return

def vernutspisok():
    f = open("Biblioteka.txt")

    verper = f.read().splitlines()

    f.close()

    return verper


def dobavitdeneg():
    try :
        lave = int(input("Skolko deneg dobavit?:"))
        if lave >= 0:
            global kowel
            kowel = kowel + lave



    except:
        print("Vse huina davai po novoi")




kowel = 0


while True:
    print("Deneg$$$ =", kowel)
    vvod = input("1 = zapisat knigu\n2 = pokazat knigi\n3 = pokazat cenu\n4 = dobavit deneg\n5 = vihod\n> ")

    if vvod == "1":
        zapisatknigu()

    elif vvod == "2":
        pokazatknigi()

    elif vvod == "3":
        pokazatcenu()

    elif vvod == "4":
        dobavitdeneg()

    elif vvod == "5":
        print("exit")
        break

    else :
        print("naher")

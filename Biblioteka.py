def zapisatknigu():
    try:
        newknigaN = input("nazvanie:")
        newknigaC = int(input("Cena:"))
        if newknigaC >= 0:
            f = open("Biblioteka.txt", "a")
            gotstr = newknigaN + ".," + str(newknigaC) + "\n"
            f.write(gotstr)
            print("zapisano\n")
            f.close()
    except:
        print("Cena ne pravilnaja baran\n")

def pokazatknigi():
    spisokknig = vernutspisok()
    spisokknig = "\n".join(spisokknig)
    spisokknig = spisokknig.replace(".,"," ")
    print("Vse knigi:\n" + spisokknig  + "\n")
    return

def pokazatcenu():
    try:
        spisokknig = vernutspisok()

        nazvknigi = input("Nazvanie: ")

        knigi = []
        ceni = []

        for stroka in spisokknig:
            stroka = stroka.split(".,")
            knigi.append(stroka[0])
            ceni.append(int(stroka[1]))


        if nazvknigi in knigi:
            takniga = knigi.index(nazvknigi)
            print(str(ceni[takniga])+"\n")

    except:
        print("Knigi netu\n")

    return

def vernutspisok():
    f = open("Biblioteka.txt")

    verper = f.read().splitlines()
    # print(verper)


    f.close()

    return verper


def dobavitdeneg():
    try :
        lave = int(input("Skolko deneg dobavit?:"))
        if lave >= 0:
            global kowel
            kowel = kowel + lave
            print("\n")
    except:
        print("Vse huina davai po novoi\n\n")

def kupitknigu():
    try:
        spisokknig = vernutspisok()

        nazvknigi = input("Kakuju knigu kupit?: ")

        knigi = []
        ceni = []
        global kowel

        for stroka in spisokknig:
            stroka = stroka.split(".,")
            knigi.append(stroka[0])
            ceni.append(int(stroka[1]))

        if nazvknigi in knigi:
            takniga = knigi.index(nazvknigi)
            cena = ceni[takniga]

            if kowel - cena > 0:
                kowel = kowel - cena

            else:
                print("Netu deneg baran!\n")


        else:
            print("knigi netu\n")


    except:
        print("Knigi netu\n")

    return


kowel = 0


while True:
    print("Deneg$$$ =", kowel)
    vvod = input("1 = zapisat knigu\n2 = pokazat knigi\n3 = pokazat cenu\n4 = dobavit deneg\n5 = kupit knigu\n9 = vihod\n> ")

    if vvod == "1":
        zapisatknigu()

    elif vvod == "2":
        pokazatknigi()

    elif vvod == "3":
        pokazatcenu()

    elif vvod == "4":
        dobavitdeneg()

    elif vvod == "5":
        kupitknigu()


    elif vvod == "9":
        print("exit")
        break

    else :
        print("naher")

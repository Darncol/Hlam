import os
# os.system("clear")

def zapisatknigu():
    os.system("clear")
    try:
        newknigaN = input("Название книги:")
        newknigaC = int(input("Цена:"))
        newknigaA = "Green"
        if newknigaC >= 0:
            f = open("Biblioteka.txt", "a")
            gotstr = newknigaN + ".," + str(newknigaC) + ".," + newknigaA + "\n"
            f.write(gotstr)
            print("Записано\n")
            f.close()
    except:
        print("Цена не правильная\n")

def pokazatknigi():
    spisokknig = vernutspisok()
    spisokknig = "\n".join(spisokknig)
    spisokknig = spisokknig.replace(".,", " ")
    spisokknig = spisokknig.replace("Green", "Есть в наличии")
    spisokknig = spisokknig.replace("Red", "Нет в наличии")
    print("Все книги:\n" + spisokknig  + "\n")
    return

def pokazatcenu():
    os.system("clear")
    try:

        spisokknig = vernutspisok()

        nazvknigi = input("Название книги: ")

        knigi = []
        ceni = []

        for stroka in spisokknig:
            stroka = stroka.split(".,")
            knigi.append(stroka[0])
            ceni.append(int(stroka[1]))


        if nazvknigi in knigi:
            takniga = knigi.index(nazvknigi)
            print(str(ceni[takniga])+"\n")

        elif nazvknigi != knigi:
            print("Нету книги.\n")

    except:
        print("Error\n")

    return

def vernutspisok():
    f = open("Biblioteka.txt")

    verper = f.read().splitlines()
    # print(verper)


    f.close()

    return verper

def vernutimena():
    f = open('Bibli_Name.txt')
    imena = f.read().splitlines()
    f.close()
    return imena

def dobavitdeneg():
    os.system("clear")
    try :
        lave = int(input("Сколько денег добавить?:"))
        if lave >= 0:
            global kowel
            kowel = kowel + lave
            print("\n")
    except:
        print("Error\n\n")

def kupitknigu():
    os.system("clear")
    try:
        spisokknig = vernutspisok()

        nazvknigi = input("Какую книгу купить?: ")

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

            if kowel - cena >= 0:
                kowel = kowel - cena

            else:
                print("Нхватает денег\n")


        else:
            print("Книги нету\n")


    except:
        print("Error\n")

    return

def arendaknig():
    os.system("clear")
    vibor = input("""Привет,что хотите зделать?
    1 = Взять книгу в аренду
    2 = Вернуть книгу
    3 = Проверить не возвращенные книги
    4 = Зарегистрироваться
    >""")

    if vibor == "1":
        os.system("clear")
        f = open("Bibli_Name.txt")
        vname = f.read().splitlines()
        f.close()
        # print(vname)

        imja = []
        razrewenie = []
        nazvanievzatoiknigi = []
        dlazapis = []

        try:
            for stroka in vname:
                stroka = stroka.split(".,")
                imja.append(stroka[0])
                razrewenie.append(stroka[1])
                nazvanievzatoiknigi.append(stroka[2])
                dlazapis = dlazapis.append(stroka)
                print(stroka)
        except:
            print("Error")

        name = input("Как вас зовут?: ")

        if name in imja:
            inname = imja.index(name)

            if razrewenie[inname] == 'Allow':
                knigavarendu = input('1 = Выбрать книгу?\n2 = показать список?\n>')

                if knigavarendu == '1':
                    nazvknigi = input('Название книги?: ')

                    spisokknig = vernutspisok()
                    knigi = []
                    ceni = []
                    dostup = []

                    for stroka2 in spisokknig:
                        stroka2 = stroka2.split('.,')
                        knigi.append(stroka2[0])
                        ceni.append(stroka2[1])
                        dostup.append(stroka2[2])

                    if nazvknigi in knigi:
                        nomerknigi = knigi.index(nazvknigi)
                        print(nomerknigi)

                        if dostup[nomerknigi] == 'Green':

                            dlazapis[nomerknigi[2]] = "Denied"
                            print(dlazapis)



                            zapis = open('Bibli_Name.txt', 'w')
                            zapis.write(dlazapis)
                            zapis.close()
                            

                        elif dostup[nomerknigi] == 'Denied':
                            os.system('clear')
                            print('Книга уже в аренде\n')

                        else:
                            os.system('clear')
                            print('Проверь название\n')

                elif knigavarendu == '2':
                    pokazatknigi()

                else:
                    os.system('clear')
                    print('Erorr434')

            elif razrewenie[inname] == 'Denied':
                print('Нужно вернуть старые книги\n')
        else:
            print('Нет такого имени в базе\n')

    elif vibor == "2":
        pass

    elif vibor == "3":
        knigi = vernutspisok()

    elif vibor == "2":
        pass

    elif vibor == "3":
        pass

    elif vibor == "4":

        name = input("Как вас зовут?: ")

        nname = name + ".," + "Allow" + ".," + "pusto" + "\n"

        f = open("Bibli_Name.txt","a")
        zapis = f.write(nname)

        os.system("clear")
        print("Записано")



kowel = 0

def main():
    while True:

        print("Денег$$$ =", kowel)
        vvod = input("1 = Добавить книгу\n2 = Показать все книги\n3 = Показать цену книги\n4 = Добавить денег\n5 = Купить книгу\n6 = Аренда книг\n9 = Выход\n> ")

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

        elif vvod == "6":
            arendaknig()


        elif vvod == "9":
            print("exit")
            break

        else :
            print("Не балуйся!")

if __name__ == "__main__":
    main()
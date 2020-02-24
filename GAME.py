import os

level = 1        # level - уровень и жизни (level*10=hp)
exp = 0         # exp - опыт
stren = 1       # stren - урон
dex = 1        # dex - будет влиять на шанс попадания
luck = 1        # luck - будет влиять на силу монстров
expp = 5        # expp - скил поинты


def addskills(kuda,skolko):  # добавить скиллов
    global stren,dex,luck,expp
    
    if kuda == '1' and skolko <= expp:
        stren += skolko
        expp -= skolko
    elif kuda == '2' and skolko <= expp:
        dex += skolko
        expp -= skolko
    elif kuda == '3' and skolko <= expp:        
        luck += skolko
        expp -= skolko
    else:
        os.system('clear')
        print('не хватает очков!')          
    

def levelup(income_exp): # увеличение уровня и получение опыта с очками навыков
    global exp,level,expp
    exp += income_exp
   
    if exp > ((level**2)*100):
        level += 1
        expp += 5
      

def char():  # посмотреть персонаж
    os.system('clear')
    global level,exp,expp,stren,dex,luck,expp
 
    print(f'''
    Уровень:{level}
    Опыт:{exp}
    1=Сила:{stren}
    2=Ловкость:{dex}
    3=Удача:{luck}
    Свободных очков:{expp}
    ''')
    vvod = input('1.добавить очки\n2.назад\n>')

    if vvod == '1':
        if expp > 0:
            kuda = input('Куда добавить?\n>')
            skolko = int(input('Сколько?:'))
            addskills(kuda,skolko)
        else:
            print('Не хватает очков')
    elif vvod == '2':
        pass
    else:
        print('Не балуйся!')

def fight():
    income_exp = int(input("exp:"))
    levelup(income_exp)
    return

def main():
    os.system('clear')
    while True:
        print(f'''
    Уровень:{level}
    Опыт:{exp}
    1=Сила:{stren}
    2=Ловкость:{dex}
    3=Удача:{luck}
    Свободных очков:{expp}
    ''')
        
        vvod = input('1.Персонаж\n2.бой\n3.сохранить\n>')

        if vvod == '1':
            char()
            
        elif vvod == '2':
            fight()
        elif vvod == '3':
            pass

main()
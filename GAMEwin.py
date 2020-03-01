import os
import random

# статы персонажа
level = 1        # level - уровень и жизни (level*10=hp)
exp = 0         # exp - опыт
stren = 20       # stren - урон и жизни
dex = 5        # dex - броня
luck = 1        # luck - будет влиять на силу монстров
expp = 10        # expp - скил поинты

# временые статы для боя
hp = 0
attack = 0
armor = 0

# временные статы монстра
hpm = 0
attackm =0
armorm = 0

# временный опыт за победу
temp_exp_for_win = 0
damage = 0

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
        os.system('cls')
        print('не хватает очков!')          
    

def levelup(income_exp): # увеличение уровня и получение опыта с очками навыков
    global exp,level,expp
    exp += income_exp
    obnulit_damag()
    if exp > ((level**2)*100):
        level += 1
        expp += 5
      

def char():  # посмотреть персонаж
    os.system('cls')
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

def fightstats(): #статы персонажа перед боем
    global hp,attack,armor
    hp = (level * 100) + stren
    attack = stren 
    armor = dex
    
def exp_for_fight(): # получаемый опыт после боя income_exp
    global temp_exp_for_win
    income_exp = damage/10
    temp_exp_for_win = income_exp
    levelup(income_exp)

def obnulit_damag(): # обнуляем накопленный дамаг после боя
    global damage
    damage = 0

def fight_process():    #  процесс боя
    global hp,attack,armor,hpm,attackm,armorm,damage
    while hpm > 0:
        os.system('cls')
        randnum1 = random.randrange(1,4)
        randnum2 = random.randrange(1,4)
        

        print(f"""
        Персонаж:           Монстр:
        Жизни:{hp}           Жизни:{hpm}
        Урон:{attack}             Урон:{attackm}
        Броня:{armor}             Броня:{armorm}""")

        def udar(): #Удар
            global hp,attack,armor,hpm,attackm,armorm,damage
            try:
                vibor1 = int(input(""" 
                куда ударить ?
                1 = голова
                2 = тело
                3 = ноги
                >"""))
            
                if vibor1 == randnum1:
                    print('Не попал!')
                        
                    
                elif vibor1 != randnum1:
                    if vibor1 in range(1,4):
                        uron = attack-armorm
                        hpm -= uron
                        damage += uron
                        print(f"Нанесено урона:{uron}")
                    else:
                        print('Не попал!')
                else:
                    print('s udarom beda')
            except:
                udar()

        def block():  # блок
            global hp,attack,armor,hpm,attackm,armorm,damage
            try:    
                vibor2 = int(input(""" 
                куда поставить блок ?
                1 = голова
                2 = тело
                3 = ноги
                >"""))
                

                if vibor2 == randnum2:
                    print('Успешно защитился')
                elif vibor2 != randnum2:
                    
                    uron = attackm - armor
                    hp -= uron
                    print(f'получено урона:{uron}')

            except:
                block()    
        udar()
        block()
        os.system('cls')
        if hp < 0:
            print('Ты проиграл!')
            break
    else:
        exp_for_fight()
        print('Победа! ты получил опыта:',temp_exp_for_win)
        
def save():     # сохранение
    a = [level,exp,stren,dex,expp]
    b = []

    for i in a:
        i = str(i)
        b.append(i)

    b = ' '.join(b)
    f = open('GAME.txt','w')
    f.write(b)
    f.close()
    

def load():     # загрузка
    global level,exp,stren,dex,expp
    a = []
    f = open('GAME.txt')
    b = f.read().split(' ')
    for i in b:
        i = int(i)
        a.append(i)

    level = a[0]
    exp = a[1]
    stren = a[2]
    dex = a[3]
    expp = a[4]

    


def fight():      # бой с монстром
    global hp,attack,armor,hpm,attackm,armorm
    fightstats()
    monster()
    fight_process()
    
    

    
def monster():   #сила монстра
    global hpm,attackm,armorm
    hpm = (random.randrange(hp)*1.5+(level*30))
    attackm = random.randrange(attack)* 1.5
    armorm = random.randrange(armor)
    

def main():     #главное меню
    
    while True:
        os.system('cls')
        print(f'''
    Уровень:{level}
    Опыт:{exp}
    1=Сила:{stren}
    2=Ловкость:{dex}
    3=Удача:{luck}
    Свободных очков:{expp}
    ''')
        
        vvod = input('1.Персонаж\n2.бой\n3.сохранить\n4.Загрузить\n>')

        if vvod == '1':
            char()
        elif vvod == '2':
            fight()
        elif vvod == '3':
            save()
        elif vvod == '4':
            load()
        else:
            print('Не балуйся!')

main()

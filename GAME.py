import os
import random


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

def fightstats(): #статы персонажа перед боем
    global hp,attack,armor
    hp = (level * 100) + stren
    attack = stren 
    armor = dex
    
def exp_for_fight(): # получаемый опыт после боя income_exp
    income_exp = (hpm+(attackm*10)+(armorm*10))
    levelup(income_exp)
    

def fight():      # бой с монстром
    fightstats()
    monster()
    while hp > 0 and hmp > 0:
        vibor = input()
    else:
        print()
        pass

    
def monster():   #сила монстра
    global hpm,attackm,armorm
    hpm = (random.randrange(hp)*1.5+(level*30))
    attackm = random.randrange(attack)* 1.5
    armorm = random.randrange(armor)*1.5
    

def main():     #главное меню
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
        else:
            print('Не балуйся!')

# статы персонажа
level = 10        # level - уровень и жизни (level*10=hp)
exp = 0         # exp - опыт
stren = 10       # stren - урон и жизни
dex = 10        # dex - броня
luck = 1        # luck - будет влиять на силу монстров
expp = 5        # expp - скил поинты

# временые статы для боя
hp = 0
attack = 0
armor = 0

# временные статы монстра
hpm = 0
attackm =0
armorm = 0

main()

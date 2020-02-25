import os
import random

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

#  опыт за победу
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
    global temp_exp_for_win
    income_exp = damage/10
    temp_exp_for_win = income_exp
    levelup(income_exp)

def obnulit_damag(): # обнуляем накопленный дамаг после боя
    global damage
    damage = 0
    

def fight():      # бой с монстром
    global hp,attack,armor,hpm,attackm,armorm
    fightstats()
    monster()
    while hpm > 0:
        os.system('clear')
        randnum1 = random.randrange(1,4)
        randnum2 = random.randrange(1,4)
        print (randnum1)

        print(f"""
        Персонаж:           Монстр:
        Жизни:{hp}          Жизни:{hpm}
        Урон:{attack}       Урон:{attackm}
        Броня:{armor}       Броня:{armorm}""")

        
        vibor1 = int(input(""" 
        куда ударить ?
        1 = голова
        2 = тело
        3 = ноги
        >"""))
        

        if vibor1 == randnum1:
            print('Не попал!')
                
            
        elif vibor1 != randnum1:
            if vibor1 == range(1,4) and attack - armorm > 0:
                 hpm -= (attack-armorm)
            elif attack - armorm < 0: 
                print('Удар слишком слабый и не нанесет урона,ты проиграл!')
                break
            else:
                print('что-то пошло не так!')
            

        vibor2 = int(input(""" 
        куда поставить блок ?
        1 = голова
        2 = тело
        3 = ноги
        >"""))

        if vibor2 == randnum2:
            print('Успешно защитился')
        elif vibor2 != randnum2:
            print()

        if hp < 0:
            print('Ты проиграл!')
            break


    else:
        exp_for_fight()
        print('Победа! ты получил опыта:',temp_exp_for_win)
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

main()

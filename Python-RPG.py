name = input("Nome: ")
race = input("Raça: ")
speed = int(input("Velocidade: "))
defence = int(input("Defesa: "))
attack = int(input("Digite o ataque: "))
 
if race == "Humano":
    speed = speed + 0
    defence = defence + 0
    attack = attack + 1
 
if race == "Orc":
    speed = speed - 1
    defence = defence + 5
    attack = attack + 3
 
if race == "Elfo":
    speed = speed + 2
    defence = defence + 0
    attack = attack + 2
if race == "Fada":
    speed = speed + 5
    defence = defence - 1
    attack = attack + 2
 
if race == "Bruxa":
    speed = speed - 2
    defence = defence + 2
    attack = attack + 2
 
if race == "Robô":
    speed = speed + 5
    defence = defence + 2
    attack = attack + 3
print ("\n**** FICHA DE PERSONAGEM ****")
print ("O nome é: ", name)
print ("A raça é: ", race)
print ("A velocidade é: ", speed)
print ("A defesa é: ", defence)
print ("O ataque é: ", attack)

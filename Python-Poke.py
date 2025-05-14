print("Boas vindas a batalha pokémon!")
print("\nEscolha seu pokémon: Alakazan, Charizard, Mesprit")

vida = 200
while vida > 0:
    pokemon=input("\nDigite o nome do seu Pokémon: ")
    
    if pokemon == "Alakazan":
        print("Ataque Psico")
        print("Ataque de -90hp")
        vida = vida - 90
        print(vida)
        
    if pokemon == "Charizard":
        print("Ataque bola de fogo")
        print("Ataque de -120hp")
        vida = vida - 120
        print(vida)
        
    if pokemon == "Mesprit":
        print("Ataque Nevasca")
        print("Ataque de -50hp")
        vida = vida - 50
        print(vida)

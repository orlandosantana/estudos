
#Crie um programa que o usuário digite um nome e retorne o nome e também o nº de letras que tem o nome

question = "Qual o melhor jogador que viu jogar? "
awnser = input(question)
return_ = "Melhor jogador "
len_awnser = len(awnser)

print(return_ + awnser)
print("Nº de letras: " + str(len_awnser))
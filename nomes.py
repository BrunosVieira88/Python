import random
homens =[]
mulheres=['Isabele','Aline','Luisa','Flavia','Daniela']

random.shuffle(homens)
random.shuffle(mulheres)

for i in range (0,5):
    homens.append(str(input("Digite o nome do Amigo ")))



for j in range(0, len(mulheres)):
        print(f'{homens[i]} quer muito foder a  {mulheres[j]}')
        i -= 1



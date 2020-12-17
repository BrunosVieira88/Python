nome=str(input('digite uma frase ')).strip()
nome=nome.lower()

print('tem {} letras A na frase '.format(nome.count('a')))
print('Ela aparece na primeira vez na posição {} posição'.format(nome.find('a')+1))
print('Ela aparece na ultima vez na posição {} posição'.format(nome.rfind('a')+1))
print("""
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
""")
j = 17
times = ('Flamengo','Palmeiras','Santos','São Paulo','Corinthians','Internacional','Grêmio',
            'Bahia','Athletico-PR','Goiás','Vasco da Gama','Atlético-MG','Botafogo','Fortaleza',
            'Ceará','Fluminense','Cruzeiro','CSA','Chapecoense','Avaí')

print('*'*30)
print('Os primeiros 5 colocados !')
for i in range (0,5):
                print(f'{i+1}->{times[i]} ',end=' ')


print('\n')
print('*'*30)
print('os ultimos 4 lugares ')
for i in range (-4,0,):
        print(f'{j}->{times[i]} ',end=' ')
        j=j +1

print('\n')
print('*'*30)
print('os times por ordem alfabetica!')
print(sorted(times))
print('\n')
print('*'*30)
print('colocação da chape')
print(f'A Chape esta na ->{times.index("Chapecoense" )+1} ')
print('*'*30)
print(times[0:5])
print(times[-4:])
print(sorted(times))
print(times.index("Chapecoense")+1)


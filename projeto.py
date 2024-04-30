nome = "Ash"
xp = float(input('Digite sua xp: '))

if xp < 1.000:
    print(f'O Herói de nome {nome}, está no nível de {xp},Ferro!')
elif xp > 1001 and xp <= 2000:
    print(f'O Herói de nome {nome}, está no nível de {xp},Bronze!')
elif xp > 2001 and xp <= 5000:
    print(f'O Herói de nome {nome}, está no nível de {xp},Prata!')
elif xp > 6001 and xp <= 7000:
    print(f'O Herói de nome {nome}, está no nível de {xp},Ouro!')
elif xp > 7001 and xp <= 8000:
    print(f'O Herói de nome {nome}, está no nível de {xp},Platina!')
elif xp > 8001 and xp <= 9000:
    print(f'O Herói de nome {nome}, está no nível de {xp},Ascendente!')
elif xp > 9001 and xp <= 10000:
    print(f'O Herói de nome {nome}, está no nível de {xp},Imortal!')
else:
    print(f'O Herói de nome {nome}, está no nível de {xp},Radiante!')
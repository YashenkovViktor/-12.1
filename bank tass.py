per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("10000:"))
deposit1 = money*per_cent['ТКБ']/100
deposit2 = money*per_cent['СКБ']/100
deposit3 = money*per_cent['ВТБ']/100
deposit4 = money*per_cent['СБЕР']/100
deposit =[], deposit.append(deposit1)
deposit.append(deposit2)
deposit.append(deposit3)
deposit.append(deposit4)
print("deposit =", deposit)
print('Максимальная сумма, которую Вы можете заработать =', max(deposit))
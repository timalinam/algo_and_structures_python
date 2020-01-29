"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import defaultdict

below_the_average = []
above_average = []

company_profits = defaultdict(list)
n = int(input('Введите колличество предприятий\n'))

for i in range(1, n + 1):
    name = input(f'Введите название предприятия под номером {i}\n')
    for j in range(1, 5):
        profit = int(input(f'Введите прибыль предприятия {name} за {j} квартал\n'))
        company_profits[name].append(profit)
    sum_profit = sum(company_profits[name])
    company_profits[name].append(sum_profit)

sum_profits = 0
for i in company_profits.values():
    sum_profits += i[4]
middle_profit = sum_profits/n

for i, j in company_profits.items():
    if j[4] < middle_profit:
        below_the_average.append(i)
    elif j[4] > middle_profit:
        above_average.append(i)

print(f'Предприятия, у которых прибыль ниже среднего: {below_the_average}')
print(f'Предприятия, у которых прибыль выше среднего: {above_average}')





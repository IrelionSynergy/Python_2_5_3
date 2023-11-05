print('Введите минимальную сумму инвестиций:')
minimumSumInvestition = int(input())

print('Введите сумму у Майкла:')
sumMike = int(input())

print('Введите сумму у Ивана:')
sumIvan = int(input())

if sumMike >= minimumSumInvestition and sumIvan >= minimumSumInvestition:
    print(2)
else:
    if(sumMike >= minimumSumInvestition):
        print('Mike')
    elif(sumIvan >= minimumSumInvestition):
        print('Ivan')
    elif sumMike + sumIvan >= minimumSumInvestition:
        print(1)
    else:
        print(0)
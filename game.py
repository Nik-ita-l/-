b=[]#Игра начинается 
for x in range(8):
    b.append(['','','','','','','',''])# заполняю пустыми значениями 
import random 
chips_couter = 0
for _ in range(12): # исходная расстановка фишек 
    i = random.randint(0,7)# индекс строка 
    j = random.randint(0,7)# индекс столбца
    if b[i][j]!= 'x':
        b[i][j] = 'x'
        chips_couter = chips_couter + 1


print ('   ' + '0' + '  ' + '1' + '  ' + '2' + '  ' + '3' + '  ' + '4' + '  ' + '5' +'  '+'6'+'  '+'7')# номера столбцов печатаем 
i=0
for raw in b:
    print( str(i) + '  ' + raw[0] + '  '  + raw[1] + '  ' + raw[3] + '  ' + raw[4] + '  ' + raw[5] + '  ' + raw[6] +'  '+ raw[7])# печатаем все элементы 
    i=i+1
    
player = 1

while True:
    print('Ходит игрок номер: ' + str(player))
    print("Напиши, что хочешь удалить строку или столбец.")
    user_input = input()
    while user_input!='строку' and user_input!='столбец':
        print("Некорректный ввод. Напиши, что хочешь удалить строку или столбец.")
        user_input = input()
    if user_input == 'строку':
        print("Напиши номер строки")
        raw = int(input())
        while raw<0 and raw>7:
            print("Напиши номер строки от 0 до 7")
            raw = int(input())
        for index,value in enumerate(b[raw]):
            if value=='x':
                b[raw][index]=''
                chips_couter = chips_couter - 1
        
    elif user_input == 'столбец':
        print("Напиши номер столбца")
        column = int(input())
        while column<0 and column>7:
            print('Напиши номер столбца от 0 до 7')
        for index,value in enumerate(b):
            if b[index][column]=='x':
                b[index][column]=''
                chips_couter = chips_couter - 1
        
    if chips_couter==0:
        break
    print ('   ' + '0' + '  ' + '1' + '  ' + '2' + '  ' + '3' + '  ' + '4' + '  ' + '5' +'  '+'6'+'  '+'7')
    i=0
    for raw in b:
        print( str(i) + '  ' + raw[0] + '  '  + raw[1] + '  ' + raw[3] + '  ' + raw[4] + '  ' + raw[5] + '  ' + raw[6] +'  '+ raw[7]) 
        i=i+1
    if player==1:
        player=2 
    else:
        player=1
        
    
print('Игра закончилась, победил игрок номер: ' + str(player))

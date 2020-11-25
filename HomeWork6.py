userChoice = 0
work_array = []

def do_first_operation():
    a = list(map(int,input().split()))
    return a
    

def do_second_operation():
    if len(work_array) == 0:
        print("База пуста!")
    else:
        print("Результат умножения", work_array[0], "на", work_array[1], ":", work_array[0] * work_array[1])
        
def do_third_operation():
    if len(work_array) == 0:
        print("База пуста!")
    else:
        if work_array[1] == 0:
            print("Делитель равен 0")
        else:
            print("Результат деления", work_array[0], "на", work_array[1], ":", float(work_array[0]) / float(work_array[1]))
    
def printMenu():
    print('Меню:')
    print('1. Ввести значения а и b')
    print('2. Умножить значения a и b')
    print('3. Делить а на b')
    print('4. Выход')
    
printMenu()
userChoice = int(input())
while userChoice != 4:
    print('Введите опцию:', userChoice)
    if (userChoice < 1 or userChoice > 4):
        print('Такой опции нет, выберите существующую опцию.')
    else:
        if userChoice == 1:
            print("Введите a и b через пробел")
            work_array = do_first_operation()
            print("Вы ввели:")
            print(work_array)
        elif userChoice == 2:
            do_second_operation()
        else:
            do_third_operation()
    printMenu()
    userChoice = int(input())    

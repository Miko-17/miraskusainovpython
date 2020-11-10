userChoice = 0
workArray = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def doOperation(n):
    if n == 1:
        print(" ".join(map(str, workArray)))
    elif n == 2:
        print("Введите значение, которое хотите добавить")
        result = int(input())
        workArray.append(result)
        print("Вы добавили к массиву ", result)
            
def printMenu():
    print('Меню:')
    print('1. Вывести на экран все знаения')
    print('2. Добавить значение')
    print('3. Удалить значение')
    print('4. Найти значение')
    print('5. Отсортировать значения')
    print('6. Выйти')
    print('Введите опцию:')

printMenu()
userChoice = int(input())
while userChoice != 6:
    print('Введите опцию:', userChoice)
    if (userChoice < 1 and userChoice > 6):
        raise ValueError()
    else:
        doOperation(userChoice)
    printMenu()
    userChoice = int(input())
        
        

userChoice = 0
workArray = [0,1,2,3,4,5,6,7,11,10,9,8,12,13,14,15]

def doOperation(n):
    if n == 1:
        print(" ".join(map(str, workArray)))
    elif n == 2:
        print("Введите новое число")
        result = int(input())
        workArray.append(result)
    elif n == 3:
        if len(workArray) != 0:
                print('Введите число для удаления:')
                searchValue = int(input())
                deleted = False
                for count in range(0, len(workArray)):
                    if (workArray[count] == searchValue) & (count < len(workArray)):
                        deleted = True
                        while count+1 < len(workArray):
                            workArray[count] = workArray[count+1]
                            count = count+1
                if deleted:
                    del workArray[count]
                elif not deleted:
                    print('Значения нет в базе данных.')
                else:
                    print('База пустая! Добавте значения!')
      
    elif n == 4:
        print("Введите число для поиска его индекса:")
        element = int(input())
        found = False
        if len(workArray) != 0:
            for count in range(0, len(workArray)):
                if workArray[count] == element:
                    found = True
                    print('Индекс значения "', element, '":', count)
            if found is False:
                print('Значение не найдено!')
        else:
            print('База пустая! Не можем искать!')
    else:
        if len(workArray) != 0:
            print("Список до:"," ".join(map(str, workArray))) 
            workArray.sort()
            print("Список после:"," ".join(map(str, workArray)))
        else:
            print("База пуста!")
            
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
    if (userChoice < 1 or userChoice > 6):
        print('Такой опции нет, выберите существующую опцию.')
    else:
        doOperation(userChoice)
    printMenu()
    userChoice = int(input())    

# Сортировка


"""
jack =  19
adam =  43                               # Это список который должен быть отсортирован, тут у каждой переменной совй аргумент
becky = 11
people = [jack, adam, becky]                    # Объявляем ещё одну переменную в которую помещаем все предыдушие

people.sort(reverse= False)                     # Функция reverse  в зависмости от значения True = значения сортируются по убыванию, False = по возрастанию

                                 
                                  
print(people)                        # Думаю понятно

"""
# сортировка чисел которые делятся на 2 
"""
def funcSort(x):                            #  Эта функция  определяет остаток у чисел, у которых его нет согласно следуещему условию(делятся на 2) юудут выводиться согласно слудующим условиям
    return x%2

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sorted(a, key=funcSort))              
"""

# Сортировка по определенному символу 
"""
lst = ["Москва", "Тверь", "Смоленск", "Псков", "Рязань"]
print(sorted(lst, key= lambda x: x[1]))
print(sorted(lst, key= lambda x: x[3]))
"""

# Рекурсия

"""
def fib(x):                             # Вычисление чисел фибоначи 
    if x == 1:
        return 0
    if x == 2:
        return 1
    else:
        return fib(x - 1) + fib(x -1)   # Формула для вычисления чисео фибоначи, учитывая что за счет этой формулы происходит постоянное воспроизведение чисел до 1, получается рекурсия

print(fib(10))
"""
"""
def fac(x):                 # Вычисление факториала с помошью рекурсии
    if x< 10:               # Условие гласит что x меньше 10
        print(x)            # Печатаем x
        fac(x + 1)          # Передаем от аргумента X на 1 больше
        print(x)            # Печатаем тот аргумент X, к которому прибавили 1 

fac(1)        
"""
'''
Таким образом, с помошью рекурсии мы дошли до 10 и вернулись обратно
'''


# Бинарный поиск

def binary_search(x, y):                
    low = 0                               
    high = len(x)
    
    while low < high:
        center = (low + high)// 2

        if x[center] == y:
            return center
        elif x[center] > y:
            high = center        
        elif x[center] < y:
            low = center


    return -1 

x = [0,1,2,3,4,5,6,7,8,9,10]
print(binary_search(x, 8))
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
"""
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
"""

# Слияние списков


"""
n, m = 3,5
a = [2,8,8] 
b = [3,4,5,5,10]
i = j =0
c =[]
while i<n and j<m:
    if a[i]< b[j]:
        c.append(a[i])
        i +=1
    else:
        c.append(b[j])
        j+=1
while j<m:
    c.append(b[j])
    j+=1

    print(*c)
"""

# Слияние списков через рекурссию
"""
def merge_lists(a, b):
    c= []
    i=j=0
    while i<len(a) and j<len(b): 
        if a[i]< b[j]:
            c.append(a[i])
            i+= 1
        else:
            c.append(b[j])
            j+=1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c

def merge(s):           # функция merge выполняет сортировку
    if len(s) == 1:        # По условию, если длина нашего списка равна 1, значит мы имеем дело с отсортированным списком, тогда выходим из рекурсии
        return s        # Учитывая предыдщее условия, возвращаем этот элемент
    midlle =len(s)//2   # Находим середину деля наш список на 2 
    left_side = merge(s[:midlle])    # Левая часть списка s, это все до середины. Но также мы должны не просто брать до или после середины, а передовать его функции merge, ьлшда они будут распадатся на отделные цифры и собираться обратно в отсортированный список
    right_side = merge(s[midlle:])    # Правая часть, это все после середины.Но также мы должны не просто брать до или после середины, а передовать его функции merge
    return merge_lists(left_side, right_side)


print(merge([7,5,2,3,9,8]))
"""

# Быстрая сортировка


def quick_sort(s):
    if len(s)<= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x<elem, s))
    center = [i for i in s if i== elem ]
    right = list(filter(lambda x: x>elem, s)) 

    return quick_sort(left) + center + quick_sort(right)  

print(quick_sort([7,6,10,5,9,8,3,4]))

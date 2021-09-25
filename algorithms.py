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

"""
def quick_sort(s):
    if len(s)<= 1:
        return s
    elem = s[0]                                     # Выбираем опорный элемент
    left = list(filter(lambda x: x<elem, s))        # В левой части выбираем из списка числа меньше опорного 
    center = [i for i in s if i== elem ]            # Элементы равные опорному
    right = list(filter(lambda x: x>elem, s))       # справ жлементы которые больше опорного

    return quick_sort(left) + center + quick_sort(right)  #     Справа и слева они не отсортированы поэутому передаем им функцию quick sort, она рекусивна поэтому действия будут повотряться вновь пока не будет длстигнут базовый случай

print(quick_sort([7,6,10,5,9,8,3,4]))
"""

# Поиск в ширину с помошью графов

"""
N, M = map(int, input().split())            # Вводим кол-во вершин и ребер  
graph = {i:set() for i in range(N)}         # Будем хранить в  виде словаря с множествами
for i in range(M):

    v1, v2 = map(int, input().split())      # Считываем ребро
    graph[v1].add(v2)                       # Добавляем смежность 2-ух вершин
    graph[v2].add(v1)

from collections import deque              
distance = [None] * N                       # Расстояние, по дефолту неизвестно
start_vertex = 0                            # Начинаем с вершины 0
distance[start_vertex] = 0                  # Расстояние до верщины 0 равно 0
queue = deque([start_vertex])               # Создаем очередь

while queue:                                # Цмкл выполняется пока очередь не пуста 
    cur_v = queue.popleft()                  # Достаем первый элемент
    for neigh_v in  graph[cur_v]:            # Про ходим всех ео соседей
        if distance[neigh_v] is None:        # если сосед не посещен
            distance[neigh_v] = distance[cur_v] + 1     # Считаем расстояние 
            queue.append(neigh_v)                   # Добавляем в очередь
print(distance)     
"""


# Алкогритм Дейкстры
"""
import math


def arg_min(T, S):
    amin = -1
    m = math.inf  # максимальное значение
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i

    return amin


D = ((0, 3, 1, 3, math.inf, math.inf),
     (3, 0, 4, math.inf, math.inf, math.inf),
     (1, 4, 0, math.inf, 7, 5),
     (3, math.inf, math.inf, 0, math.inf, 2),
     (math.inf, math.inf, 7, math.inf, 0, 4),
     (math.inf, math.inf, 5, 2, 4, 0))

N = len(D)  # число вершин в графе
T = [math.inf]*N   # последняя строка таблицы

v = 0       # стартовая вершина (нумерация с нуля)
S = {v}     # просмотренные вершины
T[v] = 0    # нулевой вес для стартовой вершины
M = [0]*N   # оптимальные связи между вершинами

while v != -1:          # цикл, пока не просмотрим все вершины
    for j, dw in enumerate(D[v]):   # перебираем все связанные вершины с вершиной v
        if j not in S:           # если вершина еще не просмотрена
            w = T[v] + dw
            if w < T[j]:
                T[j] = w
                M[j] = v        # связываем вершину j с вершиной v

    v = arg_min(T, S)            # выбираем следующий узел с наименьшим весом
    if v >= 0:                    # выбрана очередная вершина
        S.add(v)                 # добавляем новую вершину в рассмотрение

#print(T, M, sep="\n")

# формирование оптимального маршрута:
start = 0
end = 4
P = [end]
while end != start:
    end = M[P[-1]]
    P.append(end)

print(P)
"""

# Представляем число в любой системе исчислений
"""
base = 3

x = int(input("Enter the number:"))

while x>0:
    digit = str(x % base) 
    print(digit, end='')
    x //= base
"""
"""
def BinarySearch(list, item): # Бинарный поиск
    first = 0
    last = len(list)
    index = -1                               # Индекс мы будем выводить и отнимать 1, посколькусистема исчислении в Python введется с 0
    while (first <= last) and (index == -1): # Условия, думаю понятны
        help = (first+last)//2               # Объявляем переменную help которую будем считать по формуле двоичного поиска
    
        if list[help] == item:               # Собственно пишем условия. Если 2 аргумент равен одному из списка, то мы выводим положение в числе  согласно функции len(list)
            index = help
       
                
                    
    return index

print(BinarySearch([1, 2, 3, 4, 5 ,6 , 7], 2))
"""


# Сортировка

class Sort():                       # создаем класс Sort
    def __init__(self, name, age):  # Создаем метод init,  он будет выводить список который мы создадим ниже
        self.name = name 
        self.age = age


    def __repr__(self):                         # Метод repr выведет список в строке 
        return "" % (self.name, self.age)       # Тут показано в каком виде он возврашает

jack = 'Jack', 19
adam = 'Adam', 43                               # Это список который должен быть отсортирован, тут у каждой переменной совй аргумент
becky = 'Becky', 11
people = [jack, adam, becky]                    # Объявляем ещё одну переменную в которую помещаем все предыдушие

sorted(people)                                  # Думаю понятно
print(people) 



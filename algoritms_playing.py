

"""
1 task
есть список и необходимо каждое второе число уможить на два. ну или другую любую манипуляцию. Использовал декоратор для усложнения
"""

def generator(func):  # делаем декор для выбора каждого второго числа и умножения на 2 его
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(1, len(result), 2):   #  ЗАПОМНИТЬ !!!!  необходимо именно длина списка а не просто список
            result[i] = result[i]*2
        return result
    return inner
                       
old_list = [1,2,3,4]
new_list = old_list[1::2]
new_list1 = old_list[0::2]

@generator  
def generate(old_list, new_list):  # теперь основная функц которая создает из двух списков один, внедряя один в другой а не чередуя их
    new_list1 = [i for a in zip(old_list, new_list) for i in a]   # ЗАПОМНИТЬ !!!!!   i for a in zip(old_list, new_list) создает тапл пар (1,3), (2,4) за второю итерацию ми перебираем пари таплов и вносим их поочередно в список
    return new_list1

print(generate(new_list1, new_list))  #  [1, 4, 3, 8]


"""
2 task
создать функцию, определяющую наличие или отсутствие двойных символов в строке (включая пробельные символы). Например, aa, !! или .
Вы хотите, чтобы функция возвращала true, если строка содержит двойные символы, и false, если нет. 
тест не должен быть чувствителен к регистру; например, оба aa & aA возвращают true.
"""


doubleCheck = "abca"
#returns false
  
doubleCheck1 = "aabc"
#returns true

doubleCheck2 = "a 11 c d"
#returns true
  
doubleCheck3 = "AabBcC"
#returns true
  
doubleCheck4 = "a b  c"
#returns true
  
doubleCheck5 = "a b c d e f g h i h k"
#returns false
  
doubleCheck6 = "2020"
#returns false
  
doubleCheck7 = "a!@€£#$%^&*()_-+=}]{[|\"':;?/>.<,~"
#returns false
  

def check_string(a: str):
    b = a.lower()
    for i in range(1, len(b)):
        if b[i] == b[i-1]:  # индекс что мы проверяем если совпадает с индексом предыдущим
            return True
    return False


print(check_string(doubleCheck7))


"""
3 task
Вы получите список с несколькими разрозненными числами.
Вы должны проверить, что сумма двух значений по обе стороны равна сумме остальных элементов списка.
Если нет, удалите два элемента по бокам и проверьте еще раз,
пока не достигнете контрольного списка условий:
Сумма списка без сторон = сумме сторон
Если она не равна, верните пустой список []
[1,2,3,4,5] ==> 1+5 != 2+3+4 ==> [2,3,4] ==> 2+4 != 3 == [3] ==> 3+3 != 0 ==> []
[0,104,3,101,0,111] ==> 0+111 != 104+3+101+0 ==> [104,3,101,0] ==> 104+0 = 3+101 ==> [104,3,101,0]
[1,-1] ==> 1-1 = 0 ==> [1,-1]
"""

listik = [1,2,3,4,5]

def summ_first_and_last(a: list):
    while len(a) > 1:  # продолжать, пока длина списка больше 1
        b = a[0]
        c = a[-1]
        d = sum(a[1:-1])
        
        if b + c == d:
            break  # если сумма совпадает, прервать цикл
        else:
            a.pop(0)
            a.pop(-1)
    
    return a if len(a) > 1 else []


print(summ_first_and_last(listik)) 


"""
4 task
N наименьших элементов в исходном порядке
количество возвращаемых элементов не может быть больше длины списка;
элементы могут дублироваться;
в случае дубликатов достаточно вернуть их в исходном порядке (см. третий пример для большей наглядности).

Array	         N	 Expected
[1, 2, 3, 4, 5]	 3	[1, 2, 3]
[5, 4, 3, 2, 1]	 3	[3, 2, 1]
[1, 2, 3, 4, 1]	 3	[1, 2, 1]
[1, 2, 3, -4, 0] 3	[1, -4, 0]
[1, 2, 3, 4, 5]	 0	[]

"""
array = [1, 2, 3, 4, 5]

def minimum_nnumbers(lis: list, n: int):
    while len(lis) > n:
        lis.pop(lis.index(max(lis)))
    return lis

print(minimum_nnumbers(array, 3))


"""
5 task
В смешанном массиве числовых и строковых представлений целых чисел сложите целые числа, 
не являющиеся строками, и вычтите сумму целых чисел, являющихся строками.
Верните в виде числа.
"""

listik = ["234", 234, "12", 11, 98, 43, "567", "123"]

def sum_of_int_and_str(a: list) -> int:
    list_int_sum = []
    list_str_sum = []
    for i in a:
        if isinstance(i, (int, float)):
            list_int_sum.append(i)
        else:
            list_str_sum.append(int(i))
    return (sum(list_int_sum) - sum(list_str_sum))

print(sum_of_int_and_str(listik))

# second variant with using decorator
listik = ["234", 234, "12", 11, 98, 43, "567", "123", 550]

def list_int_sum(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        int_sum = 0
        for i in result:
            if isinstance(i, (int, float)):
                int_sum += i
        return int_sum
    return inner

def list_str_sum(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        str_sum = 0
        for i in result:
            if isinstance(i, str):
                str_sum += int(i)
        # Возвращаем список, чтобы он мог быть обработан следующим декоратором
        return result + [str_sum]
    return inner

@list_int_sum
@list_str_sum
def sum_of_int_and_str(a: list) -> list:
    return a

print(sum_of_int_and_str(listik))  # Ожидаемый результат: сумма всех чисел и чисел, представленных строками

"""
6 
Удалите из словаря d = {1: 1, '2': 2, '3': 3, 4: 4} все элементы со строковыми ключами. 
Помните, что изменение размеров словаря во время итерации может привести к ошибке, поэтому для работы используйте копию словаря.
"""

d = {1: 1, '2': 2, '3': 3, 4: 4}

print(d)

for key in d.copy():
    if isinstance(key, str):
        r = d.pop(key)
        print(r)

print(d)

"""
7
Задав строку слов, вы должны найти слово, набравшее наибольшее количество очков.
Каждая буква слова набирает очки в соответствии с ее положением в алфавите: a = 1, b = 2, c = 3 и т. д.
Например, оценка слова abad равна 8 (1 + 2 + 1 + 4).
Вам нужно вернуть слово, набравшее наибольшее количество баллов, в виде строки.
Если два слова набрали одинаковое количество баллов, верните слово, которое встречается раньше всех в исходной строке.
Все буквы будут строчными, а все вводимые данные - валидными.
"""

import string

text_for = "English texts for beginners to practice reading and comprehension online and for freeo."

class WorkWithStr():
    def __init__(self, a: str) -> None:
        self.a = a
        self.text = a.split()
        self.alphabet = string.ascii_lowercase
        self.points = {letter: index for index, letter in enumerate(self.alphabet, start=1)}
    
    def how_many_points(self):
        word_points = {}
        for word in self.text:
            total =sum(self.points.get(letter.lower(), 0) for letter in word)
            word_points[word] = total
        return word_points
    
lets_do_it = WorkWithStr(text_for)
a= lets_do_it.how_many_points()

max_value = max(a.values())
max_key = [key for key, value in a.items() if value == max_value]
print(f"{max_key}:{max_value}")

# sorted_a = dict(sorted(a.items(), key=lambda item: item[1]))  
# print(sorted_a)



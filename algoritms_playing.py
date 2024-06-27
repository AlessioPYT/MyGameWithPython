

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


"""
8
Метод toString() был отключен для булевых величин, чисел, массивов и объектов. 
Ваша цель - восстановить toString() для следующих типов данных.
"""

class ToString():
    def toString(self, value):
        if isinstance(value, (int, bool, float)):
            return str(value)
        return None
example = ToString()
print(example.toString(True))


"""
9 
Напишете декоратор функций @lazy(n), где n - частота "нормальных" запусков. 
Например, если n == 4, то после первого успешного запуска следующие три вызова этой функции не будут ничего делать, а на пятом запуске снова произойдет нормальный запуск. 
(Первый запуск всегда должен быть успешным, за исключением n == -1, который всегда ленив).
Однако если n - отрицательное число, то частота инвертируется (т. е. @lazy(-4) означает, что только каждый 4-й запуск будет ленивым, остальные - нормальными).
Если n == 1, то функция всегда должна быть нормальной, а если n == -1, то функция всегда должна быть ленивой. n == 0 никогда не будет проверяться.
Примечание: Когда ленивая функция "ничего не делает", это означает, что она немедленно возвращает None. Ни одна строка "нормальной" функции не должна выполняться.
"""

def lazy(func):
    def inner(*args, **kwargs):
        pass




"""
10
Если задана строка, удалите из нее все символы, которые являются уникальными.
Пример:
input: "abccdefee"
выход: "cceee"
"""




"""
11
Напишите функцию, которая принимает последовательность имен оленей и возвращает последовательность с именами оленей, отсортированных по фамилиям.
Примечания:
Гарантируется, что каждая строка состоит из двух слов.
В случае двух одинаковых фамилий сохраните исходный порядок
For this input:

[
  "Dasher Tonoyan", 
  "Dancer Moore", 
  "Prancer Chua", 
  "Vixen Hall", 
  "Comet Karavani",        
  "Cupid Foroutan", 
  "Donder Jonker", 
  "Blitzen Claus"
]
You should return this output:

[
  "Prancer Chua",
  "Blitzen Claus",
  "Cupid Foroutan", 
  "Vixen Hall", 
  "Donder Jonker", 
  "Comet Karavani",
  "Dancer Moore", 
  "Dasher Tonoyan",
]
"""




"""
12
Возвращает количество (count) гласных в заданной строке.
В этом Ката мы будем считать гласными буквы a, e, i, o, u (но не y).
Входная строка будет состоять только из строчных букв и/или пробелов.
"""

getCount = lambda s: sum(s.count(i) for i in 'aeiou') 


"""
13
Цель этого упражнения - преобразовать строку в новую строку, в которой каждый символ в новой строке будет "(", 
если этот символ встречается в исходной строке только один раз, или ")", 
если этот символ встречается в исходной строке более одного раза. 
При определении того, является ли символ дубликатом, игнорируйте капитализацию.
"""

def duplicate_encode(word):
    return "".join(")" if word.lower().count(c) > 1 else "(" for c in word.lower())


"""
14
Создайте программу, которая фильтрует список строк и возвращает список, в котором есть только имена ваших друзей.
Если в имени ровно 4 буквы, вы можете быть уверены, что это ваш друг! В противном случае вы можете быть уверены, что он не...
"""
text = ["Ryan", "Kieran", "Jason", "Yous"] # ["Ryan", "Yous"]
def friend(x):
    return filter(lambda name: len(name) == 4, x)


"""
15
словарь переделать в список
"""

dicti = {"age": 34, "name": "Alex", "city": "Kiev"}
dicti1 = [key for value in dicti.items() for key in value]

print(dicti1)


"""
16
Напишите функцию persistence, которая принимает положительный параметр num и возвращает его мультипликативную стойкость, 
то есть количество раз, которое нужно перемножить цифры в num, чтобы получить единственную цифру.
"""

def persistence(n):
    count = 0
    while n >= 10:  # пока число имеет больше одной цифры
        n = eval('*'.join(str(n)))  # умножаем все цифры числа
        count += 1  # увеличиваем счетчик шагов
    return count

# n = 39
# n_str = str(n)                  # Преобразуем число в строку: '39'
# joined_str = '*'.join(n_str)    # Объединяем цифры с '*': '3*9'
# result = eval(joined_str)       # Вычисляем строку как выражение: 27
# n = result                      # Присваиваем результат переменной n
# print(n)                        # Выводим результат: 27

text = 39
print(persistence(text))  # Output: 3


"""
17
Напишите функцию, которая принимает массив чисел (целые числа для тестов) и целевое число. 
Она должна находить в массиве два разных элемента, которые при сложении дают целевое значение. 
Индексы этих элементов должны быть возвращены в виде кортежа/списка (в зависимости от языка), например: (index1, index2).
"""

text = [1, 2, 3] # returns (0, 2) or (2, 0)
target = 4

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for a in range(i+1, len(numbers)):
            if numbers[i] + numbers[a] == target:
                return [i, a]
    return None

print(two_sum(text, target))

"""
18
В этом ката вы должны, получив строку, заменить каждую букву на ее место в алфавите.
Если что-то в тексте не является буквой, игнорируйте это и не возвращайте.
"""

import string
text = "The sunset sets at twelve o' clock."
# Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

class MyAlphabet():
    def __init__(self, text: str) -> None:
        self.text = text
        self.alphabet = string.ascii_lowercase
        self.letters = {letter: index for index, letter in enumerate(self.alphabet, start=1)}

    def alphabet_position(self):
        new_string = []
        for i in self.text.lower():
            if i in self.letters:
                new_string.append(str(self.letters[i]))
        return " ".join(new_string)

letsdoit = MyAlphabet(text)
print(letsdoit.alphabet_position())

"""
19
Напишите функцию, которая будет возвращать количество различных алфавитных символов и цифровых цифр, 
встречающихся во входной строке более одного раза без учета регистра. 
Предполагается, что входная строка содержит только алфавиты (как прописные, так и строчные) и числовые цифры.
"""

# 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

text = "nBVA7aDiPKkiTWKJTu"
def duplicate_count(text):
    text = text.lower()
    counter = {letter: text.count(letter) for letter in set(text)}
    new_list = [key for key, value in counter.items() if value > 1]    
    return len(new_list)

print(duplicate_count(text))

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])  # не мой способ, крутой способ жаль ума нехватила так написать


"""
20
Задав строку слов, вы должны найти слово, набравшее наибольшее количество очков.
Каждая буква слова набирает очки в соответствии с ее положением в алфавите: a = 1, b = 2, c = 3 и т. д.
Например, оценка слова abad равна 8 (1 + 2 + 1 + 4).
Вам нужно вернуть слово, набравшее наибольшее количество баллов, в виде строки.
Если два слова набрали одинаковое количество баллов, верните слово, которое встречается раньше всех в исходной строке.
Все буквы будут строчными, а все вводимые данные - валидными.
"""

import string

text = "man i need a taxi up to ubud"

def high(text):
    alphabet = string.ascii_lowercase
    points = {letter: point for point, letter in enumerate(alphabet, start=1)}
    result = max(text.split(), key=lambda word: sum(points.get(letter.lower(), 0) for letter in word)) # тут метод макс(1.кортеж, список, строку,,  кей= условия (в моем случае лямда))
    return result


"""
21
перевод даты в римские числа
"""

units = " I II III IV V VI VII VIII IX".split(" ")
tens = " X XX XXX XL L LX LXX LXXX XC".split(" ")
hundreds = " C CC CCC CD D DC DCC DCCC CM".split(" ")
thousands = " M MM MMM".split(" ")

def solution(n):
    return thousands[n//1000] + hundreds[n%1000//100] + tens[n%100//10] + units[n%10]



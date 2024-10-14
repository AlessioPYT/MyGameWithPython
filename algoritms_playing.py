

"""
1 task
I have a list and need to multiply every second number by two. or any other manipulation. I used a decorator to make it more complicated
"""

def generator(func):  # make a decor to select every second number and multiply it by 2.
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(1, len(result), 2):   #  REMEMBER !!!! it is the length of the list that is needed, not just the list.
            result[i] = result[i]*2
        return result
    return inner
                       
old_list = [1,2,3,4]
new_list = old_list[1::2]
new_list1 = old_list[0::2]

@generator  
def generate(old_list, new_list):  # now the main function that creates one list from two lists, embedding one into the other and not alternating them.
    new_list1 = [i for a in zip(old_list, new_list) for i in a]   # REMEMBER !!!!! i for a in zip(old_list, new_list) creates taple pairs (1,3), (2,4) for the second iteration we loop through the taple pairs and add them one by one to the list.
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

def sort_reindeer(reindeer_names: list):
    return sorted(reindeer_names, key=lambda s: s.split()[1]) # выполняется внутри лямбда-функции, чтобы извлечь второе слово в каждой строке


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

# и обратно

dicti1 = ["age", 34, "name", "Alex", "city", "Kiev"]

# Преобразуем обратно в словарь
keys = dicti1[::2]  # Каждое второе значение начиная с первого (ключи)
values = dicti1[1::2]  # Каждое второе значение начиная со второго (значения)

dicti = dict(zip(keys, values))


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

"""
22
сравнение букв с одной строки на наличие в другой
"""
def scramble(s1: str, s2: str) -> bool:
    return all(s1.count(char) >= s2.count(char) for char in set(s2)) # если в ОЛЛ уровнение правильное то вернет тру, внутри один счетчик больше другого по итерации уникальних сет значений

"""
23
волна букв, тоесть каждая буква по очереди становиться заглавной
"""

text = "hello" 
def wave(text: str):       
    return [text[:i] + text[i].upper() + text[i + 1:] for i in range(len(text)) if text[i].isalpha()]  # берем одну часть слова до нужного индекса + букву которую надо и добавляем остаток слова.
# Поскольку в строке нельзя поменять букву по индексу"""


"""
24
В этом ката ваша задача - создать все перестановки непустой входной строки и удалить дубликаты, если они есть.
With input 'a': Your function should return: ['a']
With input 'ab': Your function should return ['ab', 'ba']
With input 'abc': Your function should return ['abc','acb','bac','bca','cab','cba']
With input 'aabb': Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
"""
from itertools import permutations
s = ("abc")
def print_all_permutations(s: str):
    new_list = []
    perm = permutations(s) #составляет список из всех разных возможностей переставляя данные
    for p in perm:
        new_list.append(''.join(p))
    return list(set(new_list))

"""
25
Найти факториал и вичислить из него количество нулей
"""
from functools import reduce

def zeros(n):
    if n == 0:
        return 0
    a = reduce(lambda x, y: x * y, list(range(1, n+1)))  #функция вычисляет факторил, умножая по очереди все цыфры
    result = [int(i) for i in str(a)] # переводим в строку что бы посчитать количество нулей
    return result.count(0)

"""
26
выводить сумму всех чисел пока не будет одиночное число
"""
s = 493193  #  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(s):
    while s >= 10:
        s = eval("+".join(str(s))) # посчитай мне по знаку что я указываю результат в строке
    return s


"""
27
# ('Hello world !')     # elloHay orldway !
"""

text = ('Pig latin is cool') # igPay atinlay siay oolcay

def pig_it(text: str):  
    new_list = []
    for word in text.split():
        if word.isalpha():
            new_word = word[1:] + word[0] + "ay"
        else:
            new_word = word
        new_list.append(new_word) 
    return " ".join(new_list)

"""
28
нули в списке должны быть в конце
"""
def move_zeros(lst):
    new_list1 = []
    new_list2 = []
    for num in lst:
        if num == 0:
            new_list1.append(num)
        else:
            new_list2.append(num)
    return new_list2 + new_list1

"""
29

"""
arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
# get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88]

def get_larger_numbers(a, b):
    return [max(num) for num in zip(a, b)]

print(get_larger_numbers(arr1, arr2))

"""
30
"""
def add(*args):
    result = []
    try:
        for rows in zip(*args):
            sumall = [sum(elements) for elements in zip(*rows)]
            result.append(sumall)
            return result
    except:
        raise ValueError("Given matrices are not the same size.")

# Пример матриц для суммирования
mat1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
mat2 = [[2, -1, 3], [0, -2, 1], [4, -5, 6]]
mat3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

# Вызов функции с матрицами
add(mat1, mat2, mat3)


"""
31
[7]должно вернуться 7, потому что оно встречается 1 раз (что нечетно).
[0]должно вернуться 0, потому что оно встречается 1 раз (что нечетно).
[1,1,2]должно вернуться 2, потому что оно встречается 1 раз (что нечетно).
[0,1,0,1,0]должно вернуться 0, потому что оно встречается 3 раза (что нечетно).
[1,2,2,3,3,3,4,3,3,3,2,2,1]должно вернуться 4, потому что оно встречается 1 раз (что нечетно).
"""
from collections import Counter


def find_it(seq):
    a = Counter(seq)
    for key, value in a.items():
        if value % 2 != 0:
            return key



"""
32
calculator and test without class
"""
import pytest

class Calculator:

    def __init__(self, expression: str) -> None:
        self.expression = expression

    def calculate(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error: {e}"

class TestCalculate:

    def test_first(self):
        calc = Calculator("2+2")
        assert calc.calculate() == 4

    def test_second(self):
        calc = Calculator("150-140")
        assert calc.calculate() == 10

    def test_third(self):
        calc = Calculator("10*10")
        assert calc.calculate() == 100

    def test_fourth(self):
        calc = Calculator("200/100")
        assert calc.calculate() == 2

    def test_fiveth(self):
        calc = Calculator("10/0")
        assert "Error" in calc.calculate()

if __name__ == "__main__":
    pytest.main()

"""
33
n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1

n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k

n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""

def dig_pow(n, p):
    new_list = []
    for i in str(n):
        new_list.append(int(i)**p)  # перебираем 
        p += 1                       # добавляем счетчик
    return (sum(new_list) / n) if (sum(new_list) % n == 0) else -1  # возвращаем сумму поеделенную на н если сумма делить на это число без остатка


"""
34
piramida "*"
"""

def tower_builder(n_floors):
    for i in range(n_floors):
        spaces = ' ' * (n_floors - i - 1)
        stars = '*' * (2 * i + 1)
        print(list(spaces + stars))

"""
35 
способ пронумерировать словарь и вообще вывести буквы по ord() chr()
"""
print(ord("a"))
start = 1072
end = 1103
lett = [chr(x) for x in range(start, end)]
print(lett)
new_dict = {num: let for num, let in enumerate(lett, start=1)}
print(new_dict)

"""
36
рекурсия для обхода словаря и поиска необходимого значения
"""

users_dict = {
    'user_1': {'user_1_1': {'user_1_2': {'user_1_3': 'Maryna Viazovska'}}},'user_2': 'Lina Kostenko','user_3': {'user_3_1': 'Kateryna Bilokur'}}

a = users_dict.get("user_1").get("user_1_1").get("user_1_2").get("user_1_3")
b = users_dict.get("user_2")
c = users_dict.get("user_3").get("user_3_1")

print(a, b, c)

def some_func(d):
    new_list = []
    def rescui_items(d: dict):
        if isinstance(d, dict):
            for key, value in d.items():
                rescui_items(value)
        elif isinstance(d, list):
            for items in d:
                rescui_items(items)
        elif isinstance(d, set):
            for num in d:
                rescui_items(num)
        elif isinstance(d, str):
            if " " in d:
                new_list.append(d)
    rescui_items(d)
    return new_list
        
print(some_func(users_dict))

# второй вариант более гибкий и автоматизированый и принимает значение которое надо искать

def find_value(data, target):
    new_list = []
    if isinstance(data, dict):
        for key, value in data.items():
            new_list.extend(find_value(value, target))
            new_list.extend(find_value(key, target))
    elif isinstance(data, list):
        for it in data:
            new_list.extend(find_value(it, target))
    elif isinstance(data, str):
        if target in data:
            new_list.append(target)
    return new_list


"""
37
математические функции
"""
# seven(times(five()))  35
# four(plus(nine()))  13
# eight(minus(three()))  5
# six(divided_by(two()))  3


def zero(act=None): 
    if act:
        return act(0)
    return 0

def one(act=None): 
    if act:
        return act(1)
    return 1

def two(act=None): 
    if act:
        return act(2)
    return 2

def three(act=None): 
    if act:
        return act(3)
    return 3

def four(act=None): 
    if act:
        return act(4)
    return 4

def five(act=None): 
    if act:
        return act(5)
    return 5

def six(act=None): 
    if act:
        return act(6)
    return 6

def seven(act=None): 
    if act:
        return act(7)
    return 7

def eight(act=None): 
    if act:
        return act(8)
    return 8

def nine(act=None): 
    if act:
        return act(9)
    return 9

def plus(num): 
    return lambda x: x + num
def minus(num): 
    return lambda x: x - num
def times(num): 
    return lambda x: x * num
def divided_by(num): 
    return lambda x: int(x / num)

print(seven(divided_by(nine())))

"""
38
СОРТИРОВКА СЛОВАРЕЙ ПО КЛЮЧУ!!!

Это работает, потому что кортежи упорядочиваются, а кортежи упорядочиваются лексикографически 
(то есть они сортируются сначала по первым элементам, затем по вторым и так далее). 
Таким образом, мы эффективно сортируем кортежи из двух элементов по их ключам.
"""
counts = {"sandwiches": 10, "drinks": 20, "oranges": 7}

print(counts.items())
print(sorted(counts.items()))

def sorted_counts(a: dict):
    return dict(sorted(a.items()))

print(sorted_counts(counts))


"""
39
СОРТИРОВКА СЛОВАРЕЙ ПО ЗНАЧЕНИЮ!!!

Это работает, потому что в Python функции - это объекты.

Функция sorted опирается на тот факт, что мы можем передавать функции так же, как и любые другие объекты. 
Функция sorted будет вызывать заданный аргумент key, поэтому ключ должен быть функцией (или другим вызываемым объектом).
"""
# 1
# 1
counts = {"sandwiches": 10, "drinks": 20, "oranges": 7}
sorted_counts = {key: value for (value, key) in sorted((value, key) for (key, value) in counts.items())}

print(sorted_counts)

# 2
def value_of(item):
    """Return value given a (key, value) tuple."""
    key, value = item
    return value

for item in counts.items():
    print(value_of(item))

print(value_of(("sandwiches", 10)))

sorted_counts = dict(sorted(counts.items(), key=value_of))
print(sorted_counts)

"""
40
массив чисел и количество повторений даеться, вывести не больше количества повторений
"""
num = [1, 1, 3, 3, 7, 2, 2, 2, 2] # [1, 1, 3, 3, 7, 2, 2, 2]
qunt = 3 

def delete_nth(order,max_e):
    new_dict = {}
    new_list = []
    for i in order:
        if i not in new_dict:
            new_dict[i] = 0
        if new_dict[i] <= max_e:
            new_list.append(i)
            new_dict[i] += 1
    return new_list

"""
41
вичислить сумму каждого числа и отсортировать его, использовал декоратор для вычислении суммы и тренировки использования.
"""
rec = ("103 123 4444 99 2000") # "2000 103 123 4444 99"

def sum_numb(func):
    def inner(strng, *argы, **kwargы):
        def sum_numb(num):
            return sum(int(i) for i in num)
        result = func(strng, sum_numb)
        return result
    return inner

@sum_numb
def order_weight(strng: str, sum_numb):
    res = strng.split()
    res.sort(key=lambda x: (sum_numb(x), x))
    return " ".join(res)

print(order_weight(rec))

"""
42
ДЕКОРАТОР!!!
"""
import time

"""
        1. Сумма чисел: Напишите функцию, которая принимает два числа и возвращает их сумму. 
        Добавьте проверку, чтобы убедиться, что оба аргумента являются числами.
"""

def check(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if all(isinstance(i, int) for i in args):
            return result
        else:
            return f"please enter int"
    return inner

@check
def sumari(a, b):
    return a + b 
print(sumari(2, 3))


"""
        2. Факториал: Напишите функцию, которая принимает одно число и возвращает его факториал. 
        Учтите, что факториал отрицательного числа не определен.
"""

def facto(func):
    def inner(*args):
        n = args[0]
        if n == 0 or n == 1:
            return 1
        return func(*args)
    return inner

@facto
def factorial(n):
    return n * factorial(n - 1)
    
print(factorial(5))

"""
        3. Палиндром: Напишите функцию, которая принимает строку и возвращает True, 
        если она является палиндромом (читается одинаково с обеих сторон), 
        и False в противном случае.
"""

def some_decor(func):
    def inner(*args):
        s = args[0]
        if isinstance(s, str):
            if s == s[::-1]:
                return func(*args)
            else:
                return False
    return inner

@some_decor
def palindrom(s: str) -> str:
    return f"This is palindrom {s}"

print(palindrom("asa"))


"""
        4 Декоратор для замера времени: Напишите декоратор, который измеряет время выполнения функции и выводит его на экран. 
        Примените этот декоратор к функции, которая вычисляет сумму всех чисел от 1 до N.
"""

def to_do_it(name: str):
    def time_to_action(func):
        def inner(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            print(f"{name} duration: {duration:.6f} seconds")
            return result
        return inner
    return time_to_action

@to_do_it("Summing all numbers")
def summ_all(n):
    if n <= 0:
        return f"It must be > 0, got {n}."
    elif n == 1:
        return 1 
    else:
        return n + summ_all(n - 1)

print(summ_all(20)) 

"""
        5. Декоратор с параметрами: Напишите декоратор, который принимает параметр num_repeats. 
        Этот декоратор должен вызывать обернутую функцию num_repeats раз и выводить результат выполнения. 
        Примените этот декоратор к функции, которая возвращает случайное число.
"""

from random import randint


def num_repaets(quant: int):
    def wrapper(func):
        def inner():
            for _ in range(quant):
                res = func()
                print(res)
            return res
        return inner
    return wrapper

@num_repaets(4)
def rand_int():
    return randint(1, 100)

print(rand_int())


"""
43  баловоство с ООП и датасловари
"""

from collections import UserDict
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class Product(UserDict):

    def __init__(self, name: str, price: int):
        logger.info("recieved product")
        super().__init__()
        self.name = name
        self.price = price
        self.data[self.name] = self.price

    def __str__(self) -> str:
        logger.info("return product")
        return f"Product: {self.name}, Price: {self.price}"
    
    def __eq__(self, other):
        logger.info("hesh 1")
        return self.name == other.name and self.price == other.price

    def __hash__(self):
        logger.info("hesh 2")
        return hash((self.name, self.price))  # Используем кортеж для хэширования
    
class Cart(UserDict):

    def __init__(self):
        super().__init__()

    def add_product(self, product: Product, quantity: int):
        logger.info("in cart was add")
        self.data[product] = quantity

    def remove_product(self, product: Product):
        logger.info("from cart was removed")
        self.data.pop(product, None)  # Безопасное удаление продукта

    def get_total_price(self):
        logger.info("recieved to total price")
        total = 0
        for product, quantity in self.data.items():
            total += product.price * quantity  # Рассчитываем общую цену
        return total

    def __str__(self) -> str:
        logger.info("work str in cart")
        if not self.data:  # Если корзина пуста
            return "Cart is empty"
        result = ""
        for product, quantity in self.data.items():
            result += f"Product: {product.name}, quantity: {quantity}\n"
        return result.strip()  # Возвращаем результат без лишних переносов строки

    def is_product_available(self, prod):
        product = Product
        if prod in product.name and Cart.data:
            return True

class TestStart:
    pass


if __name__ == "__main__":
    product1 = Product("apple", 45)
    product2 = Product("banan", 59)
    cart = Cart()
    cart.add_product(product1, 10)
    cart.add_product(product2, 23)
    print(product1)
    print(product2)
    print(cart)
    print(cart.get_total_price())


"""
44. Анализ текстового файла
Описание: Напишите программу, которая считывает текстовый файл и выполняет анализ текста.

Программа должна:
Подсчитать общее количество слов и предложений в файле.
Найти 5 самых частых слов и их частоту.
Для каждого предложения вернуть длину предложения (количество слов) и сам текст предложения.
Данные:

Используйте строку для обработки текста.
Используйте список для хранения слов и длины предложений.
Используйте словарь для подсчета частоты слов.
Результаты должны быть возвращены в виде словаря.
"""

from typing import Any
from collections import Counter
import string

class CreateFile:

    def __init__(self, file_name: str, mode_file: str = "r") -> None:
        self.name_file = file_name
        self.mode_file = mode_file
        self.file = open(self.name_file, self.mode_file)

    def __getattribute__(self, attr) -> Any:
        if attr in ['name_file', 'mode_file', 'file']:
            return object.__getattribute__(self, attr)
        return getattr(self.file, attr)
    
    def __enter__(self):
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Exception caught: {exc_type}, {exc_value}")
        self.file.close()
        return True

    def close(self):
        if self.file:
            self.file.close()
    
    def __del__(self):
        self.close()  # Закрываем файл при удалении объекта


class MetodsWithFile:
    
    def __init__(self, file: CreateFile) -> None:
        self.file = file
        self.text = self.file.read() # Читаем содержимое файла один раз и сохраняем его в переменной

    def total_words(self):
        words = self.text.split()
        cleaned_words = [word.strip(string.punctuation) for word in words]
        word_count = len(cleaned_words)
        return word_count


    def often_words(self):
        res = Counter(self.text.split())  # Подсчитываем количество вхождений слов
        new_list = [key for key, value in res.items() if value >= 5]  # Добавляем слова, встречающиеся 5 и более раз
        return new_list

    def len_text(self):
        return len(self.text.split("."))

if __name__ == "__main__":
    example = CreateFile("new_text.txt", "r")
    manip = MetodsWithFile(example)
    print(manip.total_words())
    print(manip.often_words())
    print(manip.len_text())

"""
45 Просто класс при инит открывает джейсон файл потом пара манипуляций и сохранения
практика 
"""

import json
import logging

class DataManager:

    def __init__(self, data, mode = "r") -> None:
        self.filepath = data
        self.mode = mode
        try:
            with open(self.filepath, "r") as file:
                self.data = json.load(file)
                logging.info("its ok")
        except json.JSONDecodeError as e:
            logging.exception(f"Ошибка при загрузке JSON: {e}")
        except FileNotFoundError as e:
            logging.exception(f"Файл не найден: {e}")
        except Exception as e:
            logging.exception(f"Произошла ошибка: {e}")
        
        
    def add_person(self, name, *grades):
        new_name = {"name": name, "grades": {'math': grades[0], 'history': grades[1], 'physics': grades[2]}}
        self.data.append(new_name)
        logging.info(f"{new_name} was added in {self.data}")


    def update_person_info(self, name, what, info):
        for person in self.data:
            if what == "name":
                person["name"] = info
            elif what == 'math' and person["name"] == name:
                person["grades"]["math"] = info
            elif what == 'history' and name == person["name"]:
                person[name]["grades"]["history"] = info
            elif what == 'physics' and name == person["name"]:
                person[name]["grades"]["physics"] = info
        logging.info(f"info about {person} was updated")



    def get_person_contacts(self, name):
        for person in self.data:
            if person["name"] == name:
                logging.info(f"info about {person}")
                return person

    def get_projects(self, name):
        for person in self.data:
            if name == person["name"]:
                result = person["grades"]
                logging.info(f"info about {name} is {result}")
                return result
                
       

    def analyze_data(self, name):
        for person in self.data:
            if name == person["name"]:
                result = [person.get("grades").get("math"), person.get("grades").get("history"), person.get("grades").get("physics")]
                logging.info(f"Several makr for {name} - {sum(result) / len(result)}")

    def save_update(self):
        try:
            with open(self.filepath, "w") as file:
                json.dump(self.data, file, indent=4)
                logging.info(f"Saving succesfull")
        except Exception as e:
            logging.exception(f"was error {e}")



if __name__ == "__main__":
    logging.basicConfig(
        filename='app.log',  
        level=logging.DEBUG,  # for all levels
        format='%(asctime)s - %(levelname)s - %(message)s' 
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Уровень логирования для консоли
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)


    logging.getLogger().addHandler(console_handler)
    example = DataManager("new_text.json")
    example.add_person("Alex", 80, 90, 90)
    # example.update_person_info("Alex", "math", 50)
    # example.get_person_contacts("Charlie")
    example.get_projects("Charlie")
    example.analyze_data("Charlie")
    # example.save_update()


"""
46 Если ты хочешь, чтобы все необработанные ошибки автоматически попадали в логи, 
ты можешь использовать специальную настройку, например, с использованием sys.excepthook.
Таким образом, даже если ты не логируешь ошибки вручную, они могут быть записаны в лог через глобальный обработчик ошибок.
"""

import logging
import sys

logging.basicConfig(level=logging.ERROR)

def handle_exception(exc_type, exc_value, exc_traceback):
    if not issubclass(exc_type, KeyboardInterrupt):
        logging.error("Необработанное исключение", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception

# Пример ошибки
1 / 0  # Это вызовет ZeroDivisionError и автоматически попадет в лог


"""
47 Asyncio and Pytest
"""

import pytest
import asyncio
from random import randint
import logging
import functools

logging.basicConfig(filename="new_app.log", level=logging.INFO, format='%(asctime)s - %(message)s')

def log_execution(func):
    @functools.wraps(func)
    async def inner(*args, **kwargs):
        logging.info(f"Executing {func.__name__}")
        result = await func(*args, **kwargs)
        logging.info(f"Finished {func.__name__}")
        return result
    return inner

def rand_int():
    a = randint(1, 6)
    logging.info(f"info for testing {a}")
    return a

@log_execution
async def calculate():
    await asyncio.sleep(randint(1, 3))  # Simulate 
    return 4

@log_execution
async def first():
    await asyncio.sleep(randint(1, 3))  
    return 3

@pytest.mark.asyncio
async def test_concurrent_execution():
   
    results = await asyncio.gather(
        calculate(),
        first(),
    )
    logging.info(f"Results: {results}")

if __name__ == "__main__":
    pytest.main()

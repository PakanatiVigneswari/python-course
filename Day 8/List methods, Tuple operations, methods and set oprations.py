Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[55,67,89,56,54,32,879,4,89]
l.pop()
89
l.pop()
4
l.pop(0)
55
l.pop(3)
54
l.remove(67)
l
[89, 56, 32, 879]
l.remove(56)
l
[89, 32, 879]
l.clear()
l
[]
l=[56,54,89,54,132,87,54,89,54]
count(54)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(54)
NameError: name 'count' is not defined. Did you mean: 'round'?
l
[56, 54, 89, 54, 132, 87, 54, 89, 54]
l.count(54)
4
l.index(89)
2
l.index(54)
1
l.index(54)
1
sorted()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    sorted()
TypeError: sorted expected 1 argument, got 0
sorted(l)
[54, 54, 54, 54, 56, 87, 89, 89, 132]
reverse(l)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    reverse(l)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
reversed(l)
<list_reverseiterator object at 0x00000211FCE2EC20>
l.reverse()
l
[54, 89, 54, 87, 132, 54, 89, 54, 56]
sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    sort(reverse=True)
NameError: name 'sort' is not defined
l.sort(reverse=True)
l
[132, 89, 89, 87, 56, 54, 54, 54, 54]
a
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a
NameError: name 'a' is not defined
a=[1,2]
c=a
c
[1, 2]
c.append(4)
c
[1, 2, 4]
a
[1, 2, 4]
a.append(3)
a
[1, 2, 4, 3]
c
[1, 2, 4, 3]
b=a.copy()
b
[1, 2, 4, 3]
b.append(13)
b
[1, 2, 4, 3, 13]
a
[1, 2, 4, 3]
any(l)
True
all(l)
True
l
[132, 89, 89, 87, 56, 54, 54, 54, 54]
any(l)
True
all(l)
True
l.append(0)
l
[132, 89, 89, 87, 56, 54, 54, 54, 54, 0]
any(l)
True
all(l)
False
k=[0,0.8,'',]
any(k)
True
all(k)
False
j=[0,0.0,'']
any(j)
False
all(j)
False

"""
Tuple
"""
'\nTuple\n'
t=()
t=tuple()
t=tuple((1,2,3))
t
(1, 2, 3)
type(t)
<class 'tuple'>
t=(1)
t
1
type(t)
<class 'int'>
t=(1,)
type(t)
<class 'tuple'>
t=(1,4,56,8,7,8)
t
(1, 4, 56, 8, 7, 8)
t=(1,4,6,'gfdg',[5,6,87,9],(1,2,4,5),{4,78,89,56,7},{1:3,2:"Krishna Ram",5:6},True)
t
(1, 4, 6, 'gfdg', [5, 6, 87, 9], (1, 2, 4, 5), {4, 7, 56, 89, 78}, {1: 3, 2: 'Krishna Ram', 5: 6}, True)
type(t)
<class 'tuple'>
t=(1,5,7,9)
t
(1, 5, 7, 9)
a,b,c,d=t
a
1
b
5
c
7
d
9
a,b,c,d=(1,2,4,5)
a
1
b
2
c
4
d
5
t=(1,1.2,"Krishna",[4,5,7,8],{1,3,4,6,9},(5,8,95,6),{1:2,3:6,4:7},True)
t
(1, 1.2, 'Krishna', [4, 5, 7, 8], {1, 3, 4, 6, 9}, (5, 8, 95, 6), {1: 2, 3: 6, 4: 7}, True)
len(t)
8
t[3]
[4, 5, 7, 8]
t[3].append(l)
t
(1, 1.2, 'Krishna', [4, 5, 7, 8, [132, 89, 89, 87, 56, 54, 54, 54, 54, 0]], {1, 3, 4, 6, 9}, (5, 8, 95, 6), {1: 2, 3: 6, 4: 7}, True)
t[3].remove(l)
t
(1, 1.2, 'Krishna', [4, 5, 7, 8], {1, 3, 4, 6, 9}, (5, 8, 95, 6), {1: 2, 3: 6, 4: 7}, True)
t[3].append(34)
t
(1, 1.2, 'Krishna', [4, 5, 7, 8, 34], {1, 3, 4, 6, 9}, (5, 8, 95, 6), {1: 2, 3: 6, 4: 7}, True)
len(t)
8
a=(3,5,6,7,9,56)
b=(2,3,5,7,9,2)
a+b
(3, 5, 6, 7, 9, 56, 2, 3, 5, 7, 9, 2)
a*2
(3, 5, 6, 7, 9, 56, 3, 5, 6, 7, 9, 56)
a
(3, 5, 6, 7, 9, 56)
t
(1, 1.2, 'Krishna', [4, 5, 7, 8, 34], {1, 3, 4, 6, 9}, (5, 8, 95, 6), {1: 2, 3: 6, 4: 7}, True)
t[2]
'Krishna'
t[-1]
True
t[-4]
{1, 3, 4, 6, 9}
t[4]
{1, 3, 4, 6, 9}
t[1]
1.2
t[3:6]
([4, 5, 7, 8, 34], {1, 3, 4, 6, 9}, (5, 8, 95, 6))
t[::-1]
(True, {1: 2, 3: 6, 4: 7}, (5, 8, 95, 6), {1, 3, 4, 6, 9}, [4, 5, 7, 8, 34], 'Krishna', 1.2, 1)
t[-2:]
({1: 2, 3: 6, 4: 7}, True)
t[-4:]
({1, 3, 4, 6, 9}, (5, 8, 95, 6), {1: 2, 3: 6, 4: 7}, True)
t
(1, 1.2, 'Krishna', [4, 5, 7, 8, 34], {1, 3, 4, 6, 9}, (5, 8, 95, 6), {1: 2, 3: 6, 4: 7}, True)
1 in t
True
1.1 not in t
True
1.2 not in t
False
[4,5,7,8,34] in t
True
t=(64,87,34,87,5,97,8)
t
(64, 87, 34, 87, 5, 97, 8)
len(t)
7
sorted(t)
[5, 8, 34, 64, 87, 87, 97]
min(t)
5
max(t)
97
t.count(87)
2
t.index(29)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    t.index(29)
ValueError: tuple.index(x): x not in tuple
t.index(34)
2
t.find(29)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    t.find(29)
AttributeError: 'tuple' object has no attribute 'find'
any(t)9
SyntaxError: invalid syntax
all(t)
True
any(y)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    any(y)
NameError: name 'y' is not defined
any(t)
True
all(t)
True
t
(64, 87, 34, 87, 5, 97, 8)
sum(t)
382
s={}
type(s)
<class 'dict'>
s=set()
type(s)
<class 'set'>
s={1,3,5,6,7,1}
s
{1, 3, 5, 6, 7}
s={2,4,5,6,6,6,8}
s
{2, 4, 5, 6, 8}
# Unorder, Unique, Mutable, Hetrogenious with some conditions that is we can only add immutable elements inside set we can't add mutable elements(list, set, dictnary) inside list), dynamically sized.
s={1,1,1,1,1,1,2}
s
{1, 2}
s=set()
a.add(1)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    a.add(1)
AttributeError: 'tuple' object has no attribute 'add'
s.add(1)
s
{1}
s.add(1.2)
s
{1, 1.2}
s.add("Krishna")
s
{1, 'Krishna', 1.2}
s.add(2+3j)
s
{1, (2+3j), 'Krishna', 1.2}
s.add((1,2,3))
s
{1, 'Krishna', 1.2, (2+3j), (1, 2, 3)}
s.add(True)
s
{1, 'Krishna', 1.2, (2+3j), (1, 2, 3)}
s.add([2,4,5])
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    s.add([2,4,5])
TypeError: unhashable type: 'list'
s.add({67,34,67,7})
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    s.add({67,34,67,7})
TypeError: unhashable type: 'set'
s.add({6:4,4:5,3:8})
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    s.add({6:4,4:5,3:8})
TypeError: unhashable type: 'dict'
s
{1, 'Krishna', 1.2, (2+3j), (1, 2, 3)}
s.add(False)
s
{False, 1, 'Krishna', 1.2, (2+3j), (1, 2, 3)}
s.add(True)
s
{False, 1, 'Krishna', 1.2, (2+3j), (1, 2, 3)}
a={1,2,3,4,5}
b={4,5,6,7,8}
a+b
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a*4
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    a*4
TypeError: unsupported operand type(s) for *: 'set' and 'int'
a
{1, 2, 3, 4, 5}
b
{4, 5, 6, 7, 8}
4 in a
True
7 not in a
True
a
{1, 2, 3, 4, 5}
b
{4, 5, 6, 7, 8}
a|b
{1, 2, 3, 4, 5, 6, 7, 8}
a&b
{4, 5}
a^b
{1, 2, 3, 6, 7, 8}
a-b
{1, 2, 3}
a
{1, 2, 3, 4, 5}
b
{4, 5, 6, 7, 8}
>>> a.isdisjoint(b)
False
>>> aisdisjoint({99,100})
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    aisdisjoint({99,100})
NameError: name 'aisdisjoint' is not defined
>>> a.isdisjoint({99,100})
True
>>> a
{1, 2, 3, 4, 5}
>>> {5}.issubset(a)
True
>>> {100,99}.issubset(a)
False
>>> a.issubset
<built-in method issubset of set object at 0x00000211FCE11460>
>>> a.issubet(b)
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    a.issubet(b)
AttributeError: 'set' object has no attribute 'issubet'. Did you mean: 'issubset'?
>>> a.issubset(b)
False
>>> a.issuperset(b)
False
>>> {1,2,3,4,5,6,7,8,9,10}.issuperset(a)
True

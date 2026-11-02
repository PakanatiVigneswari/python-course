Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={34,56,89,54,54,32}
sorted
<built-in function sorted>
sorted(s)
[32, 34, 54, 56, 89]
len(s)
5
max(s)
89
min(s)
32
sum(s)
265
any(s)
True
all(s)
True
s
{32, 34, 54, 56, 89}
s.add(1)
s
{32, 1, 34, 54, 56, 89}

s.add(100)
s
{32, 1, 34, 100, 54, 56, 89}
s.update({10,20,30})
s
{32, 1, 34, 100, 10, 20, 54, 56, 89, 30}
s.pop()
32
s.pop(2)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.pop(2)
TypeError: set.pop() takes no arguments (1 given)
s.remove(34)
s
{1, 100, 10, 20, 54, 56, 89, 30}
s.remove(200)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s.remove(200)
KeyError: 200
s.discard(200)
s
{1, 100, 10, 20, 54, 56, 89, 30}
 s.clear
 
SyntaxError: unexpected indent
s.clear()
s
set()
a={1,2,3,4,5,6}
a
{1, 2, 3, 4, 5, 6}
b=a
b
{1, 2, 3, 4, 5, 6}
a
{1, 2, 3, 4, 5, 6}
b.add(7)
b
{1, 2, 3, 4, 5, 6, 7}
a
{1, 2, 3, 4, 5, 6, 7}
c=a.copy()
c.add(20)
c
{1, 2, 3, 4, 5, 6, 7, 20}
a
{1, 2, 3, 4, 5, 6, 7}
d={]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
"""
Dictionary
"""
'\nDictionary\n'
d={}
type(d)
<class 'dict'>
d={1:2,3:6}
type(d)
<class 'dict'>
#Mutable, dynamically sized, Ordered, Hetrogenious, uk
d
{1: 2, 3: 6}
d={}
d[1]='int'
d
{1: 'int'}
d[1:1]='float'
d
{1: 'int', slice(1, 1, None): 'float'}
d['str']='str'
d
{1: 'int', slice(1, 1, None): 'float', 'str': 'str'}
s
set()
d
{1: 'int', slice(1, 1, None): 'float', 'str': 'str'}
d[2+4j]='complex'
d
{1: 'int', slice(1, 1, None): 'float', 'str': 'str', (2+4j): 'complex'}
d[(1,2,3)]='tuple'
d
{1: 'int', slice(1, 1, None): 'float', 'str': 'str', (2+4j): 'complex', (1, 2, 3): 'tuple'}
d[True]='bool'
d
{1: 'bool', slice(1, 1, None): 'float', 'str': 'str', (2+4j): 'complex', (1, 2, 3): 'tuple'}
d[1.1]='float'
d
{1: 'bool', slice(1, 1, None): 'float', 'str': 'str', (2+4j): 'complex', (1, 2, 3): 'tuple', 1.1: 'float'}
d[False]='bool'
d
{1: 'bool', slice(1, 1, None): 'float', 'str': 'str', (2+4j): 'complex', (1, 2, 3): 'tuple', 1.1: 'float', False: 'bool'}
d[[1,2,3]]='lis'
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d[[1,2,3]]='lis'
TypeError: unhashable type: 'list'
d[{1,2}]='set'
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    d[{1,2}]='set'
TypeError: unhashable type: 'set'
d[{1:1,2:2}]='dict'
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    d[{1:1,2:2}]='dict'
TypeError: unhashable type: 'dict'
d
{1: 'bool', slice(1, 1, None): 'float', 'str': 'str', (2+4j): 'complex', (1, 2, 3): 'tuple', 1.1: 'float', False: 'bool'}
d[1]=1
d
{1: 1, slice(1, 1, None): 'float', 'str': 'str', (2+4j): 'complex', (1, 2, 3): 'tuple', 1.1: 'float', False: 'bool'}
d.clear()
d
{}
d[1]=1
d[2]=1.2
d[3]=23+6j
d[4]='Krishna'
d[5]=[1,2]
d[6]=(1,2)
d[7]={1,2}
d[8]={1:2,2:"Ram"}
d[9]=True
d[10]=False
d
{1: 1, 2: 1.2, 3: (23+6j), 4: 'Krishna', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 'Ram'}, 9: True, 10: False}
d[10]=1
d[11]=1
d[12]=1
d
{1: 1, 2: 1.2, 3: (23+6j), 4: 'Krishna', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 'Ram'}, 9: True, 10: 1, 11: 1, 12: 1}
d[2]
1.2
d[6]
(1, 2)
d[8]
{1: 2, 2: 'Ram'}
d[3]
(23+6j)
d[4]
'Krishna'
d[5]
[1, 2]
d[20]
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    d[20]
KeyError: 20
d
{1: 1, 2: 1.2, 3: (23+6j), 4: 'Krishna', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 'Ram'}, 9: True, 10: 1, 11: 1, 12: 1}
d.get(20)
d
{1: 1, 2: 1.2, 3: (23+6j), 4: 'Krishna', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 'Ram'}, 9: True, 10: 1, 11: 1, 12: 1}
d.get(4)
'Krishna'
d.get[3]
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    d.get[3]
TypeError: 'builtin_function_or_method' object is not subscriptable
d.get(3)
(23+6j)
d.get(16,'key is not there')
'key is not there'
d.get(2,'key is not there')
1.2
d.get(1)
1
1
1
2 in dictionary
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    2 in dictionary
NameError: name 'dictionary' is not defined
2 in d
True
1.2 in d
False
3 in d
True
4 in d
True
d
{1: 1, 2: 1.2, 3: (23+6j), 4: 'Krishna', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 'Ram'}, 9: True, 10: 1, 11: 1, 12: 1}
d[5]="Govinda"
d
{1: 1, 2: 1.2, 3: (23+6j), 4: 'Krishna', 5: 'Govinda', 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 'Ram'}, 9: True, 10: 1, 11: 1, 12: 1}
d[3]=3.6
d
{1: 1, 2: 1.2, 3: 3.6, 4: 'Krishna', 5: 'Govinda', 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 'Ram'}, 9: True, 10: 1, 11: 1, 12: 1}
d[3]="Krishna"
d
{1: 1, 2: 1.2, 3: 'Krishna', 4: 'Krishna', 5: 'Govinda', 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 'Ram'}, 9: True, 10: 1, 11: 1, 12: 1}
d[13]=100
d
{1: 1, 2: 1.2, 3: 'Krishna', 4: 'Krishna', 5: 'Govinda', 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 'Ram'}, 9: True, 10: 1, 11: 1, 12: 1, 13: 100}
d[36]=500
d
{1: 1, 2: 1.2, 3: 'Krishna', 4: 'Krishna', 5: 'Govinda', 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 'Ram'}, 9: True, 10: 1, 11: 1, 12: 1, 13: 100, 36: 500}
d.update({15:"Shyam",67:76765567})
d
{1: 1, 2: 1.2, 3: 'Krishna', 4: 'Krishna', 5: 'Govinda', 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 'Ram'}, 9: True, 10: 1, 11: 1, 12: 1, 13: 100, 36: 500, 15: 'Shyam', 67: 76765567}
d.popitem()
(67, 76765567)
d.pop(1)
1
d.pop(67)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    d.pop(67)
KeyError: 67
d.pop(6)
(1, 2)
del d[7]
d
{2: 1.2, 3: 'Krishna', 4: 'Krishna', 5: 'Govinda', 8: {1: 2, 2: 'Ram'}, 9: True, 10: 1, 11: 1, 12: 1, 13: 100, 36: 500, 15: 'Shyam'}
del d[36]
d
{2: 1.2, 3: 'Krishna', 4: 'Krishna', 5: 'Govinda', 8: {1: 2, 2: 'Ram'}, 9: True, 10: 1, 11: 1, 12: 1, 13: 100, 15: 'Shyam'}
d.clear()
d
{}
d
{}
d.keys()
dict_keys([])
d={1:4,2:"Krishna",5:56+7j,6:1,9:1}
d.keys()
dict_keys([1, 2, 5, 6, 9])
d.values()
dict_values([4, 'Krishna', (56+7j), 1, 1])
d.items()
dict_items([(1, 4), (2, 'Krishna'), (5, (56+7j)), (6, 1), (9, 1)])
len(d)
5
sorted(d)
[1, 2, 5, 6, 9]
max(d)
9
min(d)
1
a={1:1,2:2}
b=a
b[3]=3
a
{1: 1, 2: 2, 3: 3}
b
{1: 1, 2: 2, 3: 3}
c=a.copy()
c[4]=4
c
{1: 1, 2: 2, 3: 3, 4: 4}
>>> a
{1: 1, 2: 2, 3: 3}
>>> d=dict.fromkeys(["a","b","c","d","e"],0)
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
>>> d.setdefault('a')
0
>>> d.setdefault('h')
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None}
>>> d.setdefault('k',1)
1
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None, 'k': 1}
>>> d.setdefault('c',1)
0
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None, 'k': 1}
>>> s=frozenset({1,2,3,4,5})
>>> len(s)
5
>>> max(s)
5
>>> min(s)
1
>>> type(s)
<class 'frozenset'>

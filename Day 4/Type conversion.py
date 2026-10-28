Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
int(a)
10
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
b=20.2
int(b)
20
float(b)
20.2
str(b)
'20.2'
complex(b)
(20.2+0j)
bool(b)
True
list(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
a="Krishna"
int(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'Krishna'
float(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(a)
ValueError: could not convert string to float: 'Krishna'
str(a)
'Krishna'
complex(a)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    complex(a)
ValueError: complex() arg is a malformed string
bool(a)
True
list(a)
['K', 'r', 'i', 's', 'h', 'n', 'a']
tuple(a)
('K', 'r', 'i', 's', 'h', 'n', 'a')
set(a)
{'K', 'i', 'r', 'n', 's', 'h', 'a'}
dict(a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
e='2314'
int(e)
2314
float(e)
2314.0
str(e)
'2314'
complex(e)
(2314+0j)
bool(e)
True
list(e)
['2', '3', '1', '4']
set(e)
{'1', '4', '3', '2'}
tuple(e)
('2', '3', '1', '4')
dict(e)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    dict(e)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
f=10+2j
int(f)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int(f)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(f)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    float(f)
TypeError: float() argument must be a string or a real number, not 'complex'
str(f)
'(10+2j)'
complex(f)
(10+2j)
bool(f)
True
list(f)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    list(f)
TypeError: 'complex' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    set(f)
TypeError: 'complex' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    tuple(f)
TypeError: 'complex' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dict(f)
TypeError: 'complex' object is not iterable
g=[1,23,4,56]
int(g)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(g)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(g)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    float(g)
TypeError: float() argument must be a string or a real number, not 'list'
str(g)
'[1, 23, 4, 56]'
complex(g)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    complex(g)
TypeError: complex() first argument must be a string or a number, not 'list'
bool(g)
True
list(g)
[1, 23, 4, 56]
set(g)
{56, 1, 4, 23}
tuple(g)
(1, 23, 4, 56)
dict(g)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    dict(g)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
h={1,34,4, 56}
int(h)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int(h)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(h)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    float(h)
TypeError: float() argument must be a string or a real number, not 'set'
str(h)
'{56, 1, 34, 4}'
complex(h)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    complex(h)
TypeError: complex() first argument must be a string or a number, not 'set'
bool(h)
True
list(h)
[56, 1, 34, 4]
set(h)
{56, 1, 34, 4}
tuple(h)
(56, 1, 34, 4)
dict(h)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    dict(h)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
i=(1,23,6,87)
int(i)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    int(i)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(i)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    float(i)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(i)
'(1, 23, 6, 87)'
complex(i)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    complex(i)
TypeError: complex() first argument must be a string or a number, not 'tuple'
bool(i)
True
list(i)
[1, 23, 6, 87]
set(i)
{1, 87, 6, 23}
tuple(i)
(1, 23, 6, 87)
dict(i)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    dict(i)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
j={1:'Krishna',2:"Ram",3:'Shiva',4:'Govinda'}
int(j)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    int(j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(j)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    float(j)
TypeError: float() argument must be a string or a real number, not 'dict'
str(j)
"{1: 'Krishna', 2: 'Ram', 3: 'Shiva', 4: 'Govinda'}"
complex(j)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    complex(j)
TypeError: complex() first argument must be a string or a number, not 'dict'
bool(j)
True
list(j)
[1, 2, 3, 4]
set(j)
{1, 2, 3, 4}
tuple(j)
(1, 2, 3, 4)
dict(j)
{1: 'Krishna', 2: 'Ram', 3: 'Shiva', 4: 'Govinda'}
k=True
int(k)
1
float(k)
1.0
str(k)
'True'
complex(k)
(1+0j)
bool(k)
True
list(k)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    list(k)
TypeError: 'bool' object is not iterable
>>> tuple(k)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    tuple(k)
TypeError: 'bool' object is not iterable
>>> set(k)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    set(k)
TypeError: 'bool' object is not iterable
>>> dict(k)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    dict(k)
TypeError: 'bool' object is not iterable
>>> a=20
>>> int(a)
20
>>> '''
... int -> float, complex, str, bool
... float -> int, complex, str, bool
... str(names) -> str, bool, list, set, tuple
... str(numbers) -> int, float, str, bool, complex, list, set, tuple
... complex -> int, float, str, bool
... bool -> int, float, str, complex
... list -> st, tuple, set, bool
... set -> list, tuple, str, bool
... tuple -> str, list, set, bool

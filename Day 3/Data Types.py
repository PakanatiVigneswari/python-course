Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=123
>>> type(a)
<class 'int'>
>>> b=1.23
>>> type(b)
<class 'float'>
>>> c=2+4j
>>> type(c)
<class 'complex'>
>>> d="Python"
>>> type(d)
<class 'str'>
>>> e=[1,2,3]
>>> type(e)
<class 'list'>
>>> id(e)
2371470300352
>>> e.append(12)
>>> print(e)
[1, 2, 3, 12]
>>> id(e)
2371470300352
>>> e.extend([20,30])
>>> print(e)
[1, 2, 3, 12, 20, 30]
>>> id(e)
2371470300352
>>> f=(1,2,3)
>>> type(f)
<class 'tuple'>
g={1,2,34}
type(g)
<class 'set'>
h={1:"one",2:4,3:[1,2,3],5:(1,21)}
h
{1: 'one', 2: 4, 3: [1, 2, 3], 5: (1, 21)}
type(h)
<class 'dict'>
i = True
type(i)
<class 'bool'>
j = False
type(j)
<class 'bool'>
k=''
type(k)
<class 'str'>
l=None
type(l)
<class 'NoneType'>

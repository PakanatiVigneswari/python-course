Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=input("Enter the string: ")
Enter the string: Krishna
a
'Krishna'
a=input()
567
type(a)
<class 'str'>
a=int(input())
556
a=int(input("Enter the integer: "))
Enter the integer: 324
a
324
a=float(input("Enter the float:"))
Enter the float:34
a
34.0
a=list(input())
43567886785
a
['4', '3', '5', '6', '7', '8', '8', '6', '7', '8', '5']
a = list(input())
87 67 34 54 98 56
a
['8', '7', ' ', '6', '7', ' ', '3', '4', ' ', '5', '4', ' ', '9', '8', ' ', '5', '6']
'87 67 54 98 2 87 09 34'.split(' ')
['87', '67', '54', '98', '2', '87', '09', '34']
87 67 54 98 2 87 09 34'.split()
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
87 67 54 98 2 87 9 34'.split()
SyntaxError: unterminated string literal (detected at line 1)
'87 67 54 98 2 87 09 34'.split()
['87', '67', '54', '98', '2', '87', '09', '34']
'34,12,56,89,54,67,87'.split(',')
['34', '12', '56', '89', '54', '67', '87']
a
['8', '7', ' ', '6', '7', ' ', '3', '4', ' ', '5', '4', ' ', '9', '8', ' ', '5', '6']
map(int,a)
<map object at 0x0000021FB727F2E0>
list(map(int,a))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list(map(int,a))
ValueError: invalid literal for int() with base 10: ' '
'87 67 54 98 2 87 09 34'.split(' ')

['87', '67', '54', '98', '2', '87', '09', '34']
a
['8', '7', ' ', '6', '7', ' ', '3', '4', ' ', '5', '4', ' ', '9', '8', ' ', '5', '6']
a='87 67 54 98 2 87 09 34'.split(' ')
a
['87', '67', '54', '98', '2', '87', '09', '34']
map(int,a)
<map object at 0x0000021FB727FD90>
list(map(int,a))
[87, 67, 54, 98, 2, 87, 9, 34]
a=list(map(int,input().split()))
1 54 5676 678
a
[1, 54, 5676, 678]
a=list(map(float,input().split()))
a
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a=list(map(float,input().split()))
ValueError: could not convert string to float: 'a'
a=list(map(float,input().split()))
2435 44566 64 65.876
SyntaxError: multiple statements found while compiling a single statement
a
[1, 54, 5676, 678]
a=list(map(float,input().split()))
2635 753.6 567 6.65
a
[2635.0, 753.6, 567.0, 6.65]
a=tuple(input().split())
675 67 67 768 879
a
('675', '67', '67', '768', '879')
a=tuple(map(int,input().split()))
454 75 342 89 34 89
SyntaxError: multiple statements found while compiling a single statement
a=tuple(map(int,input().split()))
6757 87 54 8 54 876 54
a
(6757, 87, 54, 8, 54, 876, 54)
a=tuple(map(float,input().split()))
6 89 54 3.8 6 56
a
(6.0, 89.0, 54.0, 3.8, 6.0, 56.0)
a=set(input().split())
67
a
{'67'}
KeyboardInterrupt
a=tuple(map(int,input().split()))
a=set(map(int,input().split()))
87 34 8 54 89 34 6 879 65
a
{65, 34, 6, 8, 879, 54, 87, 89}
a=set(map(float,input().split()))
56 89 34 89 54
a
{56.0, 89.0, 34.0, 54.0}
a,b,c=(1,2,3)
a
1
b
2
c
3
a,b,c=[4,5,6]
a
4
b
5
c
6
a,b,c=list(map(int,input().split()))
a
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'a'
a,b,c=list(map(int,input().split()))
1,2,3
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: '1,2,3'
a,b,c=list(map(int,input().split()))
2,5,7
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: '2,5,7'
a,b,c=list(map(int,input().split()))
2 4 8
a
2
b
4
c
8
email,password=input.split()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    email,password=input.split()
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
email,password=input().split()
ram@gmail.com 12345678
email
'ram@gmail.com'
password
'12345678'
a=eva(input())
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a=eva(input())
NameError: name 'eva' is not defined. Did you mean: 'eval'?
a=eval(input())
[1,2,3]
a
[1, 2, 3]
a=eval(input())
"Krishna"
a
'Krishna'
a=eval(input())
(1,2,3)
a
(1, 2, 3)
a=eval(input())
[1,3,5,6]
a
[1, 3, 5, 6]
a=eval(input())
{1,5,7}
a
{1, 5, 7}
a=eval(input())
{1:2,2:"Ram",3:"Krishna",4:5}
a
{1: 2, 2: 'Ram', 3: 'Krishna', 4: 5}
a=True
a=eval(input())
True
a
True
c="codegnan"
a
True
>>> a=10
>>> b=10.2
>>> a
10
>>> b
10.2
>>> c
'codegnan'
>>> print(a,b,c)
10 10.2 codegnan
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 10.2 c= codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='')
a=10b=10.2c=codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='-')
a=-10-b=-10.2-c=-codegnan
>>> print("a=",a,"b=",b,"c=",c,end='\n\n')
a= 10 b= 10.2 c= codegnan

>>> print("a=",a,"b=",b,"c=",c,end='@')
a= 10 b= 10.2 c= codegnan@
>>> print(f'a={a} b={b} c={c}')
a=10 b=10.2 c=codegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=10.200000 c=codegnan
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
a=10 b=10.20 c=codegnan
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=10.2 c=codegnan
>>> print('a={} b={} c={}'.format(b,c,a))
a=10.2 b=codegnan c=10

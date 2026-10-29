Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s="python programming"
s.startswith('p')
True
s.startswith('n')
False
s.startswith('pyt')
True
s.endswith('p')
False
s.endswith('g')
True
s.endawith('ing')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.endawith('ing')
AttributeError: 'str' object has no attribute 'endawith'. Did you mean: 'endswith'?
s.endswith('ing')
True
's'.islower()
True
s="Codegnan@123"
'o'.islower()
True
'C'.isupper()
True
'Codegnan@'.isalpha()
False
'codegnan12'.isalpha()
False
'codegnan'.isalpha()
True
'myvar'.isidentifier()
True
'myvar@'.isidentifier()
False
' '.isspace()
True
'          hello'.isspace()
False
'1234'.isdecimal()
True
'1234'.isdigit()
True
'1234'.isnumeric()
True
'1/2'.isnumeric()
False
'a-b-c'.split('-')
['a', 'b', 'c']
'a-b-c'.split()
['a-b-c']
'a-b-c'.split('-',2)
['a', 'b', 'c']
'a-b-c'.rsplit()
['a-b-c']
'a-b-c'.rsplit('-')
['a', 'b', 'c']
'a-b-c-d'.split('-',2)
['a', 'b', 'c-d']
s="
SyntaxError: unterminated string literal (detected at line 1)
s="Hello
SyntaxError: unterminated string literal (detected at line 1)
s="""
Hello
World
python
"""
s
'\nHello\nWorld\npython\n'
s.splitlines()
['', 'Hello', 'World', 'python']
l=['a','b','c','d']
l
['a', 'b', 'c', 'd']
'-'.join(l)
'a-b-c-d'
''.join(l)
'abcd'
' '.join(l)
'a b c d'
'*'.join(l)
'a*b*c*d'
s='a-b-c-d'
s.partition('b')
('a-', 'b', '-c-d')
'python.py'.partition('.')
('python', '.', 'py')
'pyt.hon.py'.partition('.')
('pyt', '.', 'hon.py')
'pyt.hon.py'.rpartition('.')
('pyt.hon', '.', 'py')
s="hello"
s.encode()
b'hello'
t="Hello 😊"
s.encode()
b'hello'
t.encode()
b'Hello \xf0\x9f\x98\x8a'
b'Hello \xf0\x9f\x98\x8a'.decode()
'Hello 😊'
l=[]
l=list()
l=[1,2,3]
l=list([1,2,3,4])
l
[1, 2, 3, 4]
type(l)
<class 'list'>
l=[2,3,4,5,6]
l
[2, 3, 4, 5, 6]
l=[1,1,1,1,1]
l
[1, 1, 1, 1, 1]
l=[1,12.2,3+5j,"str",[1,2,3],(1,2,3),{1,2,3},{1:"Krishna",2:"Ram"},False,None]
l
[1, 12.2, (3+5j), 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'Krishna', 2: 'Ram'}, False, None]
[1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
[1,2,3]+[3,4,5]
[1, 2, 3, 3, 4, 5]
[1,2,3]*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
l=['python','java','c++','c','mysql','html','css','javascript','aws']
l[0]
'python'
l[-1]
'aws'
l[2]
'c++'
l[4]
'mysql'
l[1:]
['java', 'c++', 'c', 'mysql', 'html', 'css', 'javascript', 'aws']
l[0:]
['python', 'java', 'c++', 'c', 'mysql', 'html', 'css', 'javascript', 'aws']
l[::-1]
['aws', 'javascript', 'css', 'html', 'mysql', 'c', 'c++', 'java', 'python']
l[:3]
['python', 'java', 'c++']
l[-3:]
['css', 'javascript', 'aws']
l[2:5]
['c++', 'c', 'mysql']
l[1::2]
['java', 'c', 'html', 'javascript']
l[::-1]
['aws', 'javascript', 'css', 'html', 'mysql', 'c', 'c++', 'java', 'python']
l[-3:-6:-1]
['css', 'html', 'mysql']
l
['python', 'java', 'c++', 'c', 'mysql', 'html', 'css', 'javascript', 'aws']
'c' in l
True
'f' in l
False
'flask' in l
False
'c
SyntaxError: unterminated string literal (detected at line 1)
'css' not in l
False
'css' in l
True
'html' in l
True
len(l)
9
sorted(l)
['aws', 'c', 'c++', 'css', 'html', 'java', 'javascript', 'mysql', 'python']
max(l)
'python'
min(l)
'aws'
l
['python', 'java', 'c++', 'c', 'mysql', 'html', 'css', 'javascript', 'aws']
>>> l[1]='flask'
>>> l
['python', 'flask', 'c++', 'c', 'mysql', 'html', 'css', 'javascript', 'aws']
>>> id(l)
2420926992640
>>> l[2]
'c++'
>>> l[3]="css"
>>> l
['python', 'flask', 'c++', 'css', 'mysql', 'html', 'css', 'javascript', 'aws']
>>> id(l)
2420926992640
>>> l.append('b')
>>> l.append('a')
>>> l.extend(["html","css","js"])
>>> l
['python', 'flask', 'c++', 'css', 'mysql', 'html', 'css', 'javascript', 'aws', 'b', 'a', 'html', 'css', 'js']
>>> l.insert(2,"r")
>>> l
['python', 'flask', 'r', 'c++', 'css', 'mysql', 'html', 'css', 'javascript', 'aws', 'b', 'a', 'html', 'css', 'js']
>>> id(l)
2420926992640

Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='python'
t='programming'
s+t
'pythonprogramming'
t*3
'programmingprogrammingprogramming'
t * 3
'programmingprogrammingprogramming'
s*7
'pythonpythonpythonpythonpythonpythonpython'
'*'*20
'********************'
'0'*30
'000000000000000000000000000000'
s='python java flask mysql fastapi'
s[0]
'p'
s[7]
'j'
s[-1]
'i'
s[-9]
'l'
s[-16]
's'
s[0:6]
'python'
s[0:6:2]
'pto'
s[1:18:3]
'yojalk'
s[:6]
'python'
s[7:11]
'java'
s[24:]
'fastapi'
s[:20]
'python java flask my'
s[:22]
'python java flask mysq'
s[::-1]
'ipatsaf lqsym ksalf avaj nohtyp'
s[-7:]
'fastapi'
s[-7:2]
''
s=[-4:2]
SyntaxError: invalid syntax
s=[-4:-2]
SyntaxError: invalid syntax
s[-4:17:-2]
'ta qy'
s[-4:17:2]
''
s[-5:18:3]
''
s[-5:19:-3]
's s'
s[:-5:0]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s[:-5:0]
ValueError: slice step cannot be zero
s[-5:0]
''
s[-5:1]
''
s[-5:1:-1]
'saf lqsym ksalf avaj noht'
s[5:22:1]
'n java flask mysq'
s[1::]
'ython java flask mysql fastapi'
s[0::]
'python java flask mysql fastapi'
s[5::-1]
'nohtyp'
s
'python java flask mysql fastapi'
'java' in s
True
'mysql' in s
True
'html' in s
False
'c++' not in s
True
'python' not in s
False
'python' in s
True
len(s)
31
ord('a')
97
ord('37')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    ord('37')
TypeError: ord() expected a character, but string of length 2 found
ord('22')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    ord('22')
TypeError: ord() expected a character, but string of length 2 found
ord('p')
112
ord('0')
48
ord('1')
49
ord('20')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    ord('20')
TypeError: ord() expected a character, but string of length 2 found
s
'python java flask mysql fastapi'
ord('c')
99
ord('*')
42
ord('+')
43
chr(10)
'\n'
chr(22)
'\x16'
max(s)
'y'
s
'python java flask mysql fastapi'
min(s)
' '
sorted(s)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'f', 'f', 'h', 'i', 'j', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'p', 'q', 's', 's', 's', 't', 't', 'v', 'y', 'y']

s
'python java flask mysql fastapi'
len(s)
31
s.lower()
'python java flask mysql fastapi'
s.upper()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.swapcase()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.swapcase()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.title()
'Python Java Flask Mysql Fastapi'
s.capitalize()
'Python java flask mysql fastapi'
s='python'
s.center(40,'-')
'-----------------python-----------------'
s.center(40,'')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s.center(40,'')
TypeError: The fill character must be exactly one character long
s.center(40,'')
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s.center(40,'')
TypeError: The fill character must be exactly one character long
s.center
<built-in method center of str object at 0x0000024085FEE940>
s.center(40,' ')
'                 python                 '
s.center(40,'*')
'*****************python*****************'
s.ljust(40,'*')
'python**********************************'
s.rjust(40,'*')
'**********************************python'
'1'.zfill(5)
'00001'
'123'zfill(5)
SyntaxError: invalid syntax
'123'.zfill(5)
'00123'
'123456789'.zfill(5)
'123456789'
s.find(a)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.find(a)
NameError: name 'a' is not defined
s='python java flask mysql fastapi'
a.find(a)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.find(a)
NameError: name 'a' is not defined
s.find('a')
8

s.rfind('a')
28
s.find('y')
1
s.find('c')
-1
s.index('a')
8
s.rindex('a')
28
>>> s.index('c')
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s.index('c')
ValueError: substring not found
>>> s.index('p')
0
>>> s.count('a')
5
>>> s='       python programming            '
>>> s.strip()
'python programming'
>>> s.lstrip()
'python programming            '
>>> s.rstrip()
'       python programming'
>>> s.replace('a','*')
'       python progr*mming            '
>>> s.maketrans('apkqs','12345')
{97: 49, 112: 50, 107: 51, 113: 52, 115: 53}
>>> s.translate(s.maketrans('apks','12345'))
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    s.translate(s.maketrans('apks','12345'))
ValueError: the first two maketrans arguments must have equal length
>>> s.translate(s.maketrans('py','12'))
'       12thon 1rogramming            '
>>> s.translate(s.maketrans('aplm','1234'))
'       2ython 2rogr144ing            '

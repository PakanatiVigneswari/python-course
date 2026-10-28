Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
9/2
4.5
a//b
2
9//2
4
9%2
1
a%b
0
2**4
16
7**2
49
3**3
27
'''
Comparision Operator:
'''
'\nComparision Operator:\n'
a
20
b
10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
'''
Assignment Operator
'''
'\nAssignment Operator\n'
c=20
c=c+10
c=30
c
30
c=c-10
c
20
c*=5
c
100
c+=10
c
110
c-=10
c
100
'''
Logical Operator
'''
'\nLogical Operator\n'
a
20
a%2 == 0 and a>10
True
b
10
b%2 == 0 and b>10
False
b%2 == 0 or b>10
True
b%2==0
True
not b%2 ==0
False
'''
Membership Operator
'''
'\nMembership Operator\n'
s='python'
'p' in s
True
'o' in s
True
'z' in s
False
'n' in s
True
'b' not in s
True
'o' not in s
False
's' not in s
True
l=["krishna","ram","govinda","shiva"]
"krishna" in l
True
"shiva' not in l
SyntaxError: unterminated string literal (detected at line 1)
"shiva" not in l
False
"shiva" in l
True
"govinda" in l
True
s={12, 34, 56, 4}
12 in s
True
34 not in l
True
56 in l
False
56 in s
True
d={1:2,2:12,3:11,4:22,5:76}
1 in d
True
12 in d
False
12 not in d
True
2 in d
True
>>> 6 in d
False
>>> 5 in d
True
>>> '''
... Identity Operator
... '''
'\nIdentity Operator\n'
>>> l=[1,2,3,4,5]
>>> m=[1,2,3,4,5]
>>> id(l)
1461014168576
>>> id(m)
1460974630720
>>> l==m
True
>>> l is m
False
>>> n = m
>>> n
[1, 2, 3, 4, 5]
>>> id(n)
1460974630720
>>> n is m
True
>>> n is not m
False
>>> n is not l
True
>>> n is m
True

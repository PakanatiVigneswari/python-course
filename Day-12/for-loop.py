# for loop is used for str, list, tuple, set, dict, range()

'''s="Krishna"
for i in s:
    print(i)'''


#Checking the vowel
'''s=input("Enter thge vowel: ")
for i in s:
    if i in "AEIOUaeiou":
        print(i)'''


#List of elements to iterate check the even numbers
'''s=[10,56,80,56,54,32]
for i in s:
    print(i)'''


'''s=list(map(int, input("Enter the nums: ").split()))
for i in s:
    if i%2==0:
        print(i)'''


#Sum of tuple
'''sum=0
a=tuple(map(int,input("Enter the number: ").split()))
for i in a:
    sum+=i
print("Sum of tuple: ",sum)
'''


#Set of numbers
'''s={87,60,45,32,14,87,89,67}
for i in s:
    print(i)'''


'''max=0
s=set(map(int,input("Enter the numbers: ").split()))
for i in s:
    if i > max:
        max = i
print("max of set", max)'''


#Iterating the dictionary
'''marks = {"Python":90, "SQL":99, "HTML":89, "CSS":95}
for i in marks:
    print(i,marks[i])'''


'''sum = 0
marks = {"Python":90, "SQL":99, "HTML":89, "CSS":95}
for i in marks:
    sum += marks[i]
print("Total marks", sum)
'''


#range(start, end+1,step)
#range(0,,1)
'''for i in range(0, 11):
    print(i)'''

'''for i in range(20,0,-1):
    print(i, end=" ")
'''



'''for i in range(2, 101, 2):
    print(i, end=" ")'''


'''n=int(input("Enter a number: "))
for i in range(1,21):
    print(f"{n} X {i} = {n*i}")'''


'''s="Krishna"
for i in range(len(s)):
    print(s[i],i, end = " ")
'''


#List
'''l=[43,54,87,34,90,67,54]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum+=i      
print(sum)'''







l=[43,54,87,34,90,67,54]
mul=1
for i in range(len(l)):
    if i%2 != 0:
        mul*= i
print(mul)















'''for i in range(1,11):
    if i == 5:
        break
    print(i)'''



'''for i in range(1,11):
    if i == 5:
        continue
    print(i)
'''

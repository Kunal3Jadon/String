#1..input two strings and print them such that last character of first string replace by last chrarcter of second string and vice versa
x=input()
y=input()
a=x[:-1]+y[-1]
b=y[:-1]+x[-1]
print(a,b)
#2..WAP to print first and last charcter in upper case
x=input()
a=x[0].upper()
b=x[-1].upper()
print(a+x[1:-1]+b)
#3..WAP to reverse a string but not characters of words
x=input()
b=x.split()
c=" ".join(reversed(b))
print(c)
#4..WAP to print even index in upper case and odd index in lower case of a string
x=input()
s=''
for i in range(len(x)):
    if i%2==0:
        s+=x[i].lower()
    else:
        s+=x[i].upper()
print(s)
#5..WAP to check string is palindrome or not
x=input()
y=x[::-1]
if x==y:
    print("string is palindrome")
else:
    print("string is not palindrome")
#6..WAP to count frequency of each chararcter in string
s=input()
x=''
for i in s:
    if i not in x:
        print("frequency of",i,":",s.count(i))
        x+=i
#7..WAP to check digit is in string or not
s=input()
c=0
for i in s:
    if i.isdigit():
        c+=1
if c==0:
    print("no digit is in string")
else:
    print(c,"digits are in string")
#8..WAP to reverse a string
s=input()
print(s[::-1])

        


#(1) Ans: Decorator: Decorator is a function that takes another function as argument. It is modify existing function and return as aextensive functionality.
#Exa:
'''def dec(i):
    def sub(a,b):
        result=a-b
        return result,i(a,b)
    return sub

@dec
def num(a,b):
    add=a+b
    return add
print(num(50,20))'''

#(2)ANS: Lambda is anonymous function means a function is defined without a name. It is a single line of code.
#exa :
'''add=lambda a,b:a+b
print(add(20,30))'''

#(7)Ans:
'''li =[1,2,3]
li2=[10,20,30]
result ={}
for i in range(len(li)):
    result[li[i]]=li2[i]
print(result)'''

#(10)ans:
'''module : Module is a file.
         It can contain functions , classes and variables
        Module name added with suffix '.py' , exa: Test.py

Package: Packages is the directories
         it can contain modules and sub packages.
        Packages must contain ___init___.py file'''

#(11)ans:
'''List :
a) collection in python.
b) list is a mutable data type and heterogenous
c) it will allow duplicate data and can manipulate data
d)it enclosed with []

Tuple:
 a)collection in python
b)immutable type and heterogenous
c)can allow duplicate data but can not manipulate the data
d)enclosed with()

set:
 a)collection
b)immutable type and only allow immutable data type like allow tuple but not list
c)enclosed with {}
d)contains only single element

Dictionary:
a) collecton
b)mutable type and stores data in key, value pair
c)keys are unique and contain only immuatable datatype.
d)enclosed with {}'''


#(12)ans:
'''it is a memory management proces that deletes objects when they are no longer in use
Exa:
a=10
print(a), now the value of a is 10
a=20 
print(a), now the value of a is 20 ... so when we change the value of a from 10 to 20 then 10 value got garbage , this process is grabage collection'''

#(13)ans:

'''it is a single line code pf iteration in a list
exa:
pall_num=[i for i in range(100,501)if str(i)==str(i)[::-1]]
print(pall_num)'''

#(15)ans:
''' break:
it is break the loop with the help of condition,once break the loop it is not start again
exa:
for i in range (1,11):
    if i==7:
        break
    print(i)

continue:
it skips the rest of the current iteration of the loop and continues with next iteration
exa:
for i in range(1,11):
    if i%2==0:
        continue
    print(i)
    
pass:
it is used to pass the programe if there are no statement 
exa:
for i in range(1,11):
    pass'''

#(8)ans:
'''import csv
data=['firstname','email','phn_no']
data_rows=[
    ['Nishi','nishi12@gmaial.com',8765432100],
    ['Ram','Ram12@gmail.com',7890567432],
    ['Nihar','Nihar234@gmail.com',8765439087],
    ['Puja','Puja1234@gmail.com',8976547632],
    ['Jayant','Jayant1234@gmail.com',9876543210]
]
with open('New.csv',mode='w',newline='')as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow(data)
    csv_writer.writerows(data_rows)

for read and print:
with open('New.csv',mode='r')as file:
    csv_reader=csv.reader(file)
    for i in csv_reader:
        for j in i:
            print(j,end=' ')
        print()'''


#(9)ans:
'''An unorder or unevent that break the flow of programme is known as if exception and handle the situation instantly is known as exception handling

There are 3 block of EH:
Try , Except,Finally
Try: risk code
except: error name

exa:
try:
    num1=int(input('enter your first num:-'))
    num2=int(input('enter your second num:-'))
    div=num1/num2
    print(div)

except ZeroDivisionError:
    print('Try put without zero')'''


a=10
b=20
c=a+b
print(c)

print("-------------------")


#recursive function
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))

print("factorial):" ,factorial(5))     

print("------------------")  

c=lambda a: a+50
print(c(5))
print("-------------")

c=lambda f:f*5
print(c(5))
print("-------------------")

a= lambda a,b:a+b
print(a(24,24))
print("--------------")
import datetime as dt

current_date=dt.date.today()
print("current date",current_date)

new=dt.date(2004,4,1)
print(new)

print("year:",new.year)
print("month:",new.month)
print("day:",new.day)
print("---------------------------")
#time
a=dt.time(10,45,4,555505)
print(a)
print("hour:",a.hour)
print("minute:",a.minute)
print("a.second",a.second)
print("microsecond:",a.microsecond)

print("--------------------------")
current_time=dt.datetime.now()
print(current_time)

new=dt.date(2004,4,1)
print(new)
print("---------------")
new=dt.datetime.now()
print(new)
print(new.date())
print(new.time())
print("------------")

current=dt.datetime.now()
new_year=dt.datetime(2025,4,1)
difference=new_year-current
print(difference)
print("--------------------------")

s=current.strftime("%A %B %d %Y")
print(s)
#math function
import math
print(math.sqrt(4))
print(math.ceil(1.55555))
print(math.floor(1.55555))
#factorial
print(math.factorial(6))
print(math.fabs(-5))
print(math.pow(2,3))
print(math.log10(2))
print(math.pi)
print(math.e)

#try block in python
try:
    a=10/0
except Exception as e:
    print(e)    
print("-----------------")
try:
    a=10/2
except Exception as e:
    print(e)

else:
    print(a) 
    print("------------------")   
#finally

try:
    a=10/2
except Exception as e:
    print(e)

else:
    print(a)
finally:
    print("thank you")    

print("---------------")
try:
    a=10/2
except  Exception as e:
     print(e)
else:
    print(a)
finally:
    print("thank you")

    #type of exceptin
print(dir(locals()['__builtins__']))

print(len(dir(locals()['__builtins__'])))



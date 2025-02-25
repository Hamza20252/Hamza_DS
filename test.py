import math

###1
##print("Hello, World!")
##
###2
##x=10
##y="string"
##print(type(x))
##print(type(y))
##
###3
##lst=[1,2,3,4,5]
##
##s=sum(lst)
##l=len(lst)
##a=s/l
##print(a)
##print(s)
##
##
####4
##num1=int(input("enter first number: "))
##num2=int(input("enter second number: "))
##print(num1*num2)
##print(num1+num2)
##print(num1-num2)
##print(num1%num2)
##print(num1/num2)


#5
##name = "Alice"
##age = 25
##print(f"{name} is {age} years old")


##6

##user=input("enter the string: ")
##u=user.upper()
##l=user.lower()
##print(l)
##print(u)
##
##count=0
##string=input("enter  string: ")
##sl=string.lower()
##vowels='aeiou'
##for i in sl:
##    if i in vowels:
##        count+=1
##print(count)

##rs=user[::-1]
##print(rs)

##7
##num1=int(input("enter  number: "))
##
##if num1%2==0:
##    print("the number is even")
##else:
##    print("its odd")


##8
##for num in range(1,51):
##    if num<2:
##        continue
##    is_prime=True
##
##    for i in range(2,num):
##       if num%i==0:
##           is_prime=False
##           break
##    if is_prime:
##        print(num,end=' ')
        
##9
def factorial(n):
    result = 1
    for i in range(1, n + 1): 
        result *= i  
    return result


num = int(input("Enter a number: "))


if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")
    




##10
##class car():
##    def __init__(self,brand,model,year):
##        self.brand=brand
##        self.model=model
##        self.year=year
##
##    def display_info(self):
##        print(f'The car brand is {self.brand}, model is {self.model} and manifactured in year {self.year}')
##
##
##
##t1=car('amaze','lxi',2025)
##t1.display_info()






##11
##score={'hitesh':[70,90,88],'meet':[70,65,55],'aadil':[90,90,70]}
##
##for k,v in score.items():
##    print("keys-->",k)
##    print("values-->",v)
##h=sum(score['hitesh'])
##m=sum(score['meet'])
##a=sum(score['aadil'])
##
##if h>m and h>a:
##    print(f'hitesh is highest scorer with marks {h}')
##elif m>h and m>a:
##    print(f'meet is highest scorer with marks {m}')
##else:
##    print(f'aadil is highest scorer with marks {a}')
##


##12
##num1=int(input("enter  number: "))
##s=math.sqrt(num1)
##f=math.factorial(num1)
##print(s)
##print(f)


##13

##name=input("user please enter ur name")
##age=int("user please enter you age")
##print(f"Hello {name}, you are {age} years old")








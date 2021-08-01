#Python Program To Know whether a given number is prime or not 


num = int(input())

for i in num(2,num):
    if num % i == 0:
        print("Not Prime")
        break 
    else:
        print("The Number is a Prime Number")
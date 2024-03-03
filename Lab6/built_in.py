#Ex1
from operator import*
num_list = [1, 2, 5, 6]
m = 1
for i in num_list:
    m = mul(i, m)
print(m)

#Ex2
str=input("Enter your string:")
upper_case=0
lower_case=0
for i in str:
    if i.isupper():
        upper_case+=1
    elif i.islower():
        lower_case+=1
    else:
        pass
print("Lower case letters count: ",lower_case)
print("Upper case letters count: ",upper_case)


#Ex3
str = input("Enter your string: ")
rvrstr= ''.join(reversed(str))
if str== rvrstr:
    print("Yes,it is a palindrome!")
else:
    print("Nope")


#Ex4
def all_check(tuple):
    return all(tuple)

tuple1 = (True, "hi", 3, 4)
tuple2 = (True, False, "nirg", 5, 6)

print(all_check(tuple1))  
print(all_check(tuple2))  


#Ex5
import time
import math

def square_root(num, delay):
    time.sleep(delay/1000)
    output = math.sqrt(num)
    return output

num = int(input("Enter your number: "))
delay = int(input("Enter your delay in millisec: "))
result = square_root(num, delay)


print(f"Square root of {num} after {delay} milliseconds is {result}")

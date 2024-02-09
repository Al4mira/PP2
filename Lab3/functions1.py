#Ex1
def grams_function(grams):
     ounces = 28.3495231 * grams
     return ounces


grams = float(input("Enter grams measure: "))
ounces = grams_function(grams)
print(ounces)


#Ex2
def temperature(F):
    C = ((5 / 9) * (F - 32))
    return C

F = float(input("Enter temperature rate: "))
C = temperature(F)
print(C)


#Ex3
def solve():
    for x in range(36):
        y = 35 - x
        total_legs = 2*x + 4*y
        if total_legs == 94:
            return x, y

    return None


solution = solve()
if solution is not None:
    x, y = solution
    print("Number of chickens:", x)
    print("Number of rabbits:", y)



#Ex4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]

    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)

    return prime_numbers



#Ex5
def Queen(s, current=''):
    permutations = []
    
    if not s:
        permutations.append(current)
    else:
        for i in range(len(s)):
            remaining_chars = s[:i] + s[i+1:]
            permutations.extend(Queen(remaining_chars, current + s[i]))
    
    return permutations 

input_string = input("Enter a string: ")
result = Queen(input_string)
print(result)



#Ex6
def Metrooo(str):
    boomin = str.split()
    result = boomin[::-1]
    return result

user_input = input("Enter your sentence: ")
output = Metrooo(user_input)
print(output)


#Ex7
def a_lot(nums):
    haveit=False
    count=0
    for x in nums:
        if x==3:
            if haveit:
                count+=1
            else:
                    haveit=True
        else:
            haveit=False
    if count>=1:
        print("True")   
    else:
        print("False") 

a_lot([1, 3, 3])
a_lot([1, 3, 1, 3])
a_lot([3, 1, 3])


#Ex8
def spy(nums):
    traitor = []
    countof0 = 0
    countof7 = 0
    for i in nums:
        if i == 0 and count_0 < 2:
            traitor.append(i)
        elif i == 7 and count_7 ==0:
            traitor.append(i)
    if traitor[0] == 0 and traitor[1] == 0 and traitor[2] == 7:
        print("True")
    else:
        print("False")

spy([1,2,4,0,0,7,5])
spy([1,0,2,4,0,5,7])
spy([1,7,2,0,4,5,0])


#Ex9
import math

def V(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

user_input = float(input("Enter radius: "))
output = V(user_input)
print(output)


#Ex10
def No_name(mems):
    list = []
    for x in mems:
        if x in list:
            continue
        else:
            list.append(x)
    return list

user_input = input("Enter your numbers:")
print(*No_name(user_input), sep=' ')


#Ex11
def redrum(str):
    backward=str[::-1]
    if str == backward:
        return "This string is a palindrome"
    else:
        return "This string is NOT a palindrome"

user_input = input("Enter your word: ")
print(redrum(user_input))


#Ex12
def histo(stars):
    nums = stars.split()
    for num in nums:
        num = int(num)
        for _ in range(num):
            print("*", end="")
        print()

user_input = input("Enter your histogram (numbers separated by spaces): ")
histo(user_input)


#Ex13
import random

def guess_game():
    count_of_guesses = 0
    name = input("Hello! What's your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    
    while True:
        tries = int(input("Take a guess.\n"))
        count_of_guesses += 1
        
        if tries > number:
            print("Your guess is too high!")
        elif tries < number:
            print("Your guess is too low!")
        else:
            print()
            print(f"Good job, {name}! You guessed my number in {count_of_guesses} guess(es)!")
            break

guess_game()


    








    


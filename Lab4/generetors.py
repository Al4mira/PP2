#Ex1
def square_gen(n):
    for i in range(n):
        yield i**2


#Ex2
def even_gen(n):
    even_nums = (str(i) for i in range(n+1) if i % 2 == 0)
    print(",".join(even_nums))

n = int(input("Enter a number: "))
even_gen(n)


#Ex3
def filter_nums(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
filter_nums(n)
for num in filter_nums(n):
    print(num)


#Ex4
def squares():
    for i in range(a, b):
        yield i**2


#Ex5
def decreasing(n):
    for i in range(n, -1, -1):
        yield i

n = 6
decreasing(n)
for num in decreasing(n):
    print(num)
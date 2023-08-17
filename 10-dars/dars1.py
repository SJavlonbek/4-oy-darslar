# import time
# from multiprocessing import Pool

# def is_toq(num):
#     z = 0
#     for i in range(1, num + 1, 2):
#         z += i
#     return z

#xato bor

# def is_juft(num):
#     y = 0
#     for i in range(2, num + 1, 2):
#         y += i
#     return y

#xato bor

# def find_primes(start, end):
#     with Pool(4) as p:
#         s = sum(p.map(is_toq, list(range(start, end))))
#     return s

# def find_toqs(start, end):
#     with Pool(4) as p:
#         s = sum(p.map(is_juft, list(range(start, end))))
#     return s

# if __name__ == "__main__":
#     started = time.time()
#     primes_sum = find_primes(1, 1000000)
#     finished = time.time()
#     print(primes_sum)
#     print(finished - started)

#     started = time.time()
#     toqs_sum = find_toqs(1, 1000000)
#     finished = time.time()
#     print( toqs_sum)
#     print( finished - started)


# import time

# def sumOdd(n):
#     total1 = 0
#     for i in range(1, n, 2):
#         total1 += i
#     return total1

# def sumEven(n):
#     total2 = 0
#     for i in range(2, n, 2):
#         total2 += i
#     return total2

# started = time.time()
# print(sumOdd(100000000))
# print(sumEven(100000000))
# finished = time.time()
# print(finished - started)


import turtle
turtle.bgcolor("black")
squary=turtle.Turtle()
squary.speed(50)
squary.pencolor("red")
for i in range(500):
    squary.forward(i)
    squary.left(91)


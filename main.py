from math import exp, expm1
import math


def func1(x):
    return -5 * x ** 5 + 4 * x ** 4 - 12 * x ** 3 + 11 * x ** 2 - 2 * x + 1


def func2(x):
    return (math.log10(x-2)) ** 2 + (math.log10(10 - x)) ** 2 - (x ** 0.2)


def func3(x):
    return -3 * x * math.sin(0.75 * x) + math.exp(1) - 2 * x


def func4(x):
    return math.exp(3*x) + 5 * math.exp(1) - 2*x

def func5(x):
    return 0.2 * math.log10(x) + (x - 2.3) ** 2


def bisection_method(func1, e, d, a, b):
    #print(abs(b-a))
    if abs(b-a) > e:
        x1 = (a + b) / 2 - d
        x2 = (a + b) / 2 + d
        #print("x1 {} x2 {} f(x1) {} f(x2) {}".format(x1, x2, func1(x1), func1(x2)))
        if func1(x1) < func1(x2):
            bisection_method(func1, e, d, a, x2)
        elif func1(x1) > func1(x2):
            bisection_method(func1, e, d, x1, b)
        elif func1(x1) == func1(x2):
            bisection_method(func1, e, d, x1, x2)
    else:
        print((a + b) / 2)


def golden_section_search(func, e, a, b):
    fi = 2 / (1 + math.sqrt(5))
    x1 = b - fi * (b - a)
    x2 = a + fi * (b - a)
    print("x1 {} x2 {} f(x1) {} f(x2) {}".format(x1, x2, func(x1), func(x2)))
    if abs(b-a) > e:
        if func(x1) > func(x2):
            golden_section_search(func, e, x1, b)
            #print("a {} x2 {} b {}".format(, x2, func(x1), func(x2)))
        elif func(x1) < func(x2):
            golden_section_search(func, e, a, x2)
        elif func(x1) == func(x2):
            print((x1 + x2)/2)
            return
    else:
        print((a + b)/2)


def fibonacci(n):
    a = 1
    b = 1
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b


def fibonacci_search(func, n, k, a, b):
    if k != n:
        L2 = (fibonacci(n-k) / fibonacci(n - k + 1)) * (b - a)
        x1 = b - L2
        x2 = a + L2
        #print("ratio {}, {} x1 {} x2 {}".format(fibonacci(n-k), fibonacci(n - k + 1), x1, x2))
        if func(x2) > func(x1):
            k = k + 1
            #print("left")
            fibonacci_search(func, n, k, a, x2)
        if func(x2) <= func(x1):
            k = k + 1
            #print("right")
            fibonacci_search(func, n, k, x1, b)
    else:
        #print(a)
        #print(b)
        print((a + b) / 2)


def parabola_search2(e, a, b):
    h = 0.001
    if a == 0:
        a += 0.1
    while (func1(a + h) - 2 * func1(a) + func1(a - h)) / (h * h) <= 0:
        a += 0.1
    x1 = a - 0.5 * h * (func1(a + h) - func1(a - h)) / (func1(a + h) - 2 * func1(a) + func1(a - h))
    while abs(x1 - a) > e:
        a = x1
        x1 = a - 0.5 * h * (func1(a+h)- func1(a-h)) / (func1(a+h)-2 * func1(a)+func1(a-h))
    print(x1)
    return 0


def parabola_search(func, e, a, b, x):
    if abs(b - a) > e:
        u_part1 = (x - a) * (x - a) * (func(x) - func(b)) - (x - b) * (x - b) * (func(x) - func(a))
        u_part2 = 2 * ((x - a) * (func(x) - func(b)) - (x - b) * (func(x) - func(a)))
        u = x - (u_part1 / u_part2)
        #print("upart1 {} upart2 {} u {}".format(u_part1, u_part2, u))
        if u > b or u < a:
            print("error --> function out of bound")
            return
        #print(u, x, a, b)
        if u <= x:
            parabola_search(func, e, a, x, u)
        else:
            parabola_search(func, e, x, b, u)
    else:
        print((a + b)/2)
        return


def brent_method(func, e, a, b, x):
    if abs(b - a) > e:
        u_part1 = (x - a) * (x - a) * (func(x) - func(b)) - (x - b) * (x - b) * (func(x) - func(a))
        u_part2 = 2 * ((x - a) * (func(x) - func(b)) - (x - b) * (func(x) - func(a)))
        u = x - (u_part1 / u_part2)
        if u_part2 != 0 and (u >= a) and (u <= b):
            #print("parabola method")
            if u <= x:
                brent_method(func, e, a, x, u)
            else:
                brent_method(func, e, x, b, u)
        else:
            #print("golden section")
            fi = 2 / (1 + math.sqrt(5))
            x1 = b - fi * (b - a)
            x2 = a + fi * (b - a)
            # print("abs {} x1 {} x2 {}".format(abs(b-a), x1, x2))
            if func(x1) > func(x2):
                brent_method(func, e, x1, b, x2)
            elif func(x1) < func(x2):
                brent_method(func, e, a, x2, x1)
            elif func(x1) == func(x2):
                print((x1 + x2) / 2)
    else:
        print((a + b) / 2)
        return

print("func1")
bisection_method(func1, 0.01, 0.001, -0.5, 0.5)
golden_section_search(func1, 0.001, -0.5, 0.5)
fibonacci_search(func1, 20, 1, -0.5, 0.5)
parabola_search(func1, 0.01, -0.5, 0.5, 0)
brent_method(func1, 0.01, -0.5, 0.5, 0)

print('\nfunc2')
bisection_method(func2, 0.01, 0.001, 6, 9.9)
golden_section_search(func2, 0.01, 6, 9.9)
fibonacci_search(func2, 20, 1, 6, 9.9)
parabola_search(func2, 0.01, 6, 9.9, 7.95)
brent_method(func2, 0.01, 6, 9.9, 7.95)

print('\nfun3')
bisection_method(func3, 0.01, 0.001, 0, 2 * math.pi)
golden_section_search(func3, 0.01, 0, 2 * math.pi)
fibonacci_search(func3, 20, 1, 0, 2 * math.pi)
parabola_search(func3, 0.01, 0, 2 * math.pi, 2 * math.pi/2)
brent_method(func3, 0.01, 0, 2 * math.pi, 2 * math.pi/2)

print('\nfunc4')
bisection_method(func4, 0.01, 0.001, 0, 1) #actual answer = 0
golden_section_search(func4, 0.01, 0, 1)
fibonacci_search(func4, 20, 1, 0, 1)
parabola_search(func4, 0.01, 0, 1, 0.5)
brent_method(func4, 0.01, 0, 1, 0.5)

print('\nfunc5')
bisection_method(func5, 0.01, 0.001, 0.5, 2.5)
golden_section_search(func5, 0.01, 0.5, 2.5)
fibonacci_search(func5, 20, 1, 0.5, 2.5)
parabola_search(func5, 0.01, 0.5, 2.5, 1.5)
brent_method(func5, 0.01, 0.5, 2.5, 1.5)


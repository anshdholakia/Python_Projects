# Write a Python program to convert degree to radian.
# import math
# def func(d):
#     return math.radians(float(d))
# print(func(15))


# Write a Python program to calculate the area of a trapezium
# def func(a,b,h):
#     return 1/2*h*(a+b)
# print(func(6,5,5))


# Write a Python program to calculate the area of a parallelogram
# def area(b,h):
#     return b*h
# print(area(6,5))


# Write a Python program to calculate arc length of an angle
# def length(d,ang):
#     import math
#     return d/2*math.radians(ang)
# print(length(8,45))


# Write a Python program to calculate the area of the sector
# def area(r,a):
#     import math
#     return 1/2*pow(r,2)*math.radians(a)
# print(area(4,45))


# Write a Python program to find out, if the given number is abundant
# def func(n):
#     sum=0
#     for i in range(1,n):
#         if(n%i==0):
#             sum+=i
#     if(sum>n):
#         return True
#     else:return False
# print(func(13))


# Write a Python program to print all permutations of a given string (including duplicates)
# def func(stra):
#     import random
#     fact=1
#     lis=[]
#     res=[]
#     for i in range(0,len(stra)):
#         lis.append(stra[i])
#     for i in range(2,len(stra)+1):
#         fact=fact*i
#     for i in range(0,fact):
#         random.shuffle(lis)
#         res.append("".join(lis))
#     return res
# print(func("ABC"))


# Write a Python program to print the first n Lucky Numbers
# n=int(input("Input a Number: "))
# List=range(-1,n*n+9,2)
# i=2
# while List[i:]:List=sorted(set(List)-set(List[List[i]::List[i]]));i+=1
# print(List[1:n+1])


# Write a Python program to computing square roots using the Babylonian method
# def BabylonianAlgorithm(number):
#     if(number == 0):
#         return 0
#
#     g = number/2.0
#     g2 = g + 1
#     while(g != g2):
#         n = number/ g
#         g2 = g
#         g = (g + n)/2
#
#     return g
# print('The Square root of 0.3 =', BabylonianAlgorithm(0.3))


# Write a Python program to multiply two integers without using the * operator in python
# def func(a,b):
#     orig=a
#     for i in range(0,b-1):
#         a+=orig
#     return a
# print(func(4,3))


# Write a Python program to get prime numbers through Eratosthenes method
# def sieve_of_Eratosthenes(num):
#     limitn = num+1
#     not_prime_num = set()
#     prime_nums = []
#
#     for i in range(2, limitn):
#         if i in not_prime_num:
#             continue
#
#         for f in range(i*2, limitn, i):
#             not_prime_num.add(f)
#
#         prime_nums.append(i)
#     return prime_nums
# print(sieve_of_Eratosthenes(3485))



# Write a python program to find the next previous palindrome of a specified number.
# def palindrom(n):
#     pal=[]
#     for i in range(n,n*100):
#         j=i
#         res=0
#         while(j>0):
#             r=j%10
#             res=res*10+r
#             j=int(j/10)
#
#         if(res==i):
#             pal.append(i)
#             break
#         else:continue
#     return pal[0]
# print(palindrom(123235))



# Write a Python program to generate all permutations of a list in Python
# import itertools
# def func(lis):
#     return list(itertools.permutations(lis))
#
# print(func([1,2,3,4]))



# Write a Python program to convert a binary number to decimal number
# def func(bin):
#     value = 0
#     for i in range(len(bin)):
#         digit = bin.pop()
#         if digit == '1':
#             value = value + pow(2, i)
#     return value
# print(func([1,0,0,0,0,0,1]))


# Write a Python program to get the length and the angle of a complex number
# import cmath
# cn = complex(3,4)
# #length of a complex number.
# print("Length of a complex number: ", abs(cn))
# # gets angle. return in radians, between  [-π, π]
# print("Complex number Angle: ",cmath.phase(0+1j) )


# Write a Python program to convert Polar coordinates to rectangular coordinates.
# import cmath
# cp=complex(3,4)
# print("Polar coordinates:",cmath.polar(cp))
# print("In rectangel form:",cmath.rect(2,cmath.pi))


# write a Python program to round a specified decimal by setting precision (between 1 and 4).
# import decimal
# a=decimal.Decimal(00.234234)
# print("Original number: ",a)
# for i in range(1,5):
#     decimal.getcontext().prec=i
#     print("number rounded to ",i,":",a*1)


# Write a Python program to get the local and default precision
# import decimal
# with decimal.localcontext() as dq:
#     dq.prec=2
#     print('Local precision:',dq.prec)
#     print("22/7: ",(decimal.Decimal(22)/7))
# print()
# print('Default precision:', decimal.getcontext().prec)
# print('22 /7 =', (decimal.Decimal('22') / 7))


# fractions in the form of instances of float numbers
# import fractions
# for i in [0.2,0.6,2.0,1.4]:
#     print(f"{i} : {fractions.Fraction(i)}")


# Write a Python program to create the fraction instances of decimal numbers.
# import fractions
# from decimal import Decimal
# for i in [Decimal('0'), Decimal('0.7'), Decimal('2.5'), Decimal('3.0')]:
#     print(f"{i} : {fractions.Fraction(i)}")


# Write a Python program to convert a floating point number (PI)
# to an approximate rational value on the various denominator.
# import fractions
# import math
# print('PI       =', math.pi)
# f_pi = fractions.Fraction(str(math.pi))
# print('No limit =', f_pi)
# for d in [1, 5,  50, 90, 100, 500, 1000000]:
#     limited = f_pi.limit_denominator(d)
#     print('{0:8} = {1}'.format(d, limited))

    
# Write a Python program to generate random float numbers in a specific numerical range
# import random
# for x in range(6):
#     print(f"{random.uniform(x,100)} ")


# Write a Python program to generate random integers in a specific numerical range
# import random
# for c in range(0,10):
#     print(random.randint(1,10),end=" ")


# Write a Python program to flip a coin 1000 times and count heads and tails
# import random
# head=0
# tail=0
# for i in range(1000):
#     if random.randint(0,1)==0:
#         head+=1
#     else:
#         tail+=1
# print("Number of heads: ",head)
# print("Number of tails: ",tail)


# get random words from system dictionary
# import random
# with open('/Ansh/share/dict/words', 'rt') as fh:
#     words = fh.readlines()
# words = [w.rstrip() for w in words]
# for w in random.sample(words, 7):
#     print(w)


# Write a Python program to randomly select an item from a list
# import random
# lis=[2,3,2,4,6,654,542332,5]
# random.shuffle(lis)
# print(lis[0])


# Write a Python program to calculate the absolute value of a floating point number
# a=float(input("Enter float number: "))
# import math
# print(math.fabs(a))


# Write a Python program to calculate the standard deviation of the following data
# P=((xi-U)^2/N)^1/2
# def func(lis):
#     if len(lis)<=1:
#         return 0
#     else:
#         N=len(lis)
#         U=mean(lis)
#         sigma=0
#         for i in range(0,len(lis)):
#             sigma+=float(lis[0]-U)**2
#         total=(sigma/float(N-1))**(1/2)
#         return total
#
#
#
#
# def mean(lis):
#     (total,n)=(0,len(lis))
#     for i in lis:
#         total+=float(i)
#     return total/float(n)
# print(func([4,2,5,8,6]))



# Write a Python program to print the floating point from mantissa, exponent pair
# import math
# print('{:^7}  {:^8}  {:^17}'.format('Mantissa', 'Exponent', 'Floating point value'))
# print('{:-^8}  {:-^8}  {:-^20}'.format('', '', ''))
# for m, e in [(0.7, -3),
#              (0.3, 0),
#              (0.5, 3),
#              ]:
#     x = math.ldexp(m, e)
#     print('{:7.2f}  {:7d}  {:7.2f}'.format(m, e, x))


# Write a Python program to split fractional and integer parts of a floating point number.
# import math
# print('           (F)  (I)')
# for i in range(6):
#     print('{}/2 = {} {}'.format(i, i / 2, math.modf(i / 2.0)))


# Write a Python program to parse math formulas and put parentheses around multiplication and division.
# import ast
# def recurse(node):
#     if isinstance(node, ast.BinOp):
#         if isinstance(node.op, ast.Mult) or isinstance(node.op, ast.Div):
#             print('(', end='')
#         recurse(node.left)
#         recurse(node.op)
#         recurse(node.right)
#         if isinstance(node.op, ast.Mult) or isinstance(node.op, ast.Div):
#             print(')', end='')
#     elif isinstance(node, ast.Add):
#         print('+', end='')
#     elif isinstance(node, ast.Sub):
#         print('-', end='')
#     elif isinstance(node, ast.Mult):
#         print('*', end='')
#     elif isinstance(node, ast.Div):
#         print('/', end='')
#     elif isinstance(node, ast.Num):
#         print(node.n, end='')
#     else:
#         for child in ast.iter_child_nodes(node):
#             recurse(child)
# def search_expr(node):
#     returns = []
#     for child in ast.iter_child_nodes(node):
#         if isinstance(child, ast.Expr):
#             return child
#         returns.append(search_expr(child))
#     for ret in returns:
#         if isinstance(ret, ast.Expr):
#             return ret
#     return None
# formula = '4+6-7*7/2'
# a = ast.parse(formula)
# expr = search_expr(a)
# if expr is not None:
#     recurse(expr)
# print()


# Write a Python program to describe linear regression .
# data = set()
# count = int(input("Enter the number of data points: "))
# for i in range(count):
#     x=float(input("X"+str(i+1)+": "))
#     y=float(input("Y"+str(i+1)+": "))
#     data.add((x,y))

# Find the average x and y
# avgx = 0.0
# avgy = 0.0
# for i in data:
#     avgx += i[0]/len(data)
#     avgy += i[1]/len(data)
#
# # Find the sums
# totalxx = 0
# totalxy = 0
#
# for i in data:
#     totalxx += (i[0]-avgx)**2
#     totalxy += (i[0]-avgx)*(i[1]-avgy)
#
# # Slope/intercept form
# m = totalxy/totalxx
# b = avgy-m*avgx
#
# print("Best fit line:")
# print("y = "+str(m)+"x + "+str(b))
#
# x = float(input("Enter a value to calculate: "))
# print("y = "+str(m*x+b))


# Write a Python program to calculate a grid of hexagon coordinates of the given
# radius given lower-left and upper-right coordinates.
# import math
# def calculate_polygons(startx, starty, endx, endy, radius):
#     # calculate side length given radius
#     sl = (2 * radius) * math.tan(math.pi / 6)
#     # sin(30)
#     p = sl * 0.5
#     b = sl * math.cos(math.radians(30))
#     w = b * 2
#     h = 2 * sl
#
#     # offset start and end coordinates by hex widths and heights to guarantee coverage
#     startx = startx - w
#     starty = starty - h
#     endx = endx + w
#     endy = endy + h
#
#     origx = startx
#     origy = starty
#
#     # offsets for moving along and up rows
#     xoffset = b
#     yoffset = 3 * p
#
#     polygons = []
#     row = 1
#     counter = 0
#
#     while starty < endy:
#         if row % 2 == 0:
#             startx = origx + xoffset
#         else:
#             startx = origx
#         while startx < endx:
#             p1x = startx
#             p1y = starty + p
#             p2x = startx
#             p2y = starty + (3 * p)
#             p3x = startx + b
#             p3y = starty + h
#             p4x = startx + w
#             p4y = starty + (3 * p)
#             p5x = startx + w
#             p5y = starty + p
#             p6x = startx + b
#             p6y = starty
#             poly = [
#                 (p1x, p1y),
#                 (p2x, p2y),
#                 (p3x, p3y),
#                 (p4x, p4y),
#                 (p5x, p5y),
#                 (p6x, p6y),
#                 (p1x, p1y)]
#             polygons.append(poly)
#             counter += 1
#             startx += w
#         starty += yoffset
#         row += 1
#     return polygons
# print(calculate_polygons(1, 1, 4, 4, 3))


# Write a Python program to create a simple math quiz
# import random
# def display_intro():
#     title = "** A Simple Math Quiz **"
#     print("*" * len(title))
#     print(title)
#     print("*" * len(title))
# def display_menu():
#     menu_list = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Integer Division", "5. Exit"]
#     print(menu_list[0])
#     print(menu_list[1])
#     print(menu_list[2])
#     print(menu_list[3])
#     print(menu_list[4])
#
# def display_separator():
#     print("-" * 24)
# def get_user_input():
#     user_input = int(input("Enter your choice: "))
#     while user_input > 5 or user_input <= 0:
#         print("Invalid menu option.")
#         user_input = int(input("Please try again: "))
#     else:
#         return user_input
# def get_user_solution(problem):
#     print("Enter your answer")
#     print(problem, end="")
#     result = int(input(" = "))
#     return result
# def check_solution(user_solution, solution, count):
#     if user_solution == solution:
#         count = count + 1
#         print("Correct.")
#         return count
#     else:
#         print("Incorrect.")
#         return count
# def menu_option(index, count):
#     number_one = random.randrange(1, 21)
#     number_two = random.randrange(1, 21)
#     if index is 1:
#         problem = str(number_one) + " + " + str(number_two)
#         solution = number_one + number_two
#         user_solution = get_user_solution(problem)
#         count = check_solution(user_solution, solution, count)
#         return count
#     elif index is 2:
#         problem = str(number_one) + " - " + str(number_two)
#         solution = number_one - number_two
#         user_solution = get_user_solution(problem)
#         count = check_solution(user_solution, solution, count)
#         return count
#     elif index is 3:
#         problem = str(number_one) + " * " + str(number_two)
#         solution = number_one * number_two
#         user_solution = get_user_solution(problem)
#         count = check_solution(user_solution, solution, count)
#         return count
#     else:
#         problem = str(number_one) + " // " + str(number_two)
#         solution = number_one // number_two
#         user_solution = get_user_solution(problem)
#         count = check_solution(user_solution, solution, count)
#         return count
# def display_result(total, correct):
#     if total > 0:
#         result = correct / total
#         percentage = round((result * 100), 2)
#     if total == 0:
#         percentage = 0
#     print("You answered", total, "questions with", correct, "correct.")
#     print("Your score is ", percentage, "%. Thank you.", sep = "")
# def main():
#     display_intro()
#     display_menu()
#     display_separator()
#
#     option = get_user_input()
#     total = 0
#     correct = 0
#     while option != 5:
#         total = total + 1
#         correct = menu_option(option, correct)
#         option = get_user_input()
#
#     print("Exit the quiz.")
#     display_separator()
#     display_result(total, correct)
#
# main()


# Write a Python program to compute the value of e(2.718281827...) using infinite series.
# import math
# def fact(n):
#     if n == 0:
#        return 1
#     else:
#        return n*fact(n-1)
#
# def e(EPS):
#     v1 = 2
#     v2 = v1 + float(1.0/fact(2))
#     i = 3
#     while math.fabs(v1-v2) >= EPS:
#           v1 = v2
#           v2 += float(1.0/fact(i))
#           i += 1
#     return v2
# print("The mathematical constant e")
# #computes the value of e using infinite series
# print(e(0.00000001))
# #mathematical constant e build-in
# print(math.e)



# Write a Python program to create an ASCII waveform.
# from time import sleep
# from math import sin, cos, radians
# # increase 40 to get more wave
# for n in range(1, 100000):
#     circle_1 = 50 * (1 + sin(radians(n * 10)))
#     circle_2 = 50 * (1 + cos(radians(n * 10)))
#     print("#".center(int(circle_1)))
#     print("*".center(int(circle_2)))
#     sleep(0.05)


# Write a Python function to round up a number to specified digits
# import math
# def roundup(a, digits=0):
#     n = 10**-digits
#     return round(math.ceil(a / n) * n, digits)
# x = 123.01247
# print("Original  Number: ",x)
# print(roundup(x, 0))
# print(roundup(x, 1))
# print(roundup(x, 2))
# print(roundup(x, 3))


# Write a Python program for casino simulation.
# import random
# import math
# limit = 1000
# acc = 0
# results = []
# exp = 1000
# for i in range(exp):
#   color = 0
#   amount = 10000
#   max_amount = amount
#   bid = 1
#   count = 0
#   while count < limit and amount > 0 :
#     amount = amount - bid
#     next = random.randint(0, 1)
#     if next == color :
#       amount = amount + bid + bid
#       bid = 1
#       # color = 1 if color == 0 else 0
#       if amount > max_amount:
#         max_amount = amount
#     else :
#       bid = bid + bid
#     count = count + 1
#   acc = acc + max_amount
#   results.append(max_amount)
#   print("Exp {}".format(i))
# avg = acc / exp
# acc = 0
# for i in range(len(results)):
#   acc = acc + math.pow(results[i] - avg, 2)
# std = math.sqrt(acc / exp)
#
# print("Average max amount earned {} with standard deviation {}".format(avg, std))


# Write a program to reverse a range
# def reversed_range(start, stop=None, step=1):
#   if stop is None:
#     return range(start - step, -step, -step)
#   else:
#     new_start = stop - ((stop-start-1) % step + 1)
#     new_end = new_start - (stop-start+step-1) // step * step
#     if (stop - start) % step == 0 and step < 0: new_start -= step
#     return range(new_start, new_end, -step)
# print(reversed_range(1, 10, 2))
# print(reversed_range(1, 5, 1))


# spiral way to print matrix containing 123456789
# def generateMatrix(n):
#     if n <= 0:
#         return []
#     matrix = [row[:] for row in [[0] * n] * n]
#     row_st = 0
#     row_ed = n - 1
#     col_st = 0
#     col_ed = n - 1
#     current = 1
#     while (True):
#         if current > n * n:
#             break
#         for c in range(col_st, col_ed + 1):
#             matrix[row_st][c] = current
#             current += 1
#         row_st += 1
#         for r in range(row_st, row_ed + 1):
#             matrix[r][col_ed] = current
#             current += 1
#         col_ed -= 1
#         for c in range(col_ed, col_st - 1, -1):
#             matrix[row_ed][c] = current
#             current += 1
#         row_ed -= 1
#         for r in range(row_ed, row_st - 1, -1):
#             matrix[r][col_st] = current
#             current += 1
#         col_st += 1
#     return matrix
# print(list(generateMatrix(3)))


# Write a Python program to calculate clusters using Hierarchical Clustering method
# import math
# def distance(a, b):
#     x = float(a[0]) - float(b[0])
#     x = x * x
#     y = float(a[1]) - float(b[1])
#     y = y * y
#     dist = round(math.sqrt(x + y), 2)
#     return dist
# def minimum(matrix):
#     p = [0, 0]
#     mn = 1000
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[i])):
#             if (matrix[i][j] > 0 and matrix[i][j] < mn):
#                 mn = matrix[i][j]
#                 p[0] = i
#                 p[1] = j
#     return p
# def newpoint(pt):
#     x = float(pt[0][0]) + float(pt[1][0])
#     x = x / 2
#     y = float(pt[0][1]) + float(pt[1][1])
#     y = y / 2
#     midpoint = [x, y]
#     return midpoint
# if __name__ == '__main__':
#     n = int(input("Input number of points.> "))
#     points = list()
#     outline = '['
#     i = 0
#
#     while (i < n):
#         s = input("Input point (eg. 1,1)" + chr(65 + i) + "> ")
#         c = s.split(",")
#         points.append(c)
#         i = i + 1
#     names = {}
#     for i in range(0, len(points)):
#         names[str(points[i])] = chr(65 + i)
#     l = 0
#     while (len(points) > 1):
#         l = l + 1
#         matrix = list()
#         print('Distance matrix no. ' + str(l) + ': ')
#         for i in range(0, len(points)):
#             m = []
#             for j in range(0, len(points)):
#                 m.append(0)
#             for j in range(0, len(points)):
#                 m[j] = distance(points[i], points[j])
#             print(str(m))
#             matrix.append(m)
#         m = minimum(matrix)
#         pts = list()
#         p1 = points[m[0]]
#         pts.append(p1)
#         points.remove(p1)
#         p2 = points[m[1] - 1]
#         pts.append(p2)
#         points.remove(p2)
#         midpoint = newpoint(pts)
#         points.append(midpoint)
#         c1 = names.pop(str(p1))
#         c2 = names.pop(str(p2))
#         names[str(midpoint)] = "[" + str(c1) + str(c2) + "]"
#         outline = names[str(midpoint)]
#     print("Cluster is :", names[str(midpoint)])


# Write a Python program to implement Euclidean Algorithm to compute the greatest common divisor (gcd).
# from math import *
# def euclid_algo(x, y, verbose=True):
#     if x < y:  # We want x >= y
#         return euclid_algo(y, x, verbose)
#     print()
#     while y != 0:
#         if verbose: print('%s = %s * %s + %s' % (x, floor(x / y), y, x % y))
#         (x, y) = (y, x % y)
#     if verbose: print('gcd is %s' % x)
#     return x
# euclid_algo(150, 304)
# euclid_algo(1000, 10)
# euclid_algo(150, 9)


# Write a Python program to convert RGB color to HSV color
# def rgb_to_hsv(r, g, b):
#     r, g, b = r/255.0, g/255.0, b/255.0
#     mx = max(r, g, b)
#     mn = min(r, g, b)
#     df = mx-mn
#     if mx == mn:
#         h = 0
#     elif mx == r:
#         h = (60 * ((g-b)/df) + 360) % 360
#     elif mx == g:
#         h = (60 * ((b-r)/df) + 120) % 360
#     elif mx == b:
#         h = (60 * ((r-g)/df) + 240) % 360
#     if mx == 0:
#         s = 0
#     else:
#         s = (df/mx)*100
#     v = mx*100
#     return h, s, v
# print(rgb_to_hsv(255, 255, 255))
# print(rgb_to_hsv(0, 215, 0))


# 2 byte Hex value
# for i in range(1, 10):
#     print(i, '-->', format(i, '#04x'))

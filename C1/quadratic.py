import math

print("Enter the values of a, b, c in (ax^2 + bx + c) : ")
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

d = (b**2 - 4*a*c)

if d > 0:
    root1 = (-(b) + math.sqrt(d)) / (2*a)
    root2 = (-(b) - math.sqrt(d)) / (2*a)
    print(f"Roots are real and different\nRoot 1 : {root1:.2f}\nRoot 2 : {root2:.2f}")
elif d < 0:
    real = b/2*a
    imag = math.sqrt(-1 * d) / (2 * a)
    print(f"Roots are complex and different\nRoot 1 : {real:.2f} + {imag:.2f}i\nRoot 2 : {real:.2f} - {imag:.2f}i")
else:
    root = -b / (2 * a)
    print(f"Roots are real and same\nRoot : {root:.2f}")

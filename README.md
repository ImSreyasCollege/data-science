<h1 align="center">Data Science</h1>

<h3 align="center">Cycle 1</h3>
<h2 align="center">
  
  [`1`](#1_1) [`2`](#1_2) [`3`](#1_3) [`4`](#1_4) [`5`](#1_5) [`6`](#1_6) [`7`](#1_7)
</h2>

<h3 align="center">Cycle 2</h3>
<h2 align="center">
  
  [`1`](#2_1) [`2`](#2_2) [`3`](#2_3) [`4`](#2_4) [`5`](#2_5) [`6`](#2_6) [`7`](#2_7) [`8`](#2_8) [`9`](#2_9) [`10`](#2_10) [`11`](#2_11) [`12`](#2_12) [`13`](#2_13) [`14`](#2_14) [`15`](#2_15) [`16`](#2_16) [`17`](#2_17)
</h2>

<h3>Cycle 1</h3>

  <h3 id="1_1">1. program to print non prime numbers in a range.</h3>
  
```python
a = int(input("Enter the start of the range : "))
b = int(input("Enter the end of the range : "))

def is_prime(num):
    if num < 2 : return True
    for i in range(2, (num//2)+1):
        if num/i == num//i:
            return True
    return False

for num in range(a, b+1):
    if is_prime(num):
        print(num)
```

  <h3 id="1_2">2. program to print the first N fibonacci series.</h3>

```python
n = int(input("Enter the number of terms : "))

a = 0;
b = 1;

for i in range(0, n):
    print(a)
    c = a+b
    a = b
    b = c
```

  <h3 id="1_3">3. program to find the roots of a quadratic equation(rounded to 2 decimal places).</h3>

```python
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
```

  <h3 id="1_4">4. program to check weather a given number is perfect or not (sum of factors = num).</h3>

```python
num = int(input("Enter a number : "))

def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num // i == num / i:
            sum += i
    return sum == num

if is_perfect(num):
    print(f"Number {num} is perfect")
else:
    print(f"Number {num} is not perfect")
```

  <h3 id="1_5">5. program to display armstrong number up-to 1000.</h3>

```python
for num in range(1, 1001):
    sum = 0
    temp = num

    while temp > 0:
        remainder = temp % 10
        sum += remainder ** len(str(num))
        temp //= 10
    if sum == num:
        print(num)
```

  <h3 id="1_6">6. program to perform bubble sort on a given set of elements.</h3>

```python
n = int(input("Enter the number of terms : "))
a = []
for i in range(0, n):
    a.append(int(input(f"Enter number {i+1} : ")))
print("List before sorting : ", a)

for i in range(0, n-1):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp

print("Bubble sorted list is : ", a)
```

  <h3 id="1_7">7. program to accept a 10 digit mobile number and find the digits which are absent in it.</h3>

```python
num = int(input("Enter a mobile number : "))
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(str(num)) == 10:
    while num > 0:
        digit = num % 10
        if digit in numbers:
            numbers.remove(digit)
        num //= 10
    print(numbers)
else:
    print("Mobile number should contain 10 numbers.")
```

<h3>Cycle 2</h3>

<h3 id="2_1">1. Create a three dimensional array specifying float data type and print it.</h3>

```python
from numpy import array

numpy_array = array([
    [
        [
            10.2,
            20.8
        ],
        [
            11.4,
            2.9
        ]
    ],
    [
        [
            9.8,
            5.4
        ],
        [
            8.3,
            7.1
        ]
    ]
], dtype=float)
print("3D array : ", numpy_array)
```

<h3 id="2_2">
    2. Create a 2D array (2X3) with elements belonging to complex data type and print it, also display
        a. no.of rows and columns
        b. dimensions of an array
        c. reshape the same array to 3X2
</h3>

```python
from numpy import array

arr = array([
    [
        1 + 2j,
        3 - 2j,
        7 - 9j,
    ],
    [
        4 + 3j,
        8 + 1j,
        5 + 5j
    ]
], dtype=complex)

print("array is : ", arr)

# tuple destructuring (arr.shape returns a tuple with a size of 2)
(rows, cols) = arr.shape
print("number of rows : ", rows)
print("number of cols : ", cols)

dim = arr.ndim
print("array dimension : ", dim)

reshaped_arr = arr.reshape(3, 2)
print("reshaped array : ", reshaped_arr)
```

<h3 id="2_3">3. </h3>

```python
```

<h3 id="2_4">4. </h3>

```python
```

<h3 id="2_5">5. </h3>

```python
```
<h3 id="2_6">6. </h3>

```python
```

<h3 id="2_7">7. </h3>

```python
```

<h3 id="2_8">8. </h3>

```python
```

<h3 id="2_9">9. </h3>

```python
```

<h3 id="2_10">10. </h3>

```python
```

<h3 id="2_11">11. </h3>

```python
```

<h3 id="2_12">12. </h3>

```python
```

<h3 id="2_13">13. </h3>

```python
```

<h3 id="2_14">14. </h3>

```python
```

<h3 id="2_15">15. </h3>

```python
```

<h3 id="2_16">16. </h3>

```python
```

<h3 id="2_17">17. </h3>

```python
```

<h1 align="center">Data Science</h1>

<details>
  <summary>1. program to print non prime numbers in a range.</summary>
  
```python
a = int(input("Enter the start of the range : "))
b = int(input("Enter the end of the range : "))

def is_prime(num):
    if num < 2 : return True
    for i in range(2, (num//2)+1):
        if num/i == num//i :
            return True
    return False

for num in range(a, b+1):
    if is_prime(num):
        print(num)
```
</details>
<details>
  <summary>2. program to print the first N fibonacci series.</summary>

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
</details>

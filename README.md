<h1 align="center">Data Science</h1>

<details>
  <summary>
    
  **1. program to print non prime numbers in a range.**
  </summary>
  
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

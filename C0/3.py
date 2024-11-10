print("Name   : sreyas")
print("Reg.no : SJC23MCA-2053")
print("Roll.no : 53")
print("Batch : MCA 2023-25")

def count_vowels(string):
  vowel_count = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
  string = string.upper()
  for char in string:
    if char in vowel_count:
      vowel_count[char] += 1
  return vowel_count

input_string = input("Enter a string: ")
vowel_counts = count_vowels(input_string)
for vowel, count in vowel_counts.items():
  print(f"{vowel}: {count}")
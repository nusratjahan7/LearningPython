str1 = "this is a string."
str2 = "hello"

# String concatenation
str3 = str1 + " " + str2
print(str3)

# String length
print("Length of str1:", len(str1))
print("Length of str2:", len(str2))

# String indexing
print("First char of str1:", str1[0])
print("Last char of str1:", str1[-1])

# String slicing
print("str1[0:4]:", str1[0:4])
print("str1[:4]:", str1[:4])
print("str1[4:]:", str1[4:])

# String methods
print("Uppercase:", str1.upper())
print("Lowercase:", str2.lower())
print("Replace:", str1.replace("string", "python"))
print("Split:", str1.split())

# String formatting
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

# Boolean operations
val1 = True
val2 = False
print("val1 and val2:", val1 and val2)
print("val1 or val2:", val1 or val2)
print("not val1:", not val1)

# Lists
fruits = ["apple", "banana", "cherry", "date"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# List methods
fruits.append("elderberry")
print("After append:", fruits)
fruits.remove("banana")
print("After remove:", fruits)
print("Length of fruits list:", len(fruits))

# List slicing
print("First two fruits:", fruits[0:2])
print("Last two fruits:", fruits[-2:])

# Loops
print("\nIterating through fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# Range-based loop
print("\nCounting to 5:")
for i in range(1, 6):
    print(f"  {i}")

# While loop
count = 3
print("\nCountdown:")
while count > 0:
    print(f"  {count}")
    count -= 1
print("  Done!")

# Conditional statements
num = 10
if num > 0:
    print(f"\n{num} is positive")
elif num < 0:
    print(f"\n{num} is negative")
else:
    print("\nNumber is zero")




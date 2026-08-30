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

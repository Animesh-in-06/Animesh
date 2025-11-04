# 1. Print numbers from 1 to 10
print("1. Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)
print("-----------------------------")

# 2. Print even numbers from 1 to 20
print("2. Even numbers from 1 to 20:")
for i in range(2, 21, 2):
    print(i)
print("-----------------------------")

# 3. Print each character of a word
print("3. Characters in the word 'Python':")
for char in "Python":
    print(char)
print("-----------------------------")

# 4. Print sum of first 10 natural numbers
print("4. Sum of first 10 natural numbers:")
sum_num = 0
for i in range(1, 11):
    sum_num += i
print("Sum =", sum_num)
print("-----------------------------")

# 5. Print multiplication table of a number
print("5. Multiplication table of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
print("-----------------------------")

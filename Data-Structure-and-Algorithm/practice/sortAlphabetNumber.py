"""
Sort Alphabet and Number
Given string input, sort alphabets in ascending order and add sum of integers.

# Example
Input: K1KA5CB7
Output: ABCKK13


isalpha(): return true or false if char is character.


"""


# My Code
s = input()
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

result = sorted(s)

count = 0
for i in range(len(result)):
    if result[i] in num:
        count += int(result[i])
    else:
        index = i
        break

result = result[index:-1]
result = ''.join(result) + str(count)

print(result)


# Example
data = input()

result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))

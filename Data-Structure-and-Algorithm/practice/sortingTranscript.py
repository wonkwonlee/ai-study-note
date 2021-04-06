"""
Transcript Sorting program

# Lambda function : Anonymous function expression
lambda argument : result

(lambda x : x + 1)(3) >> 4

# Sorting algorithm
"""

n = int(input())    # Input size
dic = {}            # Dictionary data structure

for i in range(n):
    # Use name as key and grade as value
    name, grade = map(str, input().split())
    dic[int(grade)] = name

# Built-in sort algorithm, descending order if reverse=True
sorted_grade = sorted(dic.keys(), reverse=True)
# print(sorted_grade)   # Check if grades are reverse sorted
sorted_name = []
for x in sorted_grade:
    # Find the name of each corresponding grade
    sorted_name.append(dic[x])

print(sorted_name)


# Example code
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    # Store name as str and grade as int
    array.append((input_data[0], int(input_data[1])))

# Lambda function - use key to sort by grade(student[1])
array = sorted(array, key=lambda student: student[1])

# Counting sort
for student in array:
    print(student[0], end=' ')

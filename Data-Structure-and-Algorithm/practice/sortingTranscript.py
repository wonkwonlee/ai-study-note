"""
성적 정렬 프로그램
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

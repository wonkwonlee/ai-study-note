"""
Sorting by Korean, Math, and English

N number of students with name, Korean, Math, and English score.
1. Descending order by Korean score
2. If Korean score is equal, ascending order by English score.
3. If Korean and English scores are equal, Descending order by Math score.
4. If all scores are equal, ascending dictionary order by name. 

# Sort by ascending first element and then descending second element
list.sort(key=lambda x: (x[0], -x[1]))
"""


n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in students:
    print(i[0])

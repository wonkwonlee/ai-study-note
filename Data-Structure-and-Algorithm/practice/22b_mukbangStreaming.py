"""
Muji's Mukbang Streaming

Input1: food_times array to store food consuming time in second
Input2: K seconds of streaming delay
Output: Return next food, or -1 if none exists.
"""


def solution(food_times, k):
    answer = 0
    dic = {}
    for i in range(len(food_times)):
        dic[food_times[i]] = i

    while k > 0:
        # One cycle of food mukbang
        cycle = len(food_times)
        # Minimum time
        min_t = min(food_times)
        # Index of minimum time
        min_i = food_times.index(min_t)

        # print(food_times)
        if k > cycle * min_t:
            k -= cycle * min_t
            answer = dic.get(food_times[min_i])
            food_times.pop(answer)
        else:
            res = k % cycle
            answer = dic.get(food_times[res])
            k = 0

    return answer + 1

print(solution([3,1,2], 5))     # 1
print(solution([8,6,4], 15))    # 2

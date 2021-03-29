# 정렬 알고리즘 Sorting Algorithm


## 정렬 Sort
* 정렬이란 **데이터를 특정한 기준에 따라서 순서대로 나열하는 것**을 말한다. 
* 프로그래밍에서는 데이터를 가공할 때 오름차순이나 내림차순 등 데이터를 정렬해서 사용하는 경우가 많다.
* 정렬 알고리즘은 **이진 탐색의 전처리 과정**이고 데이터를 정렬하면 이진 탐색이 가능하다.
* 정렬 알고리즘에는 *선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬* 등이 있다.


## 선택 정렬 Selection Sort
* 데이터가 무작위로 여러 개 있을 때, **가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복**하는 방식이다.
* *가장 원시적인 방법*으로 **매번 가장 작은 것을 선택한다**는 의미에서 선택 정렬 알고리즘이라고 한다.
* *즉, 가장 작은 것을 선택해서 앞으로 보내는 과정을 반복*하다 보면, 전체 데이터의 정렬이 이루어진다.

```python
array = [7,5,9] # Initialize an array

# Find the index of min value
for i in range(len(array)): 
    min_index = i
    # Loop after the min index
    for j in range(i + 1, len(array)):  
        if array[min_index] > array[j]:
            min_index = j              
    # Swap the current value and min value
    array[i], array[min_index] = array[min_index], array[i]

print(array)

>> [5, 7, 9]
```

### 스왑 Swap
* **스왑(Swap)**이란 *특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업*을 의미한다.
    + 파이썬에서는 간단히 리스트 내 두 원소의 위치를 변경할 수 있다.
* 하지만 다른 대부분의 프로그래밍 언어에서는 명시적으로 임시 저장용 변수를 만들어 두 원소의 값을 변경해야 한다.

```python
array = [3, 5]
array[0], array[1] = array[1], array[0]
print(array)

>> [5, 3]
```



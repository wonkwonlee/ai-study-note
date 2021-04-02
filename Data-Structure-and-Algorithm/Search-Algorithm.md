# 탐색 알고리즘 Search Algorithm

## 순차 탐색 Sequential Search
* 순차 탐색은 이름처럼 **순차로 데이터를 탐색한다는 의미**로 리스트의 데이터에 하나씩 방문하여 특정한 문자열과 같은 지 검사한다.
    + 리스트 내에 *데이터가 아무리 많아도 시간만 충분하다면 항상 원하는 원소(데이터)를 찾을 수 있다*는 장점이 있다.
* 일반적으로 **정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용**한다. 
* 순차 탐색은 *리스트에 특정 값의 원소가 있는지 체크*할 때나 리스트 자료형에서 특정한 값을 갖는 원소의 개수를 세는 **count()** 메서드를 이용할 때 내부에서 수행된다.
* 순차 탐색은 *데이터 정렬 여부와 상관 없이 가장 앞에 있는 원소부터 하나씩 확인*해야 한다는 점이 특징이다.

```python
def sequential_search(n, target, array):
    for i in range(n):
        # Search if target is equal to sequential data in the array
        if array[i] == target: 
            return i + 1
```

## 이진 탐색 Binary Search
* 이진 탐색은 **탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방식**으로 작동한다.
* 이진 탐색은 **배열의 내부가 정렬되어 있어야만 사용**할 수 있는 알고리즘으로 데이터가 무작위일 때는 사용할 수 없지만, *이미 정렬되어 있다면 빠르게 데이터를 찾을 수 있다.*
* 이진 탐색에는 탐색하고자 하는 범위의 시작점, 끝점, 그리고 중간점의 변수 3개를 사용한다. 
    + *찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교*해서 원하는 데이터를 찾는 게 이진 탐색 과정이다.
 
<img width="883" alt="binary1" src="https://user-images.githubusercontent.com/28593767/113076290-abd29e00-9209-11eb-81d5-29fe1aa3217e.png">

<img width="883" alt="binary2" src="https://user-images.githubusercontent.com/28593767/113076368-d886b580-9209-11eb-93a6-029762a02b5a.png">

<img width="883" alt="binary3" src="https://user-images.githubusercontent.com/28593767/113076294-aecd8e80-9209-11eb-99d4-e58e98a793ff.png">

* 이진 탐색은 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 퀵 정렬과 공통점이 있다.
* 이진 탐색 알고리즘은 한 단계를 거칠 때마다 확인하는 원소가 평균적으로 절반으로 줄어들기 때문에 연산 횟수가 크게 줄어든다.
* 일반적으로 재귀 함수를 이용하거나 반복문을 이용해서 구현한다.

```python
def binary_search(array, target, start, end):
    if start > end: 
        return None 
    # Find middle point (Ignore decimal point)
    mid = (start + end) // 2
    # If target is equal to mid val
    if array[mid] == target:
        return mid
    # If target is smaller than mid val, use recursion to left side
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # If target is larger than mid val, use recursion to right side
    else:
        return binary_search(array, target, mid + 1, end)
```

### 코딩 테스트에서의 이진 탐색
* 코드만 보면 이진 탐색이 단순하다고 느낄 수도 있지만, *참고할 소스코드가 없는 상태에서 이진 탐색의 소스코드를 구현하는 것*은 상당히 어려운 작업이 될 수 있다. 
* 존 벤틀리의 말을 인용하면 *제대로 이진 탐색 코드를 작성한 프로그래머는 10% 내외라 할 정도로 실제 구현은 까다로운 알고리즘*이다.
* 이진 탐색의 원리는 다른 알고리즘에서도 폭넓게 적용되는 원리와 유사하기 때문에 매우 중요하고 *높은 난이도의 문제에서는 이진 탐색 알고리즘이 다른 알고리즘과 함께 사용*되는 경우도 많다.
    + 실제로 대회에서 그리디 알고리즘과 이진 탐색 알고리즘을 모두 사용해서 풀어야 하는 문제가 출제된 적이 있다.
* 코딩 테스트의 이진 탐색 문제는 *탐색 범위가 큰 상황에서의 탐색을 가정*하는 문제가 많기 때문에 탐색 범위가 1000만 단위 이상으로 넘어가면 고려해볼만 하다.


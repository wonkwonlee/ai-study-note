# 스택과 큐 Stack and Queue

> 탐색(Search)이란 **많은 양의 데이터 중에서 원하는 데이터를 찾는 과정**을 의미한다. 프로그래밍에서는 그래프, 트리 등의 자료 구조 안에서 탐색을 하는 문제를 자주 다루게 된다.
>
> 대표적인 탐색 알고리즘으로 **DFS(Depth-First Search)** 와 **BFS(Bredth-First Search)** 가 있는데 이 두 알고리즘을 제대로 이해해야 탐색 문제 유형을 풀 수 있다.
>
> DFS와 BFS를 제대로 이해하려면 기본 자료 구조인 스택과 큐에 대한 이해가 전제되어야 한다.


## 자료 구조 Data Structure
* 자료 구조란 **데이터를 표현하고 관리하고 처리하기 위한 구조**를 의미한다.
* 스택과 큐는 자료 구조의 기초 개념으로 다음의 두 핵심 학수로 구성된다.
    + 삽입 Push : 데이터를 삽입한다. 
    + 삭제 Pop : 데이터를 삭제한다.
* 오버 플로 Overflow : 특정한 자료 구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행하면 저장 공간을 벗어나 데이터가 넘쳐흘러 발생한다.
* 언더 플로 Underflow : 특정한 자료 구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행하면 데이터가 전혀 없는 상태이므로 발생한다.


## 스택 Stack
![stack](https://user-images.githubusercontent.com/28593767/111928125-1d1d9d00-8af6-11eb-9bed-8c122e002355.png)

* 스택은 *박스 쌓기에 비유할 수 있다*. 일반적으로 박스는 아래에서부터 위로 아래에 있는 박스를 지우기 위해서는 위에 있는 박스를 먼저 내려야 한다.
* 이러한 구조를 **선입후출(First-In Last-Out)** 구조 또는 **후입선출(Last-In First-Out)** 구조라고 한다.
* 파이썬에서 스택을 이용할 때는 별도의 라이브러리를 사용할 필요가 없다. 기본 리스트에서 **append()** 와 **pop()** 메서드를 사용하면 스택 자료구조와 동일하게 동작한다.
    + append() : 리스트의 가장 뒤쪽에 데이터를 삽입한다.
    + pop() : 리스트의 가장 뒤쪽에서 데이터를 꺼낸다.

```python
stack = [] 
stack.append(5)     # 5
stack.append(2)     # 5, 2
stack.append(3)     # 5, 2, 3
stack.append(7)     # 5, 2, 3, 7
stack.pop()         # 5, 2, 3  
stack.append(1)     # 5, 2, 3, 1
stack.append(4)     # 5, 2, 3, 1, 4
stack.pop()         # # 5, 2, 3, 1

print(stack)        # 최 하단 원소부터 출력    
print(stack[::-1])  # 최 상단 원소부터 출력

[5, 2, 3, 1]
[1, 3, 2, 5]
```


## 큐 Queue

![queue](https://user-images.githubusercontent.com/28593767/111928124-1c850680-8af6-11eb-9130-7c692100483a.png)

* 큐는 *대기 줄에 비유할 수 있다*. 일반적으로 대기 줄은 먼저 온 사람이 먼저 들어가고 나중에 온 사람이 나중에 들어가기 때문에 공정한 자료 구조라고 비유된다.
* 이러한 구조를 **선입선출(First-In First-Out)** 구조라고 한다.
* 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있다.
* 파이썬에서 큐를 표현할 때는 collections 모듈에서 제공하는 **deque** 자료구조를 활용한다.
* deque는 스택과 큐의 장점을 모두 채택한 것으로 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단하다. 
    + 대부분의 코딩 테스트에서는 collections 모듈과 같은 기본 라이브러리 사용을 허용한다.


```python
from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)     # 5
queue.append(2)     # 5, 2
queue.append(3)     # 5, 2, 3
queue.append(7)     # 5, 2, 3, 7
queue.popleft()     # 2, 3, 7
queue.append(1)     # 2, 3, 7, 1
queue.append(4)     # 2, 3, 7, 1, 4
queue.popleft()     # 3, 7, 1, 4

print(queue)        # 먼저 들어온 순서대로 출력
queue.reverse()     # 다음 출력을 위해 역순으로 바꾸기
print(queue)        # 나중에 들어온 원소부터 출력

deque([3, 7, 1, 4])
deque([4, 1, ,7, 3])
```


## 재귀 함수 Recursive Function

```python
def recusive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시 
    if i == 100:
        return
    print(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.") 
    recusive_function(i+1)
    print(i, "번째 재귀 함수를 종료합니다.")

recusive_function(1)

```

* 재귀 함수란 **자기 자신을 다시 호출하는 함수**를 의미한다.
* 재귀 함수를 사용할 때는 재귀 함수가 언제 끝날지, *종료 조건을 꼭 명시*해야 한다. 
* 종료 조건을 명시하지 않으면 함수가 무한히 호출되어 재귀의 최대 깊이를 초과했다는 오류가 발생한다.
    + *RecursionError: maximum recursion depth exceeded while calling a Python object*
* 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문에 *컴퓨터 내부에서 재귀 함수의 수행은 스택 자료 구조를 이용*한다.
    + 즉, 스택 자료 구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있다.

### 반복문과 재귀 함수로 구현한 팩토리얼
```python
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기 
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환 
        return 1
    # n! = n * (n-1)! 를 그대로 코드로 작성하기 
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현하는 n! 출력 (n = 5) 
print("반복적으로 구현 :", factorial_iterative(5)) 
print("재귀적으로 구현 :", factorial_recursive(5))

# 결과값은 둘다 동일
반복적으로 구현 : 120 
재귀적으로 구현 : 120
```
![fac](https://user-images.githubusercontent.com/28593767/111928120-1b53d980-8af6-11eb-9062-909ce0864e31.png)

* 실행 결과는 동일하지만 재귀 함수는 수학의 점화식(재귀식)을 그대로 소드 코드로 옮겼기 때문에 더 간결하게 표현된다.
* 점화식은 **특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것**을 의미한다.
* 일반적으로 재귀 함수는 반복문보다 더 빠르고 더 효율적이다.



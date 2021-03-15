# 알고리즘 복잡도 Complexity of Algorithm

## 알고리즘의 정의
> 문제를 풀기 위한 효율적인 절차
>
> 문제를 풀기 위한 단계별 절차를 명확하게 기술

## 복잡도 Complexity
> 알고리즘의 성능을 나타내는 척도

* 시간 복잡도 Time Complexity : 입력 크기 vs 걸리는 시간
    + 알고리즘을 위해 필요한 *연산의 횟수*
* 공간 복잡도 Space Complexity : 입력 크기 vs 필요한 메모리
    + 알고리즘을 위해 필요한 *메모리의 양*


## Big-O Notation
> 가장 빠르게 증가하는 항만을 고려하는 표기법
* 연산 횟수는 N에 비례
* Constant 연산은 N이 커질수록 상대적으로 무시할 수 있을 정도로 작아짐
* N개의 element를 검사하는 for-loop의 Time Complexity는 O(N)


### Quiz 1 : 정수를 담고 있는 배열의 평균값을 return하는 함수를 만들어보시오.

```python
def average(list):
    if len(list) == 0:
        return 0
    
    return sum(list) / len(list)
```
### Quiz 2 : 정수가 짝수일 경우 Even을 return하고 홀수일 경우 Odd를 return하는 함수를 만들어보시오.

```python
def eveOrOdd(num):
    if (num % 2) == 0:
        return "Even"
    else:
        return "Odd"
```

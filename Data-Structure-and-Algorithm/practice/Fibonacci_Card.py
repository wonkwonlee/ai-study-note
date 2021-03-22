"""
피보나치 수열을 출력하는 프로그램

조건 1. 함수를 활용하여 문제에서 언급한 피보나치 알고리즘을 작성하시오.
조건 2. for 반복문과 range() 함수를 통해 출력을 제어하시오. (최소 8항의 값 21까지 출력 )
"""

# Recursive method
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

print("========재귀문 방식========")
for i in range(8):
    print(fibonacci(i+1))

# List method
fib_list = [1,1]

print("========배열 방식========")
for i in range(0,10):
    # 파이썬에서 음수 인덱스는 가장 뒤부터 시작한다
    # 즉, arr[-1]은 배열 맨 뒤, arr[-2]은 맨 뒤에서 2번째
    fib_list.append(fib_list[-1] + fib_list[-2])

print(fib_list)
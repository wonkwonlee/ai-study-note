# 기초 수학 Basic Mathematics

## 변수와 상수 Variable and Constant
* 변수 Variable : 값이 고정되지 않아 **다양한 값이 들어올 수 있다**
    + 주로 x나 y같은 문자 사용
* 상수 Constant : 값이 고정되어 **변하지 않는다**
    + 주로 a나 b같은 문자 사용
* 인공지능의 신경망에서 **가중치(weight)**는 컴퓨터가 스스로 학습하여 결정한다
    + 재미있는 점은 컴퓨터가 가중치를 학습할 때는 가중치가 *변수*의 역할을 하고, 학습이 끝나고 해당 가중치를 학습 모델에 활용할 때는 *상수*의 역할을 한다


## 1차식과 2차식 Linear equation and Quadratic equation
* 항 Term : 숫자나 문자, 또는 그 둘의 곱으로 표현되는 식
    + 3, a, 3a, -4ab, x/3, a^2
* 차수 Degree : 각각의 항에 변수가 곱해진 횟수
    + 상수의 차수는 0
* 계수 Coefficient : 각 항에서 변수에 해당하는 문자를 제외한 부분
    + 3의 계수는 3, 5a의 계수는 5, x/3의 계수는 1/3
* 단항식 Monomial : 1개의 항으로 만들어진 식
* 다항식 Polynomial : 여러 개의 항이 더하기로 연결된 식


* **Linear equation**, x에 대한 1차식 : *ax + b* (단, a != 0)
    + 직선 모양
    + 계수 a는 직선의 기울기
    + b는 x = 0일 때의 y값 절편 (y-intercept)

![1st](https://user-images.githubusercontent.com/28593767/111255052-b01f8880-8659-11eb-8d2c-68f772c3ce9e.png)

* **Quadratic equation**, x에 대한 2차식 : *ax^2 + bx + c* (단, a != 0)
    + 포물선 모양
    + 계수 a가 양수이면 포물선이 아래로 볼록하고, a가 음수이면 위로 볼록하다

![2nd](https://user-images.githubusercontent.com/28593767/111255094-c6c5df80-8659-11eb-990d-0c59f7a79b4f.png)

## 함수의 개념 Function
> 함수란 어떤 입력값 x에 따라 *하나의* 출력값 y가 결정된다면 y는 x의 함수라고 하고
>
> *y = f(x)* 라고 표기한다.

* 함수는 인공지능 뿐 아니라 프로그래밍에서도 반드시 필요한 개념
* 프로그래밍에서 말하는 함수는 수학에서 말하는 함수보다 개념이 확장되어 어떤 입력값에 대해 *True*나 *False*같은 형태나 문자열 같은 형태도 출력값으로 사용할 수 있다


## 제곱근 Square root
* 제곱을 했을 때 어떤 수 x가 되는 값을 그 어떤 수 x에 대한 제곱근이라 한다
* *a = b^2* 일 때, b를 a의 제곱근이라 하고 *b = sqrt(a)* 라고 표기한다
* 제곱근 기호를 *근호*라고 한다
* 실수에서는 양수에 대한 제곱근이 **반드시 두 개** 존재한다

![root](https://user-images.githubusercontent.com/28593767/111255135-d2b1a180-8659-11eb-9019-9b0e21efff2c.png)


## 거듭제곱과 거듭제곱근 Exponentiation and n-th Root
* 거듭제곱 Exponentiation : a를 p번 곱한 것을 a의 p제곱, 또는 a의 p승이라고 부르고, a^p 와 같이 표기한다
    + **a를 밑, p를 지수**라 한다
* 거듭제곱근 n-th Root : p제곱을 하면 a가 되는 수, 또는 p승을 하면 a가 되는 수를 a의 p제곱근이라 하고 <img width="20" alt="sqrt" src="https://user-images.githubusercontent.com/28593767/111248845-10103200-864e-11eb-857a-b0b8f0b8b564.png"> 와 같이 표기한다

<img width="555" alt="sqrt_eq" src="https://user-images.githubusercontent.com/28593767/111248702-c58eb580-864d-11eb-8fdd-e4c9171174b4.png">


## 지수함수와 로그함수 Exponential function and Logarithmic function
> 지수함수란 지수에 변수를 사용하는 함수로 다음과 같다
>
> * a > 0, a != 1* 이라고 가정할 때, *y = a^x* 라고 표현되는 함수를 의미한다

* 지수함수는 **밑인 a가 1보다 큰지, 작은지에 따라** 그래프의 모양이 달라진다
* *a > 1* 일 때 그래프는 오른쪽으로 올라가는 모양이고 *0 < a < 1* 일 때 그래프는 오른쪽으로 내려가는 모양이다
* *x = 0* 일 때, *a^0 = 1* 이고 *x = 1* 일 때, *a^1 = a* 이다

![func](https://user-images.githubusercontent.com/28593767/111254256-fa076f00-8657-11eb-8ec8-184478699e2e.png)


> 로그는 지수와는 *정 반대의 개념*이다
>
> 어떤 x에 대해서 *x = a^y* 라고 표현 될 때의 지수 y를 a를 밑으로 하는 x의 로그라고 하며, *y = log_a(x)* 와 같이 표현한다
>
> 이 때, x를 진수라고 하는데 *a > 0, a != 1* 이고 *x > 0* 이다

![log](https://user-images.githubusercontent.com/28593767/111300037-014c6e00-8694-11eb-82f4-199ea39b6c30.png)


> 로그함수란 *a > 0, a != 1* 이고 *x > 0* 일 때, 다음과 같이 표현되는 함수를 로그함수라고 한다
>
> *y = log_a(x)*

* 로그함수는 **밑인 a가 1보다 큰지, 작은지에 따라** 그래프의 모양이 달라진다
* *a > 1* 일 때 그래프는 오른쪽으로 올라가는 모양이고 x가 0에 가까울 수록 함숫값은 음의 무한대로 발산한다
* *0 < a < 1* 일 때 그래프는 오른쪽으로 내려가는 모양이고 x가 0에 가까울 수록 함숫값은 양의 무한대로 발산한다
* *x = 1* 일 때, *y = 0* 이 되므로 점 (1, 0)을 반드시 통과한다
* 로그함수는 반드시 (a, 1)을 통과한다
    + *y = log_a(a)* 라고 가정할 때, *a^y = a* 이므로, *y = 1* 이다

![log_func](https://user-images.githubusercontent.com/28593767/111300079-0b6e6c80-8694-11eb-990b-38fd98bcfbd5.png)


### 인공지능에서의 로그함수 Logarithm in AI
* 인공지능에서는 **가능성을 나타내는 척도로 가능도(likelihood)라는 것을 이용**하는데, 이러한 가능도를 다루는 함수를 **가능도함수**라고 한다
* 가능도함수는 확률을 계산하는 식과 같고 0 이상 1 이하의 값을 가지고 일반적으로 가능도의 로그를 사용한 **로그 가능도함수**를 많이 사용한다
* 또한 로그를 사용하면 *log_a(XY) = log_a(X) + log_a(Y)* 와 같이 곱셈을 덧셈으로 표현할 수 있고 값이 작아지기에 계산이 더 쉬워진다


## 자연로그 Natural Logarithm

> Euler's number **e**
>
> n의 값이 커질수록 (1+1/n)^2의 값은 일정한 값 2.7182... 에 가까워지고, 이 수를 Euler's number, Napier's constant, 또는 Base of Natural Logarithm이라 한다
>
> *e*는 유용한 특징을 지니고 있는데, *d/dx(e^x) = e^x* 나 *ln x = 1/x* 과 같은 특징 등이다

<!-- 자연로그 -->

## 절댓값과 유클리드 거리 Absolute value and Euclidean distance
* 절댓값 Absolute value : 어떤 수와 0과의 수직선 상의 거리
    + 절댓값 기호 안에 있던 숫자나 문자가 양수라면 그대로 꺼낼 수 있지만, 음수라면 부호를 바꿔서 꺼내야 한다
    + Modulus 라고도 한다
* 유클리드 거리 Euclidean distance : 한 점과 다른 한 점 사이를 자로 잰 것과 같은 거리를 의미한다
    + 즉, n차원의 공간에서 두 점간의 거리를 알아내는 공식이다
    + 점 A와 원점 사이의 유클리드 거리는 ||*A*|| 라고 표현하고, 점 A와 점 B의 두 점 사이의 거리는 ||*A - B*|| 로 표현할 수 있다

<!-- 유클리드 공식 -->

## 수열



## 집합과 원소





















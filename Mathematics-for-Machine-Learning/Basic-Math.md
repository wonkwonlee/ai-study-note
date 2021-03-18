# 기초 수학 Basic Mathematics

## 변수와 상수 Variable and Constant
* 변수 Variable : 값이 고정되지 않아 **다양한 값이 들어올 수 있다**.
    + 주로 x나 y같은 문자 사용
* 상수 Constant : 값이 고정되어 **변하지 않는다**.
    + 주로 a나 b같은 문자 사용
* 인공지능의 신경망에서 **가중치(weight)**는 컴퓨터가 스스로 학습하여 결정한다.
    + 재미있는 점은 컴퓨터가 가중치를 학습할 때는 가중치가 *변수*의 역할을 하고, 학습이 끝나고 해당 가중치를 학습 모델에 활용할 때는 *상수*의 역할을 한다.


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
    + 계수 a가 양수이면 포물선이 아래로 볼록하고, a가 음수이면 위로 볼록하다.

![2nd](https://user-images.githubusercontent.com/28593767/111255094-c6c5df80-8659-11eb-990d-0c59f7a79b4f.png)

## 함수의 개념 Function
> 함수란 어떤 입력값 x에 따라 *하나의* 출력값 y가 결정된다면 y는 x의 함수라고 하고
>
> *y = f(x)* 라고 표기한다.

* 함수는 인공지능 뿐 아니라 프로그래밍에서도 반드시 필요한 개념
* 프로그래밍에서 말하는 함수는 수학에서 말하는 함수보다 개념이 확장되어 어떤 입력값에 대해 *True*나 *False*같은 형태나 문자열 같은 형태도 출력값으로 사용할 수 있다.


## 제곱근 Square root
* 제곱을 했을 때 어떤 수 x가 되는 값을 그 어떤 수 x에 대한 제곱근이라 한다.
* *a = b^2* 일 때, b를 a의 제곱근이라 하고 *b = sqrt(a)* 라고 표기한다.
* 제곱근 기호를 *근호*라고 한다.
* 실수에서는 양수에 대한 제곱근이 **반드시 두 개** 존재한다.

![root](https://user-images.githubusercontent.com/28593767/111255135-d2b1a180-8659-11eb-9019-9b0e21efff2c.png)


## 거듭제곱과 거듭제곱근 Exponentiation and n-th Root
* 거듭제곱 Exponentiation : a를 p번 곱한 것을 a의 p제곱, 또는 a의 p승이라고 부르고, a^p 와 같이 표기한다.
    + **a를 밑, p를 지수**라 한다.
* 거듭제곱근 n-th Root : p제곱을 하면 a가 되는 수, 또는 p승을 하면 a가 되는 수를 a의 p제곱근이라 하고 <img width="20" alt="sqrt" src="https://user-images.githubusercontent.com/28593767/111248845-10103200-864e-11eb-857a-b0b8f0b8b564.png"> 와 같이 표기한다.

<img width="555" alt="sqrt_eq" src="https://user-images.githubusercontent.com/28593767/111248702-c58eb580-864d-11eb-8fdd-e4c9171174b4.png">


## 지수함수와 로그함수 Exponential function and Logarithmic function
> 지수함수란 지수에 변수를 사용하는 함수로 다음과 같다.
>
> *a > 0, a != 1* 이라고 가정할 때, *y = a^x* 라고 표현되는 함수를 의미한다.

* 지수함수는 **밑인 a가 1보다 큰지, 작은지에 따라** 그래프의 모양이 달라진다.
* *a > 1* 일 때 그래프는 오른쪽으로 올라가는 모양이고 *0 < a < 1* 일 때 그래프는 오른쪽으로 내려가는 모양이다.
* *x = 0* 일 때, *a^0 = 1* 이고 *x = 1* 일 때, *a^1 = a* 이다.

![func](https://user-images.githubusercontent.com/28593767/111254256-fa076f00-8657-11eb-8ec8-184478699e2e.png)


> 로그는 지수와는 *정 반대의 개념*이다.
>
> 어떤 x에 대해서 *x = a^y* 라고 표현 될 때의 지수 y를 a를 밑으로 하는 x의 로그라고 하며, *y = log_a(x)* 와 같이 표현한다.
>
> 이 때, x를 진수라고 하는데 *a > 0, a != 1* 이고 *x > 0* 이다.

![log](https://user-images.githubusercontent.com/28593767/111300037-014c6e00-8694-11eb-82f4-199ea39b6c30.png)


> 로그함수란 *a > 0, a != 1* 이고 *x > 0* 일 때, 다음과 같이 표현되는 함수를 로그함수라고 한다
>
> *y = log_a(x)*

* 로그함수는 **밑인 a가 1보다 큰지, 작은지에 따라** 그래프의 모양이 달라진다.
* *a > 1* 일 때 그래프는 오른쪽으로 올라가는 모양이고 x가 0에 가까울 수록 함숫값은 음의 무한대로 발산한다.
* *0 < a < 1* 일 때 그래프는 오른쪽으로 내려가는 모양이고 x가 0에 가까울 수록 함숫값은 양의 무한대로 발산한다.
* *x = 1* 일 때, *y = 0* 이 되므로 점 (1, 0)을 반드시 통과한다.
* 로그함수는 반드시 (a, 1)을 통과한다.
    + *y = log_a(a)* 라고 가정할 때, *a^y = a* 이므로, *y = 1* 이다.

![log_func](https://user-images.githubusercontent.com/28593767/111300079-0b6e6c80-8694-11eb-990b-38fd98bcfbd5.png)

### 인공지능에서의 로그함수 Logarithm in AI
* 인공지능에서는 **가능성을 나타내는 척도로 가능도(likelihood)라는 것을 이용**하는데, 이러한 가능도를 다루는 함수를 **가능도함수**라고 한다.
* 가능도함수는 확률을 계산하는 식과 같고 0 이상 1 이하의 값을 가지고 일반적으로 가능도의 로그를 사용한 **로그 가능도함수**를 많이 사용한다.
* 또한 로그를 사용하면 *log_a(XY) = log_a(X) + log_a(Y)* 와 같이 곱셈을 덧셈으로 표현할 수 있고 값이 작아지기에 계산이 더 쉬워진다.


## 자연로그 Natural Logarithm

* Euler's number **e**
* n의 값이 커질수록 (1+1/n)^2의 값은 일정한 값 2.7182... 에 가까워지고, 이 수를 Euler's number, Napier's constant, 또는 Base of Natural Logarithm이라 한다.
* *e*는 유용한 특징을 지니고 있는데, *d/dx(e^x) = e^x* 나 *ln x = 1/x* 과 같은 특징 등이다.

![ln](https://user-images.githubusercontent.com/28593767/111303303-b6345a00-8697-11eb-8b9a-d1c5d2fc0527.png)

## 절댓값과 유클리드 거리 Absolute value and Euclidean distance
* 절댓값 Absolute value : 어떤 수와 0과의 수직선 상의 거리
    + 절댓값 기호 안에 있던 숫자나 문자가 양수라면 그대로 꺼낼 수 있지만, 음수라면 부호를 바꿔서 꺼내야 한다.
    + Modulus 라고도 한다.
* 유클리드 거리 Euclidean distance : 한 점과 다른 한 점 사이를 자로 잰 것과 같은 거리를 의미한다.
    + 즉, n차원의 공간에서 두 점간의 거리를 알아내는 공식이다.
    + 점 A와 원점 사이의 유클리드 거리는 ||*A*|| 라고 표현하고, 점 A와 점 B의 두 점 사이의 거리는 ||*A - B*|| 로 표현할 수 있다.

<img width="500" alt="ed" src="https://user-images.githubusercontent.com/28593767/111303318-bcc2d180-8697-11eb-9dbb-10733f905750.png">

## 수열 Sequence
> 수열을 사용하면 여러 수를 쉽게 다룰 수 있기에 대량의 데이터를 처리하는 인공지능 분야에서는 수열을 자주 사용한다.
>
> 수열이란, 여러 숫자가 일정한 규칙에 따라 줄지어서 배열된 것을 의미한다.
* 항 Term : 수열을 구성하는 숫자 하나하나
* 초항 First term : 수열의 제 1항, a_1
* 말항 Final term : 수열의 마지막 항, a_k

### 등차수열 Arithmetic sequence
> 앞, 뒤에 인접한 항과의 차이가 일정한 수열

* 공차 Common difference : 등차수열에서 앞, 뒤 항과의 차이를 의미
* 즉, 등차수열에서는 **어떤 항에 공차를 더하면 다음 항**을 알 수 있다.
* **등차수열의 일반항** : 초항이 a, 공차가 d일때 다음과 같이 정의한다.
    + ![ar](https://user-images.githubusercontent.com/28593767/111304596-445d1000-8699-11eb-9638-efa6f1fd5a46.png)

* **등차수열의 합 Arithmetic series** : 초항이 a, 말항이 l, 항의 개수는 n일때, 다음과 같이 정의한다.
    + ![ar_sum](https://user-images.githubusercontent.com/28593767/111304713-648ccf00-8699-11eb-8ef5-e50ab9ff3d07.png)

### 등비수열 Geometric sequence
> 앞, 뒤에 인접한 항의 비율이 일정한 수열

* 공비 Ratio : 인접한 항의 비율, r로 표시한다.
* 즉, 등비수열에서는 **어떤 항에 공비를 곱하면 다음 항**을 알 수 있다.
* **등비수열의 일반항** : 초항이 a, 공비가 r일때 다음과 같이 정의한다.
    + ![ge](https://user-images.githubusercontent.com/28593767/111305582-7f137800-869a-11eb-89cd-16369585d0db.png)
* **등비수열의 합 Geometric series** : 초항이 a, 공비가 r일때, 다음과 같이 정의한다.
    + ![ge_sum](https://user-images.githubusercontent.com/28593767/111305578-7de24b00-869a-11eb-9108-23b08ae761b6.png)

### 수열의 합과 곱 Summation and Product notation
> 일반적으로 '시그마'와 '파이'라고 읽는다.

* ![sigma](https://user-images.githubusercontent.com/28593767/111305878-d9acd400-869a-11eb-95f2-222d6049cb8a.png)
* ![sum_pro](https://user-images.githubusercontent.com/28593767/111306051-124cad80-869b-11eb-987b-8618d7bc1596.png)
* 뉴런은 입력값과 가중치의 곱을 더하고 상수를 추가한 값과 같은데 신경망에서는 하나의 모델에 이와 같은 덧셈이 수백만번 이루어지기도 한다. 이 때, Summation을 써서 식을 간단히 표현 할 수 있다.


## 집합과 원소 Set and Element
* 같은 조건을 만족하는 원소들을 *중복되지 않도록* 모은 모둠을 **집합(Set)**이라고 한다.
    + 집합은 어떤 원소가 그 집합에 들어가느냐, 들어가지 않느냐를 정확하게 구분한다.
* 두 개의 집합 A, B가 있을 때, 집합 A의 원소와 집합 B의 원소가 완전히 일치한다면 **집합 A와 B는 같다**고 하고 A = B 와 같이 표현한다.
* 집합 B의 모든 원소가 집합 A의 원소라면 집합 B는 집합 A의 **부분집합(Subset)**이라고 하고 A ⊂ B 와 같이 표현한다.
* 원소가 하나도 없는 집합을 **공집합(Empty set)**이라고 하고 φ 와 같이 표현한다.
* 두 개의 집합 A, B가 있을 때, 두 집합 모두에 속하는 원소들의 집합을 집합 A와 집합 B의 **교집합(Intersection)**이라 하고 A ∩ B 와 같이 표현한다.
* 두 개의 집합 A, B가 있을 때, 두 집합 중 적어도 한 집합에 속하는 원소들의 집합을 집합 A와 집합 B의 **합집합(Union)**이라 하고 A ∪ B 와 같이 표현한다.


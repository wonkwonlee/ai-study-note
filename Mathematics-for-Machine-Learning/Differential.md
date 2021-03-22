# 미분 Differential
> 미분은 그래프의 어느 한 지점에서 아주 짧은 순간에 변화하는 값의 비율을 나타내는 수학적 개념이다.
>
> 머신러닝 분야에는 적분이 거의 사용되지 않기에 이 장에서는 미분에 대해서만 다룰 예정이다.
>
> 머신러닝에서 미분은 *딥러닝, 신경망, 최소 제곱법, 경사 하강법, 오차 역전파법* 등 폭넓게 사용된다.

## 극한 Limit
> 극한이란, 변수 x의 값이 일정한 법칙에 따라 정해진 값 a에 한없이 가까워질 때의 값을 의미한다.
>
> 이렇게 x가 a에 한없이 가까워질 때, 함수 f(x)도 어떤 값에 최대한 가까워지는 모양을 일컫어 **수렴한다**라고 표현한다.
>
> 이때, a는 함수 f(x)에서 x → a 일 때의 **극한값**이라고 한다.

![lim](https://user-images.githubusercontent.com/28593767/111458631-00cbda00-875d-11eb-9379-18ff6255c586.png)


## 미분 Differential
* 어떤 함수의 **특정한 지점에서의 기울기를 구하는 것**을 **미분한다**라고 한다.
* 이것을 *df(x)/dx* 혹은 *f'(x)* 라고 나타내고 **도함수**라고 부른다.
* *x*가 *dx*만큼 아주 조금 변화할 때, 함수 *f(x)*의 변화량, *df(x)*
    + ![diff](https://user-images.githubusercontent.com/28593767/111458635-032e3400-875d-11eb-8157-9ec8007b9a84.png)

### 인공지능에서의 미분 활용
* AI 분야에서는 함수의 값이 어느 지점에서 최소가 되는 지를 알아내는 것이 중요하다.
* 예를 들어, 손실 함수(Loss function)는 정답과 예측값 사이의 오차를 표현 하는 함수로 이 오차를 최소로 만들기 위해 다양한 기법을 사용된다.
* 손실 함수를 미분하여 기울기의 절대값이 작아지는 방향으로 그 지점을 옮기다 보면 손실 함수의 최솟값을 구할 수 있고 이 방법을 **경사하강법**이라고 한다.


## 상미분과 편미분 ODE and PDE

![diff_eq](https://user-images.githubusercontent.com/28593767/111461025-0d056680-8760-11eb-90f7-9016e4ada2f1.png)

### 상미분 Ordinary Differential Equation
> *변수가 하나만 있는 함수*의 미분을 의미한다.
>
> 다시 말해, **구하려는 함수가 하나의 독립 변수**만을 가지고 있는 경우를 의미한다.

### 편미분 Partial Differential Equation
> 변수가 두 개 이상인 함수(다변수 함수)를 미분할 때 쓰인다.
>
> 다변수 함수를 미분할 때는 *미분할 변수에만 주목하고 다른 변수는 모두 상수로 취급*해서 계산하는데 이런 미분법을 **편미분**이라고 한다.
>
> 머신러닝의 최적화를 위해서는 미분을 사용해 기울기의 방향으로 매개변수를 이동시키는데, 이 때 매개변수가 여러 개 있을 경우에는 각각의 매개변수마다 편미분을 적용해야 한다.

![pde](https://user-images.githubusercontent.com/28593767/111461198-4211b900-8760-11eb-8ac3-0b89637d9fa8.jpg)


<!--  그래프는 나중에 설명
## 함수의 그래프 Graph of functions


## 함수의 최댓값과 최솟값 Local Extrema
-->


## 합성함수의 미분 Differential of Composite Function

### 합성 함수의 미분 공식
![comp](https://user-images.githubusercontent.com/28593767/111461453-9452da00-8760-11eb-8bde-5aadda390d59.png)

### 연쇄 법칙 Chain Rule 
> 연쇄 법칙을 사용하면 임의의 식을 여러 개 끼워 넣어서 계산할 수 있다.

![comp2](https://user-images.githubusercontent.com/28593767/111461460-95840700-8760-11eb-9fa3-a3d597047e64.png)

아래 시그모이드 함수의 미분에 연쇄 법칙의 예시가 나와있다.

### 인공지능에서의 연쇄 법칙 활용
* 신경망에서는 학습한 결과를 토대로 도출된 답이 정답 데이터에 가까워질 수 있도록 가중치(w)를 조정하는 과정을 반복한다. 
* 이 때, 실제 정답과 학습 결과 사이의 *오차 값을 가중치로 편미분한 다음, 그 값을 가중치의 조정량으로 사용*한다. 
* 이렇게 편미분을 하는 과정에서 연쇄 법칙이 사용되고 이러한 일련의 기법을 **오차 역전파법**이라 한다.


## 특수 함수의 미분 Differential of Special Function

### 시그모이드 함수 Sigmoid Function
![sig](https://user-images.githubusercontent.com/28593767/111466456-a9cb0280-8766-11eb-9d7f-d2efc6bc9f0e.png)

![sig_graph](https://user-images.githubusercontent.com/28593767/111466902-31b10c80-8767-11eb-8d72-5e13332847a3.png)

* *a = 1* 일 때의 시그모이드 함수를 표준 시그모이드 함수라고 한다.
* 시그모이드는 일종의 활성화 함수(Activation)로, *신경망의 표현력을 높이기 위해 사용*된다.
* 시그모이드의 미분값은 *0 ~ 0.25* 사이이기 때문에 가중치가 갈수록 줄어드는 문제점이 있다.
    + 즉, 신경망의 계층이 많아질수록 오차 역전파법에서 오차가 전파되기 어려워지는 상황이 발생할 수 있다.
        - 아무리 곱해봤자 값이 점점 작아지기 때문
        - 이런 현상을 **기울기 소실 문제**라고 한다.
    + *따라서, 시그모이드는 역전파에 적합하지 않다.*

### 시그모이드 함수의 미분 Differential of Sigmoid Function
> 시그모이드 함수의 미분은 연쇄 법칙(Chain Rule)을 사용하여 구할 수 있다.

<img width="1100" alt="diff_sig" src="https://user-images.githubusercontent.com/28593767/111458644-05908e00-875d-11eb-87b8-d721707b6585.png">

> 시그모이드 함수의 2계 미분은 곱의 법칙(Product Rule)을 사용하여 구할 수 있다.

![sig2](https://user-images.githubusercontent.com/28593767/111466447-a768a880-8766-11eb-8e28-46ac8adf9329.png)

### ReLU 함수 Rectified Linear Unit Function

![ReLU](https://user-images.githubusercontent.com/28593767/111467147-7472e480-8767-11eb-92bd-986b2f9e660d.png)

![ReLU_gra](https://user-images.githubusercontent.com/28593767/111467154-750b7b00-8767-11eb-96b8-5b8d6fde94d8.png)

* ReLU 함수는 단순해 보이는 비선형 함수로 *신경망의 표현력을 높이기 위해 사용*된다.
* ReLU의 미분값이 *0 ~ 1* 사이이다.
* 이러한 특징이 기울기 소실 문제를 해결하는데 도움을 준다.
    + 따라서, 최근의 신경망에서는 활성화 함수로 ReLU 함수를 많이 사용한다.

# 미분 Differential

## 극한 Limit



## 미분의 기초 Foundations of Differential



## 상미분과 편미분 ODE and PDE
* 상미분 Ordinary Differential Equation
* 변수가 하나만 있는 함수의 미분을 의미한다.
* 다시 말해, **구하려는 함수가 하나의 독립 변수**만을 가지고 있는 경우를 의미한다.

* 편미분 Partial Differential Equation



<!--  그래프는 나중에 설명
## 함수의 그래프 Graph of functions




## 함수의 최댓값과 최솟값 Local Extrema


-->


## 합성함수의 미분 Differential of Composite function

### 연쇄 법칙 Chain rule 




> 신경망에서는 학습한 결과를 토대로 도출된 답이 정답 데이터에 가까워질 수 있도록 가중치(w)를 조정하는 과정을 반복한다. 
> 
> 이 때, *실제 정답과 학습 결과 사이의 오차 값을 가중치로 편미분한 다음, 그 값을 가중치의 조정량으로 사용*한다. 
>
> 이러한 일련의 기법을 **오차 역전파법**이라 한다.



## 특수 함수의 미분
### 시그모이드 함수
* *a = 1* 일 때의 시그모이드 함수를 **표준 시그모이드 함수**라고 한다.
* 시그모이드는 일종의 활성화 함수(Activation)로, *신경망의 표현력을 높이기 위해 사용*된다.
* 시그모이드의 미분값은 *0 ~ 0.25* 사이이기 때문에 가중치가 갈수록 줄어드는 문제점이 있다. 
    + 즉, 신경망의 계층이 많아질수록 오차 역전파법에서 오차가 전파되기 어려워지는 상황이 발생할 수 있다.
        - 아무리 곱해봤자 값이 점점 작아지기 때문
        - 이런 현상을 **기울기 소실 문제**라고 한다.
    + *따라서, 시그모이드는 역전파에 적합하지 않다.*

### 시그모이드 함수의 미분
<!-- diff_sig -->



### ReLU 함수 Rectified Linear Unit function
* ReLU 함수는 단순해 보이는 비선형 함수로 *신경망의 표현력을 높이기 위해 사용*된다.
* ReLU의 미분값이 *0 ~ 1* 사이이다.
* 이러한 특징이 기울기 소실 문제를 해결하는데 도움을 준다.
    + 따라서, 최근의 신경망에서는 활성화 함수로 ReLU 함수를 많이 사용한다.








# 분류 Classification

## 이진 판단 문제 Binary Classification
* 이진 판단 문제란 예, 아니오 혹은 0, 1 같은 두 가지 값에 대해서 하나로 답하는 문제이다.
* 하지만 이진 판단 문제를 신경망으로 해결하는 것은 까다로운 부분이 존재한다.
  + 가중치와 편향을 이용하는 퍼셉트론의 선형 연산을 살펴보면 하나의 값 만을 출력한다.
  + 즉 두 가지 값으로 결과를 제한할 수 없다.
* 방법은 *선형 연산에서는 범위에 제한이 없는 실숫값을 계산하되, 이를 확률값의 성질에 맞게 즉 0~1 사이의 값을 갖도록 변환*해주는 비선형 활성화 함수, **시그모이드(sigmoid) 함수**를 사용하는 것이다.

![cross](https://user-images.githubusercontent.com/28593767/112778597-d85aae80-907f-11eb-8d5a-5e752744edc5.png)

* *신경망의 예측값에 따른 확률 분포와 실제 결괏값에 따른 확률 분포 사이의 각 확률 분포가 얼마나 다른지를 숫자 하나로 표현*해주는 **교차 엔트로피(Cross Entropy)** 라는 개념으로 풀 수 있다.


## 시그모이드 함수 Sigmoid Function
![sig](https://user-images.githubusercontent.com/28593767/112778601-da247200-907f-11eb-8f64-2dfaab391360.png)

* 시그모이드 함수는 **범위에 제한이 없는 임의의 실숫값을 입력으로 받아 이 값을 확률값의 범위에 해당하는 0과 1 사이의 값으로 다시 연산을 수행**한다.
    + 즉, 선형 연산 결과가 아무리 크다 해도 입력으로 받아 처리할 수 있다.
* 시그모이드 함수는 **입력값(x)** 을 답이 참일 **가능성(odds)** 에 대해서 **로짓(logit)** 으로 표시한 값이라고 간주한다.
    + 로짓이란 실제 표현하려는 값(odds)을 로그값으로 표현한 것으로 시그모이드 함수는 이 로짓값을 확률값으로 변환해주는 함수이다.
* 로짓값으로 표시를 하게 되면 *넓은 범위의 값을 간단하게 표현*할 수 있고 값의 변화를 *변화량보다 변화 비율관점에서 더 민감하게 포착*할 수 있다.

### 시그모이드 함수의 일반화 Generalization of Sigmoid Function
* 참일 가능성과 거짓일 가능성의 로짓값이 각각 x와 0이므로 거짓인 경우의 실제 확률은 *P_F = α* 이고 참인 경우의 실제 확률은 *P_T = αe^x* 가 된다.

<img width="495" alt="sig_cal" src="https://user-images.githubusercontent.com/28593767/112779559-f6291300-9081-11eb-9c9e-2848441989c5.png">


## 정보 엔트로피 Information Entropy
* *확률 분포의 무질서도나 불확실성 혹은 정보 표현의 부담 정도*를 나타내는 개념을 **정보 엔트로피 혹은 섀넌 엔트로피(Shannon Entropy)** 라고 한다.
* 정보 이론은 *신호에 존재하는 정보의 양을 측정하는 이론*으로 정보의 양은 간단히 말해 놀람의 정도라고 할 수 있다.
* 예를 들어 전구가 표현할 수 있는 단위 정보수는 2개이니 전구가 1개면 표현 범위는 2, 2개면 4개, 3개면 8개라 할 수 있다.

<img width="1159" alt="info" src="https://user-images.githubusercontent.com/28593767/112780934-d515f180-9084-11eb-8a3a-d0c816f60feb.png">

* 이러한 정보량의 개념은 각 경우에 대한 확률이 균일하지 않은 확률포 분포에도 확장하여 적용할 수 있다.
* **정보량의 평균(기댓값)을 정보 엔트로피**라고 하며 보통 *H*라고 표현한다.

![log](https://user-images.githubusercontent.com/28593767/112787103-c5050e80-9092-11eb-9411-9dc396d1740b.png)
<img width="292" alt="h" src="https://user-images.githubusercontent.com/28593767/112787107-c6363b80-9092-11eb-87af-1010a7bbb06e.png">

* 로그의 밑이 2인 경우 단위를 **섀넌(shannon)** 또는 **비트(bit)** 라고 한다.
* 자연상수를 밑으로 할 경우 **내트(nat)** 라고 부르고 머신러닝에서는 대개 밑을 자연상수로 사용한다.


## 교차 엔트로피 Cross Entropy
<img width="334" alt="cross_ent" src="https://user-images.githubusercontent.com/28593767/112788131-1e6e3d00-9095-11eb-9b7a-ca7a0992a1ce.png">


* 교차 엔트로피는 두 가지 확률 분포가 얼마나 비슷한 지를 숫자 하나로 나타내는 개념이다.
* 정보량을 제공하는 확률 분포와 가중평균 계산에 사용되는 확률 분포를 서로 다르게 설정하여 정보량의 기댓값을 구하는 방식으로 정의된다.
* 다시 말해, 교차 엔트로피는 틀릴 수 있는 정보를 가지고 구한 엔트로피, 즉 정보량이라고 할 수 있다.
* 딥러닝에서 정보량은 신경망을 통해서 예측한 값, 즉 틀릴 수 있는 정보에 대한 기댓값이다.

### 교차 엔트로피의 특징
<img width="322" alt="cross" src="https://user-images.githubusercontent.com/28593767/112787877-8b350780-9094-11eb-9315-f0aa601eb813.png">
<img width="426" alt="cross2" src="https://user-images.githubusercontent.com/28593767/112787880-8cfecb00-9094-11eb-855a-e9fcc206b6cf.png">

* 딥러닝의 예측이 완전히 빗나가게 되면 교차 엔트로피값은 무한대이지만 어느정도 학습이 된 경우라면 교차 엔트로피의 값은 엔트로피 값으로 수렴한다.
* 학습이 완벽하게 진행된 경우라면 교차 엔트로피와 엔트로피는 같은 값을 갖게 된다.
* 따라서, **교차 엔트로피는 두 확률분포가 서로 얼마나 다른지를 나타내주는 정량적 지표 역할을 수행**한다.

<img width="1229" alt="ex" src="https://user-images.githubusercontent.com/28593767/112788135-20380080-9095-11eb-8867-14b7fb8029ce.png">

* 경기 결과에 관한 엔트로피는 1.006, 각 교차 엔트로피는 1.032, 1.053으로 *엔트로피값에 더 수렴한 이즈리얼이 더 정확하게 예측을 수행*했다.

### 딥러닝에서의 교차 엔트로피
* 딥러닝 모델의 추정 확률 분포 Q, 그리고 미지의 확률 분포 P에 대해서 교차 엔트로피를 계산하고 이 교차 엔트로피가 낮아지는 쪽으로 모델의 추정 확률 분포 Q를 꾸준히 개선함으로 확률 분포 Q를 확률 분포 P에 가깝게 접근시켜 갈 수 있다.
* 이것이 **이진 판단에서의 신경망을 학습시킬 수 있는 원리**가 된다.


## 시그모이드 함수와 교차 엔트로피의 편미분
* 이진 판단 문제에 대한 정답으로 z가 주어질 때 데이터의 결과가 참일 확률은 *P_T = z*, 거짓일 확률은 *P_F = 1 - z* 라고 표현할 수 있다.
* 어떠한 데이터에 대해 신경망 회로의 출력 t가 로짓값 x로 계산되었다고 할 때 신경망 예측에 대한 확률값은 *Q_T = σ(x)* 그리고 *Q_F = 1 - σ(x)*로 표현할 수 있다.
* 이 때 교차 엔트로피의 정의식 *H(P, Q)* 에 위 확률값들을 대입하면 H는 다음과 같다.
    + <img width="673" alt="cross" src="https://user-images.githubusercontent.com/28593767/112924916-f392f000-914b-11eb-9d36-e938211b0e17.png">
* 정리한 교차 엔트로피에 시그모이드 함수 *σ(x) = 1/(1+e^-x)* 를 대입하면 다음과 같다.
    + <img width="584" alt="cross2" src="https://user-images.githubusercontent.com/28593767/112924921-f4c41d00-914b-11eb-9d5e-cb55882915fb.png">
* 일반적으로 *이진 판단 문제의 정답값은 0 혹은 1*이므로 실제 정답 z에 0과 1을 대입하면 다음과 같다.
    + <img width="565" alt="cross3" src="https://user-images.githubusercontent.com/28593767/112924931-f68de080-914b-11eb-823c-9380c6b5d78f.png">
* 마지막으로 이진 분류 신경망의 학습을 위해 시그모이드 함수에 대한 교차 엔트로피의 편미분을 구하면 다음과 같다 (z는 편미분이기에 상수로 취급).
    + <img width="574" alt="cross4" src="https://user-images.githubusercontent.com/28593767/112924934-f7267700-914b-11eb-99d9-ae1687d8ae27.png">


### 오버플로우 Overflow
```python
import numpy as np

def sigmoid_A(x):
    y = 1.0 / 1.0 + (np.exp(-x)) 
    print(y)

x = -1000
sigmoid_A(x)
>> inf
>> /usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:4: RuntimeWarning: overflow encountered in exp after removing the cwd from sys.path.
```

* 파이썬을 활용해 시그모이드 함수를 돌리다보면 종종 **오버플로우 문제**가 발생한다.
* 입력값 x에 큰 음수가 들어오는 경우 경고가 발생하고 학습이 종료될 수 도 있다.
    + 반면 큰 음수값이 아닌 큰 양수값이 들어오는 경우에는 결괏값이 정상적으로 출력된다.
* 이러한 오버플로우 문제를 방지하기 위해서는 시그모이드 함수의 *분자와 분모에 e^x를 곱해 식을 재정의*하는 것으로 해결할 수 있다.
    + <img width="290" alt="over_sig" src="https://user-images.githubusercontent.com/28593767/112924991-12918200-914c-11eb-92c5-42cd9c2f4bd8.png">
* 시그모이드 함수의 교차 엔트로피 함수 역시 입력값에 큰 음수가 들어오는 경우 inf 출력 및 오버플로우 문제가 발생한다.
    + 마찬가지로 식을 정리해서 해결할 수 있다.
    + <img width="1129" alt="over_cross" src="https://user-images.githubusercontent.com/28593767/112924995-13c2af00-914c-11eb-8ce7-eb43833644c3.png">

* 입력값을 양수식과 음수식에 따라 나눠 대입하는 것은 처리 과정이 너무 복잡하기 때문에 양수식과 음수식을 합쳐 새로운 식을 만들면 다음과 같다.
    + <img width="637" alt="new_eq" src="https://user-images.githubusercontent.com/28593767/112925001-158c7280-914c-11eb-872a-05087e3b3a27.png">
    + 새로운 수식은 음수값과 양수값 모두 대응이 가능하고, 이 변형된 수식과 기존 수식에 대하여 같은 값으로 음수, 양수, 0을 대입하면 모두 같은 값이 나온다.
        - <img width="918" alt="eq_ex" src="https://user-images.githubusercontent.com/28593767/112925020-2341f800-914c-11eb-8dde-d1f68bb54e83.png">



# 순환 신경망 Recurrent Neural Network


## 자연어 처리에서의 순환 신경망 RNN in NLP
* 챗봇 엔진에서 **개체명 인식(Named Entity Recognition)** 을 위해서는 **양방향 LSTM(Bi-LSTM) 모델**을 사용한다.
* LSTM은 순환 신경망 모델의 일종으로 시퀀스 또는 시계열 데이터의 패턴을 인식하는 분야에서 많이 사용한다.
    + 연속적인 데이터의 패턴을 이용해 결과를 예측하므로 주로 주가 예측이나 신호 분석 및 번역분야에서 좋은 성능을 보인다.
    + LSTM은 RNN 모델에서 파생되어 만들어졌다.

## 순환 신경망 Recurrent Neural Network
<img width="927" alt="rnn" src="https://user-images.githubusercontent.com/28593767/115508853-bcca7880-a2b8-11eb-961f-754ec4cbfd5a.png">

* RNN(Recurrent Neural Network) 은 순환 신경망이라 불리고 은닉층 노드의 출력값을 출력층과 그 다음 시점의 은닉층 노드의 입력으로 전달해 순환하는 특징을 지니고 있다.
* 일반적으로 RNN에서는 (a) 형태를 세워놓은 (b) 표현법을 많이 사용한다. 
* RNN 모델에서 x는 입력 벡터, y는 출력 벡터, t는 현재 시점을 의미한다. 
    + 즉, x_t는 현재 시점의 입력 벡터, y_t는 현재 시점의 출력 벡터를 의미한다.
* RNN에서 은닉층 노드는 *이전 시점(t − 1)의 상태값을 저장하는 메모리 역할*을 수행하기 때문에 **셀(cell) 또는 메모리 셀**이라고 한다. 
* *은닉층의 메모리 셀의 출력 벡터는 출력층과 다음 시점(t + 1)의 메모리 셀에 전달*되는데 이를 **은닉 상태(Hidden State)** 라고 한다. 
    + 또한 h_t는 현재 시점의 은닉 상태, h_(t + 1)은 다음 시점의 은닉 상태를 의미한다.

![rnn2](https://user-images.githubusercontent.com/28593767/115508866-be943c00-a2b8-11eb-8531-d32637da1036.png)

* RNN 모델을 *시점의 흐름에 따라 표현한 그림으로 현재 시점의 메모리 셀은 이전 시점의 은닉 상태값에 영향을 받고 있으며 완전 연결 계층 구조를 가지고 있다*는 점을 알 수 있다.
* RNN 모델은 어떤 문제를 해결하느냐에 따라 입력과 출력의 길이를 조절할 수 있다.

#### Many-to-One RNN
![m-o](https://user-images.githubusercontent.com/28593767/115508868-bf2cd280-a2b8-11eb-8c63-7ecbde19e7dd.png)

* many-to-one은 여러 개를 입력받아 하나를 출력하는 모델을 의미한다.
* 다이어그램은 09:00 부터 09:59 분 까지 온도 데이터를 입력받아 현재까지의 온도 흐름이 정상인지 비정상인지 판단한다.

#### One-to-Many RNN
![o-m](https://user-images.githubusercontent.com/28593767/115508870-c05dff80-a2b8-11eb-9bcd-d030c43b09a1.png)

* one-to-many는 하나를 입력받아 여러 개를 출력하는 모델을 의미한다.
* 다이어그램은 한 장의 이미지를 입력받아 이미지를 설명하는 텍스트를 출력하는 모델로 사용할 수 있다.

#### Many-to-Many RNN
![m-m](https://user-images.githubusercontent.com/28593767/115508873-c05dff80-a2b8-11eb-848d-0ad92c11353d.png)

* many-to-many는 여러 개를 입력으로 받아 여러 개를 출력하는 모델을 의미한다.
* 개체명 인식기에서도 사용하는 모델로 **단어 시퀀스를 입력으로 받아 각 시퀀스가 의미하는 개체명을 출력하는 구조**이다.
* 한국어를 입력으로 받아 영어로 출력하는 번역기 모델로도 사용 가능하다.


## RNN의 원리
![rnn3](https://user-images.githubusercontent.com/28593767/115508875-c0f69600-a2b8-11eb-9454-f5e47e3ca70a.png)

* RNN은 모든 시점에서 동일한 가중치와 편향값을 사용한다.
* 현재 시점을 t로 정의할 때 각 변수는 다음과 같다.
    + x_t는 현재 시점의 입력 벡터
    + y_t는 현재 시점의 출력 벡터
    + h_t는 현재 시점의 은닉 상태 벡터값
* RNN의 각 노드에 연결되어 있는 가중치는 다음과 같다.
    + w_x는 입력 x_t에 대한 가중치
    + w_h는 이전 시점의 은닉 상태값인 h_(t - 1)에 대한 가중치
    + w_y는 현재 시점의 은닉 상태값인 h_t에 대한 가중치
* ![rnn4](https://user-images.githubusercontent.com/28593767/115508877-c18f2c80-a2b8-11eb-9333-5200e20ffd39.png)
* 현재 시점의 은닉 상탯값 h_t 는 현재 입력값 x_t와 이전 시점의 은닉 상태값 h_(t - 1)으로 계산하고 활성화 함수로 하이퍼볼릭 탄젠트(tanh)를 사용한다.
* *이전 시점의 은닉 상탯값이 현재 시점의 은닉 상태에 계속해서 영향을 주기 때문에 시퀀스 데이터의 특징을 잘 파악*할 수 있다.
* 출력층 y_t는 메모리 셀에서 계산된 은닉 상태값 h_t와 가중치 w_y를 곱한 값으로 계산한다.

### SimpleRNN
![rnn5](https://user-images.githubusercontent.com/28593767/115508869-bfc56900-a2b8-11eb-9413-e4eb49ff038a.png)

* SimpleRNN 레이어는 가장 간단한 형태의 RNN 레이어이다.
* 순환 신경망은 변화하는 입력을 받기 때문에 각 단계에서 입력이 변할 때의 계산의 흐름을 보여준다.


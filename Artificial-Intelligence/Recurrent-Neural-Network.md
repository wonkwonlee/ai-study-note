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
* 현재 시점의 은닉 상탯값 h_t 는 현재 입력값 x_t와 이전 시점의 은닉 상태값 h_(t - 1)으로 계산하고 활성화 함수로 **하이퍼볼릭 탄젠트(tanh)** 를 사용한다.
* *이전 시점의 은닉 상탯값이 현재 시점의 은닉 상태에 계속해서 영향을 주기 때문에 시퀀스 데이터의 특징을 잘 파악*할 수 있다.
* 출력층 y_t는 메모리 셀에서 계산된 은닉 상태값 h_t와 가중치 w_y를 곱한 값으로 계산한다.

### SimpleRNN
![rnn5](https://user-images.githubusercontent.com/28593767/115508869-bfc56900-a2b8-11eb-9413-e4eb49ff038a.png)

* SimpleRNN 레이어는 가장 간단한 형태의 RNN 레이어이다.
* 순환 신경망은 변화하는 입력을 받기 때문에 각 단계에서 입력이 변할 때의 계산의 흐름을 보여준다.
* SimpleRNN 레이어에는 *입력 데이터가 길어질수록, 즉 데이터의 타임스텝이 커질 수록 학습 능력이 떨어진다*는 **장기 의존성(Long-Term Dependency)** 문제가 있다.
    + 즉, 입력 데이터와 출력 사이의 길이가 멀어질수록 연관관계가 적어진다.
* SimpleRNN 레이어는 같은 가중치 W를 반복적으로 사용해서 출력값을 계산하는데 같은 값을 계속 곱하게 되면 값이 엄청나게 커지는 **그레이언트 폭발(Gradient Exploding)** 이나 **그레디언트 소실(Gradient Vanishing)** 문제가 발생할 수 있다.
    + 과거의 정보를 통해 현재의 답을 구하는 RNN이지만 과거 시점이 현재에서 너무 멀어지면 문제를 풀기 어렵다는 말과 같다.
    + 이러한 RNN의 장기 의존성 문제를 해결하기 위해 LSTM이 제안되었다.
* 또한 활성화 함수를 tanh 대신 ReLU를 사용하면 학습 자체가 불안정해진다.

<img width="493" alt="rnn_1" src="https://user-images.githubusercontent.com/28593767/115660170-9703a900-a376-11eb-939e-7f7d6a94cf06.png">

<img width="337" alt="rnn_2" src="https://user-images.githubusercontent.com/28593767/115660168-9539e580-a376-11eb-8f32-0d418e38dfeb.png">


## 장단기 메모리 Long Short Term Memory
<img width="1118" alt="lstm" src="https://user-images.githubusercontent.com/28593767/115660171-979c3f80-a376-11eb-8920-ae071d4f2303.png">

* LSTM은 RNN에 비해 복잡한 구조를 가지고 있는데 특히 출력 외에 LSTM 셀 사이에서만 공유되는 **셀 상태(Cell State)** 를 가지고 있다는 특징이 있다.
    + c_(t − 1)과 c_t가 셀 상태를 나타내는 기호이다. 
* SimpleRNN 셀에서 타임스텝의 방향으로 h_t만 전달되지만 LSTM 셀에서는 셀 상태인 c_t가 평행선을 그리며 함께 전달된다. 
* 즉, *타임스텝을 가로지르며 셀 상태가 보존되기 때문에 장기 의존성 문제를 해결*할 수 있다. 
    + 과거의 정보 중 sigmoid 함수를 통해 몇 퍼센트만 기억시킨다.
* 결과적으로 LSTM은 **잊을건 잊고 기억할 것은 기억하며 성능을 높이는 모델**이라고 할 수 있다.

<img width="1256" alt="lstm2" src="https://user-images.githubusercontent.com/28593767/115660174-98cd6c80-a376-11eb-9ebd-00041a66898e.png">

* U와 W는 입력과 출력에 곱해지는 가중치이다.
* *수식 1, 2, 3*은 각각 타임스텝 t에서의 Input, Forget, Output 게이트를 통과한 출력을 의미한다.
* *수식 4*는 x_t와 h_(t - 1)을 가중치 U와 W에 곱한 뒤 tanh 활성화 함수를 취한 값으로 셀 상태인 c_t가 되기 전의 출력값이다.
* *수식 5, 6*은 셀 상태와 LSTM의 출력을 계산하는 가장 중요한 부분이다.
    + 셀 상태는 Forget 게이트의 출력에 의해 이전 타임스템의 셀 상태를 얼마만큼 남길지 결정되고 새로 입력된 Input 게이트의 출력과 *수식 4*를 곱한 값을 더해서 다음 타임스텝의 셀 상태를 만든다.
* LSTM 참고 링크: [LSTM 이해하기](https://dgkim5360.tistory.com/entry/understanding-long-short-term-memory-lstm-kr)
* **Gate Recurrent Units(GRU)** 은 게이트 메커니즘이 적용된 RNN 프레임워크로 LSTM의 영감을 받아 고안된 더 간략한 구조로 만들어진 모델이다.


## 양방향 LSTM Bi-LSTM
* RNN이나 LSTM은 일반 신경망과 다르게 *시퀀스 또는 시계열 데이터 처리에 특화되어 은닉층에서 과거의 정보를 기억*할 수 있지만 순환 신경망의 구조적 특성상 *데이터가 입력 순으로 처리되기 때문에 이전 시점의 정보만 활용할 수 밖에 없다는 단점*이 존재한다.
    + 즉, 문장이 길어질수록 성능이 저하될 수 밖에 없다.

![ex](https://user-images.githubusercontent.com/28593767/115667678-14341b80-a381-11eb-858b-02a0776d4500.png)

* RNN이나 LSTM에서는 *ios와 앱*이라는 단어만 가지고 빈칸에 들어갈 *개발*이라는 단어를 유추하기엔 정보가 매우 부족하다.
* 예문에서는 문장의 앞부분보다 뒷 부분에 중요한 정보가 존재한다.
* 따라서 *자연어 처리에 있어 입력 데이터의 정방향 처리만큼 역방향 처리도 중요*하다고 할 수 있다.

![bi-lstm](https://user-images.githubusercontent.com/28593767/115667683-15654880-a381-11eb-9192-6a5bcefed9dc.png)

* **양방향 LSTM(Bidirectional LSTM)** 은 *기존 LSTM 계층에 역방향으로 처리하는 LSTM 계층을 하나 더 추가해 양방향에서 문장의 패턴을 분석할 수 있도록 구성*되어 있다. 
    + 입력 문장을 양방향에서 처리하므로 *시퀀스 길이가 길어진다 하더라도 정보손실없이 처리가 가능*하다.
* 정방향 LSTM은 기존과 동일하게 입력 문장을 왼쪽에서 오른쪽으로 처리하며 역방향 LSTM은 입력 문장의 단어 순서를 반대로 처리한다.


# 자연어 처리 Natural Language Processing

## 자연어 처리 NLP
* 인간이 일상에서 사용하는 언어를 자연어라고 한다.
* 컴퓨터 분야에서는 자연어 의미를 분석해 컴퓨터가 처리할 수 있도록 하는 일을 **자연어 처리(Natural Language Processing)** 혹은 줄여서 **NLP**라고 한다.
* 일반적으로 문장을 일정한 의미가 있는 **토큰(Token)** 이라는 가장 작은 단어들로 나눈 뒤 나눠진 단어들을 이용해 의미를 분석한다.
* 토큰의 단위는 **토크나이징(Tokenizing)** 방법에 따라 달라질 수 있지만 일반적으로 *일정한 의미가 있는 가장 작은 정보 단위로 결정*된다.
* *토크나이징은 문장 형태의 데이터를 처리하기 위해 제일 처음 수행해야 하는 기본적인 작업이며 주로 텍스트 전처리 과정에서 사용*된다.

### KoNLPy
* [**KoNLPy**](https://konlpy-ko.readthedocs.io/ko/v0.4.3/) 는 한국어 토크나이징을 지원하는 파이썬 라이브러리로 한국어 자연어 처리에 많이 사용된다.
* 한국어 문장을 분석하려면 토크나이징 작업을 제일 먼저 수행해야 하는데, 이때 토큰 단위를 어떻게 정의하느냐에 따라 자연어 처리 성능에 영향을 미친다.
    + 일정한 의미가 있는 가장 작은 말의 단위, 즉 의미가 더 이상 쪼개지지 않는 **형태소(Morpheme)** 를 토큰 단위로 사용한다.
* 영어의 경우 단어의 변화가 크지 않고, 띄어쓰기로 단어를 구분하기 때문에 공백을 기준으로 토크나이징을 수행해도 큰 문제 없지만 *한국어는 명사와 조사를 띄어 쓰지 않고, 용언에 따라 여러 가지 어미가 붙기 때문에 띄어쓰기만으로는 토크나이징할 수 없다*.
* 따라서 형태소 분석기를 이용하여 문장에서 형태소를 추출하면서 형태소의 뜻과 문맥을 고려해 품사 태깅을 해줘야 한다.


### Kkma
* [**Kkma**](http://kkma.snu.ac.kr/documents/?doc=postag) 는 서울대학교 IDS(Intelligent Data Systems) 연구실에서 자연어 처리를 위해 개발한 한국형 형태소 분석기로 *꼬꼬마*라고 발음한다.
* Kkma는 다음 4가지 함수를 제공한다.
<img width="1292" alt="kkma" src="https://user-images.githubusercontent.com/28593767/115185952-cf5b7b00-a11b-11eb-8900-6b10475a3618.png">


### Komoran 
* [**Komoran(Korean Morphological ANalyzer)**](https://www.shineware.co.kr/products/komoran/#demo?utm_source=komoran-kr&utm_medium=Referral&utm_campaign=github-demo) 은 Shinware에서 개발한 자바 기반 한국어 형태소 분석기로 *코모란*이라고 발음한다.
* Komoran은 다음 3가지 함수를 제공한다.
![komoran](https://user-images.githubusercontent.com/28593767/115186644-0c743d00-a11d-11eb-9d0e-9e10321a5402.png)







# auto.py

# getcwd() : Get current working directory. 현재 디렉토리 경로를 알려준다
# 현재 경로에 my_email.py를 저장하면 import 할 수 있다

import os 
os.getcwd()     

# 같은 디렉토리에 있는 my_email 코드에서 Email 클래스를 import 한다
from my_email import Email

e = Email()
e.sender = "likelion_k@gmail.com"
recv_list = ['test1@gmail.com', 'test2@gmail.com', 'test3@gmail.com']

# recv_list의 각 이메일마다 send_mail가 실행됨
for recv in recv_list:
    e.send_mail(recv, "Welcome!", "This is contents")
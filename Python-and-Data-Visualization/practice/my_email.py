# my_email.py

class Email:
    sender = ""

    def send_mail(self, recv, subject, contents):
        print("From:\t" + self.sender)
        print("To:\t" + recv)
        print("Subject:\t" + subject)
        print("Contents")
        print(contents)
        print("-" * 20)  # Python에서는 String값도 곱해서 출력이 가능

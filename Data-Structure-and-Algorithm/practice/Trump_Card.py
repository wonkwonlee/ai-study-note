"""
트럼프 카드 52장을 1 ~ 52의 정수로 표현하는 프로그램
1 ~ 13: 스페이드 A ~ K로 저장
14 ~ 26: 하트 A ~ K로 저장
27 ~ 39: 다이아몬드 A ~ K로 저장
40 ~ 52: 클로버 A ~ K로 저장

Use for-loop to print the output
"""


class Trump:
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

    def printTrump(self, suit, num):
        print(self.suit + " " + self.num)


# Initialize a Trump card
trump_card = Trump("", "")

for card in range(52):
    # Find the number
    if (card + 1) % 13 == 11:  # Jack
        trump_card.num = "J"
    elif (card + 1) % 13 == 12:  # Queen
        trump_card.num = "Q"
    elif (card + 1) % 13 == 0:  # King
        trump_card.num = "K"
    elif (card + 1) % 13 == 1:  # Ace
        trump_card.num = "A"
    else:
        trump_card.num = str((card + 1) % 13)  # int to string

    # Find the suit
    if card // 13 == 0:  # Spade
        trump_card.suit = "Spade"
    elif card // 13 == 1:  # Heart
        trump_card.suit = "Heart"
    elif card // 13 == 2:  # Diamond
        trump_card.suit = "Diamond"
    elif card // 13 == 3:  # Clover
        trump_card.suit = "Clover"

    trump_card.printTrump(trump_card.suit, trump_card.num)

from typing import Tuple


T = int(input())

#1부터 13의 숫자가 카드에 적혀 있음
#카드무늬는 (S,D,H,C)
for test_case in range(1,T+1):
    card = input()
    cards = [card[i:i+3] for i in range(0, len(card), 3)]
    flag = False
    suits = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    
    used_cards = set()
    
    for c in cards:
        suit = c[0]
        num = int(c[1:])

        if c in used_cards:
            flag = True
            break
        used_cards.add(c)

        if suit not in suits:
            flag = True
            break
        suits[suit] -= 1
    
    if flag:
        print(f'#{test_case} ERROR')
    else:
        print(f'#{test_case} {suits["S"]} {suits["D"]} {suits["H"]} {suits["C"]}')


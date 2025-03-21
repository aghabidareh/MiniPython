import random

squares = [
    "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
    "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
    "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
    "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
]

cc_squares = [2, 17, 33]
ch_squares = [7, 22, 36]
g2j = 30
jail = 10

cc_cards = ["GO", "JAIL"] + [None] * 14
ch_cards = ["GO", "JAIL", "C1", "E3", "H2", "R1", "next R", "next R", "next U", "back 3"] + [None] * 6

random.shuffle(cc_cards)
random.shuffle(ch_cards)

position = 0
visits = [0] * 40
visits[0] = 1

num_simulations = 1000000
for _ in range(num_simulations):
    dice1 = random.randint(1, 4)
    dice2 = random.randint(1, 4)
    total = dice1 + dice2

    position = (position + total) % 40

    if position == g2j:
        position = jail
    elif position in cc_squares:
        card = cc_cards.pop(0)
        cc_cards.append(card)
        if card == "GO":
            position = 0
        elif card == "JAIL":
            position = jail
    elif position in ch_squares:
        card = ch_cards.pop(0)
        ch_cards.append(card)
        if card == "GO":
            position = 0
        elif card == "JAIL":
            position = jail
        elif card == "C1":
            position = 11
        elif card == "E3":
            position = 24
        elif card == "H2":
            position = 39
        elif card == "R1":
            position = 5
        elif card == "next R":
            if position < 5 or position >= 35:
                position = 5
            elif position < 15:
                position = 15
            elif position < 25:
                position = 25
            elif position < 35:
                position = 35
        elif card == "next U":
            if position < 12 or position >= 28:
                position = 12
            else:
                position = 28
        elif card == "back 3":
            position = (position - 3) % 40

    visits[position] += 1

probabilities = [visits[i] / num_simulations for i in range(40)]

sorted_indices = sorted(range(40), key=lambda i: -probabilities[i])
top_three = sorted_indices[:3]

modal_string = ''.join(f"{i:02d}" for i in top_three)

print(f"The six-digit modal string is: {modal_string}")
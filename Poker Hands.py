import requests

# Define card values and ranks
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
               'A': 14}
ranks = ['High Card', 'One Pair', 'Two Pairs', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind',
         'Straight Flush', 'Royal Flush']


def evaluate_hand(hand):
    values = sorted([card_values[card[0]] for card in hand], reverse=True)
    suits = [card[1] for card in hand]
    is_flush = len(set(suits)) == 1
    is_straight = len(set(values)) == 5 and (max(values) - min(values) == 4)

    if is_straight and is_flush:
        if max(values) == 14:
            return (ranks.index('Royal Flush'), values)
        else:
            return (ranks.index('Straight Flush'), values)
    elif is_flush:
        return (ranks.index('Flush'), values)
    elif is_straight:
        return (ranks.index('Straight'), values)

    value_counts = {v: values.count(v) for v in set(values)}
    if 4 in value_counts.values():
        return (ranks.index('Four of a Kind'), values)
    elif 3 in value_counts.values() and 2 in value_counts.values():
        return (ranks.index('Full House'), values)
    elif 3 in value_counts.values():
        return (ranks.index('Three of a Kind'), values)
    elif list(value_counts.values()).count(2) == 2:
        return (ranks.index('Two Pairs'), values)
    elif 2 in value_counts.values():
        return (ranks.index('One Pair'), values)
    else:
        return (ranks.index('High Card'), values)


def compare_hands(hand1, hand2):
    rank1, values1 = evaluate_hand(hand1)
    rank2, values2 = evaluate_hand(hand2)
    if rank1 > rank2:
        return 1
    elif rank1 < rank2:
        return 2
    else:
        for v1, v2 in zip(values1, values2):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return 2
        return 0


def count_player1_wins(file_url):
    response = requests.get(file_url)
    lines = response.text.strip().split('\n')
    player1_wins = 0
    for line in lines:
        cards = line.split()
        hand1 = cards[:5]
        hand2 = cards[5:]
        if compare_hands(hand1, hand2) == 1:
            player1_wins += 1
    return player1_wins


# URL to the poker hands file
file_url = "https://projecteuler.net/project/resources/p054_poker.txt"

# Count the number of hands Player1 wins
result = count_player1_wins(file_url)

print(f"Player 1 wins {result} hands.")
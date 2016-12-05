'''
Poker Hands
'''

card_values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def vals(cards):
    global card_values
    return [int(c) if c not in card_values.keys() else card_values[c]
            for c in cards]


def rank(cards, suits):
    cfreq = {}
    for c in set(cards):
        cfreq.setdefault(cards.count(c), []).append(c)
    rank = (0, 0)
    if sum(cards) == 60 and len(set(suits)) == 1:
        rank = (9, card_values['A'])  # royal flush
    elif (max(cards) - min(cards) == 4 and len(set(cards)) == 5 and
          len(set(suits)) == 1):
        rank = (8, max(cards))  # flush
    elif 4 in cfreq.keys():
        rank = (7, cfreq[4][0])  # four of a kind
    elif cfreq.keys() == {2, 3}:
        rank = (6, cfreq[3][0])  # full house
    elif len(set(suits)) == 1:
        rank = (5, max(cards))  # flush
    elif max(cards) - min(cards) == 4 and len(set(cards)) == 5:
        rank = (4, max(cards))  # straight
    elif 3 in cfreq.keys():
        rank = (3, cfreq[3][0])  # three of a kind
    elif 2 in cfreq.keys() and len(cfreq[2]) > 1:
        rank = (2, cfreq[2][1])  # two pairs
    elif 2 in cfreq.keys():
        rank = (1, cfreq[2][0])  # one pair
    else:
        rank = (0, max(cards))
    return rank


def hand_winner(p1_hand, p2_hand):
    p1_cards, p1_suits = zip(*[(c[0], c[1]) for c in p1_hand])
    p2_cards, p2_suits = zip(*[(c[0], c[1]) for c in p2_hand])
    p1_rank = rank(vals(p1_cards), p1_suits)
    p2_rank = rank(vals(p2_cards), p2_suits)
    winner = 0
    if p1_rank[0] > p2_rank[0]:
        winner = 1
    elif p1_rank[0] == p2_rank[0]:
        if p1_rank[1] > p2_rank[1]:
            winner = 1
        elif p1_rank[1] < p2_rank[1]:
            winner = 2
        else:
            winner = 1 if max(vals(p1_cards)) > max(vals(p2_cards)) else 2
    else:
        winner = 2
    return winner


if __name__ == '__main__':
    hands = open('p054_poker.txt').read().split('\n')[:-1]
    hands = [h.split(' ') for h in hands]
    hand_winners = [hand_winner(h[:5], h[5:]) for h in hands]
    print("Player 1 won a total of {} hands, player 2 won {} hands.".format(
            hand_winners.count(1), hand_winners.count(2)))

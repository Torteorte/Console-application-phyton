from random import randrange

# players = int(input('Enter the number of players from 1 to 6: '))
players = 6

card_suit = ['♠', '♣', '♦', '♥']
game_trump = card_suit[int(randrange(0, 4))]
cards_names = ['6', '7', '8', '9', '10', 'B', 'Q', 'K', 'A']
list_of_cards = []
for name in cards_names:
    for suit in card_suit:
        list_of_cards.append({suit: name})

# players = 6
all_players_cards = {}

for i in range(1, players + 1):
    player_cards = []
    for j in range(0, 6):
        length = len(list_of_cards)
        number_card = randrange(0, length)
        player_cards.append(list_of_cards[number_card])
        list_of_cards.remove(list_of_cards[number_card])
    all_players_cards['player' + str(i)] = player_cards


def card_to_number(cards_list, card_trump):
    for card_name in range(0, 6):
        if cards_list[card_name] == '1':
            nominal = 10
        elif cards_list[card_name] == 'B':
            nominal = 11
        elif cards_list[card_name] == 'Q':
            nominal = 12
        elif cards_list[card_name] == 'K':
            nominal = 13
        elif cards_list[card_name] == 'A':
            nominal = 14
        else:
            nominal = int(cards_list[card_name])
        if card_trump == game_trump:
            return nominal + 9
        else:
            return nominal


def sum_of_cards(cards):
    summa = 0
    for card_nominal in range(0, 6):
        summa += cards[card_nominal]
    return summa


players_points = {}

for player in all_players_cards:
    points_of_cards = []
    for number_of_card in range(0, 6):
        for card_trump in all_players_cards[player][number_of_card]:
            card = all_players_cards[player][number_of_card][card_trump]
            points_of_cards.append(card_to_number(card, card_trump))
    players_points[player] = sum_of_cards(points_of_cards)

# for key in all_players_cards:
#     print(key + ':', all_players_cards[key])

print('Trump: ', game_trump)

sorted_values = sorted(players_points.values(), reverse=True)  # Sort the values
sorted_players_points = {}

for i in sorted_values:
    for k in players_points.keys():
        if players_points[k] == i:
            sorted_players_points[k] = players_points[k]
            break

print(sorted_players_points)

for key in sorted_players_points:
    print(key + ':', all_players_cards[key])

print('Trump: ', game_trump)

from random import randrange


def game():

    players = int(input('Выберите колличество игроков от 1 до 6: '))
    if players < 1:
        players = int(input('Слишком мало игроков. \n'
                            'Выберите колличество игроков от 1 до 6: '))
    elif players > 6:
        players = int(input('Всем не хватит карт. \n'
                            'Выберите колличество игроков от 1 до 6: '))

    card_suit = ['♠', '♣', '♦', '♥']
    game_trump = card_suit[int(randrange(0, 4))]
    cards_names = ['6', '7', '8', '9', '10', 'B', 'Q', 'K', 'A']
    list_of_cards = []
    for name in cards_names:
        for suit in card_suit:
            list_of_cards.append({suit: name})

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

    print('Козырь: ', game_trump)

    sorted_values = sorted(players_points.values(), reverse=True)  # Sort the values
    sorted_players_points = {}

    for i in sorted_values:
        for k in players_points.keys():
            if players_points[k] == i:
                sorted_players_points[k] = players_points[k]
                break

    for key in sorted_players_points:
        print(key + ':', all_players_cards[key])

    def menu_call():
        menu = input('Выберите один из следующих пунктов: \n '
                     '1. Просмотреть карты игроков \n '
                     '2. Просмотреть очки игроков \n '
                     '3. Начать новую игру \n '
                     '4. Закончить игру \n'
                     '')
        if menu == '1':
            for key in all_players_cards:
                print(key + ':', all_players_cards[key])
            menu_call()
        elif menu == '2':
            print(sorted_players_points)
            menu_call()
        elif menu == '3':
            game()
        elif menu == '4':
            print('Спасибо за игру')
        else:
            print('Шутки со мной шутишь?')
            menu_call()

    menu_call()


print(game())

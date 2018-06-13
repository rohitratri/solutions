import random

cards = [x for x in range(1,53)]
random.shuffle(cards)
card_index = 0
dealer = []
player = []

def deal_card():
    global card_index
    card = cards[card_index] % 13 + 1
    if card in [11,12,13]:
        card = 10
    card_index += 1
    return card

def start_game():
    dealer.append(deal_card())
    player.append(deal_card())
    player.append(deal_card())
    print 'Dealer - ', dealer[0], 'Player - ', player

def draw():
    player.append(deal_card())
    score = sum(player)
    if score > 21:
        print 'Dealer - ', dealer[0], 'Player - ', player
        print "Player went bust!"
        return 1
    elif score == 21:
        print 'Dealer - ', dealer[0], 'Player - ', player
        print "Player wins!!"
        return 1
    else:
        print 'Dealer - ', dealer[0], 'Player - ', player
        return 0

def stand():
    print 'Dealer - ', dealer, 'Player - ', player
    score = sum(dealer)
    while score < 21:
        dealer.append(deal_card())
        score = sum(dealer)
        print 'Dealer - ', dealer, 'Player - ', player
    if score == 21:
        print 'Dealer won!!'
    else:
        print 'Dealer busted!!'
    return 1
    

if __name__ == '__main__':
    start_game()
    while 1:
        print 'Hit (1) or Stand (2)'
        move = (raw_input())
        if not move:
            print 'Hit (1) or Stand (2)'
            continue
        move = int(move)
        if move == 1:
            ok = draw()
        elif move == 2:
            ok = stand()
        else:
            continue
        if ok:
            break

            

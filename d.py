import random
subs = ['cơ','dô','bích','tép']
the_card_score = [1,2,3,4,5,6,7,8,9,10,'J','Q','K']
class Card:
	def __init__(self,substances,card_score):
		self.substances = substances
		self.card_score = card_score
	def print_card(self):
		print("substances: ",self.substances)
		print("card_score: ", self.card_score)
class Player:
	def __init__(self,name,player_score,card_player):
		self.name = name
		self.player_score = player_score
		self.card_player = card_player

	def print_info(self):
		print("name: ",self.name)
		print("player_score: ", self.player_score)
def create_player():
	players = []
	total_player = int(input("enter total player: "))
	for i in range(total_player):
		name = input("enter name player: ")
		player_score = 0
		card_player = None
		player = Player(name,player_score,card_player)
		players.append(player)
	return players


def Dealer(deck,players):
	for i in range(len(players)):
		players[i].card_player = []
		for j in range(2):
			players[i].card_player.append(deck[i])
			deck.remove(deck[i])

def print_player(players):
	for i in range(len(players)):
		players[i].print_info()
		for j in range(2):
			players[i].card_player.print_card()



		
def creat_deck():
	deck = []
	for i in range(4):
		substances = subs[i]
		for j in range(13):
			card_score = the_card_score[j]
			the_card = Card(substances,card_score)
			deck.append(the_card)
	return deck
def print_deck(deck):
	for i in range(len(deck)):
		print('the card ' + str(i+1))
		deck[i].print_card()
def articles(deck):
	random.shuffle(deck)
	print_deck(deck)


def main():
	deck = creat_deck()
	player = create_player()
	print_player(player)
	Dealer(deck,player)
# 	print_deck(deck)
# 	print("newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
# 	articles(deck)
main()



# class player:
# 	def __init__(self):

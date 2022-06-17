import random
import time

class Mex:
	def __init__(self):
		self.botnames = ['Jan-Lid', 'Klaas-Jan', 'Willem-Alexander', 'Roderick', 'Lodewijk', 'Floris']
		self.numplayers = 0
		self.numbots = 0
		self.playernames = []
		self.playerrolls = {}
		self.laag = ''
		self.numthrows = 3
		self.mexcount = 1
		self.mex = ([2, 1], [1, 2])
		self.d32 = ([3, 2], [2, 3])
		self.d31 = ([3, 1], [1, 3])

	def get_numplayers(self):
		numplayers = int(input('    Met hoeveel van uw amices wilt u spelen? '))
		self.numbots = 7 - numplayers
		if numplayers < 6:
			print('\n    Aangezien u beschikt over een bedroevend lage hoeveelheid medeklemmers,\n    zullen we wat virtuele amices aan uw spel toevoegen.\n    Bij deze heeft u %i AI-mices.\n' % self.numbots)	
		else:
			print('\n    U gaat duidelijk niet om met laffeborrelaars. Klasse amice!\n')
		return numplayers	

	def get_playernames(self, numplayers):
		print('\n    Dan nu eens kijken met wie we aan de borreltafel staan.')
		playernames = [' '] * numplayers
		for player in range(numplayers):
			playernames[player] = input('\n    Amice, zou ik kennis met u mogen maken? ')
			if playernames[player] in ['HJ1', 'HJ2', 'HJ', 'hj1', 'hj2', 'hj', 'Willem', 'Willie', 'Willy', 'willem', 'willie', 'willy']:
				print('    Waardeloos.')
			else:
				print('    Wat mooi dat u erbij bent amice %s. Ik beloof u, u gaat kotsen vanavond.' % playernames[player])
		return playernames

	def start_game(self):
		print('\n\n\n\n\n\n                                   MEX')
		print('                       een zuip-app van Sloet INC.\n\n')	
		print('    Amice! Laten we een partij onredelijk veel fluiten trappen met een pot mex.\n\n')
		self.numplayers = self.get_numplayers()
		self.playernames = self.get_playernames(self.numplayers)
		if self.numbots > 0:
			self.playernames.extend(self.botnames[:self.numbots])
		random.shuffle(self.playernames)
		time.sleep(1)
		print('\n    Dit zijn de koninkies waarmee we gaan klemmen:\n')
		print('   ',*self.playernames)
		time.sleep(3)

	def play_round(self):
		for player in self.playernames:
			time.sleep(3)
			print('\n\n    Amice %s, aan u de beurt!' % player)
			for i in range(self.numthrows):
				dice = self.roll_dice(player, i)
				while dice == 31:
					dice = self.roll_dice(player, i)
				if dice == 32:
					break
				elif dice == 21:
					break
			# update score
			if dice not in [21, 32]:	
				if dice[0] == dice[1]:
					dice = dice[0]*100
				else:
					dice = max(dice)*10 + min(dice)
			self.playerrolls.update({player: dice})

	def roll_dice(self, player, i):
		if player not in self.botnames:
			input('\n    Druk op ENTER om te gooien')
			if player in ['Sluijter', 'Sloet', 'Ab', 'Bestuur', 'Bestuah', 'Ab Actis', 'Meneer de Ab']:
				time.sleep(1)
				dice = [random.randint(2,3), 1]
			elif player in ['HJ1', 'HJ2', 'HJ', 'hj1', 'hj2', 'hj', 'Willem', 'Willie', 'Willy', 'willem', 'willie', 'willy', 'jaars', 'Jaars', 'Jaarsch', 'jaarsch']:
				time.sleep(1)
				dice = [3, 2]
			else:
				time.sleep(1)
				dice = [random.randint(1,6), random.randint(1,6)]
		else:
			time.sleep(3)
			dice = [random.randint(1,6), random.randint(1,6)]
		temp = max(dice)*10 + min(dice)
		print('\n    %i' % temp)
		if self.check_mex(dice):
			if player == self.playernames[0]:
				self.numthrows = i+1
			return 21
		if self.check_32(dice):
			self.laag = player
			return 32
		if self.check_31(dice, player):
			return 31
		return dice

	def check_mex(self, dice):
		for mex in self.mex:
			if dice == mex:
				time.sleep(1)
				print('\n    MEEEEEXIIIICAANNOOOOO JALALALA. Vo voor jou amice.')
				self.mexcount += 1
				return True
		return False 

	def check_31(self, dice, player):
		for d31 in self.d31:
			if dice == d31:
				time.sleep(1)
				if player in self.botnames:
					delul = self.playernames[random.randint(0, self.numplayers)]
				else:
					delul = input('\n    Ahh 31, u deelt uit. Wie van uw amices is de lul? ')
				if delul in self.botnames:
					print('    %s heeft zojuist een halve bak gevouwen.' % delul)
				else:
					print('    %s, ZUIPEN KRENG!' % delul)
				return True
		return False

	def check_32(self, dice):
		for d32 in self.d32:
			if dice == d32:
				time.sleep(1)
				print('\n    Hahah laaaaag lul. Dat wordt zuipen.')
				return True
		return False

	def get_loser(self):
		low = 1000
		losers = []
		for key, value in self.playerrolls.items():
			if value != 21:
				if value < low:
					low = value
		for key, value in self.playerrolls.items():
			if value == low:
				losers.append(key)
		return losers

	def end_game(self):
		losers = self.get_loser()
		loser = ''
		if len(losers) > 1:
			print('\n    Lekker met z\'n %i\'en laag, hoogst zuipt.' % len(losers))
			loserrolls = {}
			for l in losers:
				print('\n    %s gooit:' % l)
				if l not in self.botnames:
					input('\n    Druk op ENTER om te gooien')
				time.sleep(2)
				roll = random.randint(1,6)
				print('\n    ',roll)
				loserrolls.update({l: roll})
			loser = max(loserrolls, key=loserrolls.get)
		else:
			loser = losers[0]
		bakken = 0.5*float(self.mexcount)
		print('\n    %s' % loser, '%f bakkies adten si-vous-plait. ZUIPEN! ZUIPEN DIE BAKKEN!' % bakken)

	def game_loop(self):
		self.start_game()
		self.play_round()
		self.end_game()

mexxen = Mex()
mexxen.game_loop()
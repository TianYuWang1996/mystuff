class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		print()
		for line in self.lyrics:
			print(line)

happy_bday = ["Happy birthday to you",
			  "I don't want to get sued",
			  "So I'll stop right there"]

bulls_on_parade = ["They rally around the family",
				   "With pockets full of shells"]

not_today = ["When the Death come",
			 "Life to the end",
			 "The Old One say",
			 "Not Today"]

Lyric_A = Song(happy_bday)
Lyric_B = Song(bulls_on_parade)
Lyric_C = Song(not_today)

Lyric_A.sing_me_a_song()
Lyric_B.sing_me_a_song()
Lyric_C.sing_me_a_song()
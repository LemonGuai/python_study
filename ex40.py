# mystuff = {"apple": "i am apples!"}
# print(mystuff['apple'])
# import ex40a
# print(ex40a.tangerine)


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["happy birthday to you", "i don't want to get sued", "so i'll stop right there"])

bulls_on_parade = Song(["they rally around the family", "with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
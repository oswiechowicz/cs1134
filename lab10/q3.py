from ArrayQueue1 import *

class Playlist:
    def __init__(self):
        self.playlist=ArrayQueue()
        self.size=0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def add_to_playlist(self,str_title):
        self.playlist.enqueue(str_title)
        self.size+=1

    def print_playlist(self):
        for i in range(self.size):
            print("Track ",i+1,": ",self.playlist.data[i])

    def play(self,track_no):
        if self.playlist.is_empty():
            raise Exception("Playlist is empty!")
        return self.playlist.data[track_no-1]

    def move_up(self,track_no):
        if self.playlist.is_empty():
            raise Exception("Playlist is empty!")
        first_part=self.playlist.data[:track_no-2]
        track=self.playlist.data[track_no-1]
        last_part=list(self.playlist.data[track_no-2]).extend(self.playlist.data[track_no-1:self.size])
        print(first_part,track,last_part)
        #self.playlist.data=first_part.extend(list(track).extend(last_part))

    def move_down(self,track_no):
        pass

    def remove_song(self,track_no):
        if self.playlist.is_empty():
            raise Exception("Playlist is empty!")
        first_part=self.playlist.data[:track_no-2]
        last_part=self.playlist.data[track_no-1:self.playlist.num_of_elems]
        self.playlist.data=first_part.extend(last_part)
        self.size-=1
        #self.playlist.data=first_part.extend(list(track).extend(last_part))
        print(self.playlist.data)


def main():
    p=Playlist()
    p.add_to_playlist("first")
    p.add_to_playlist("second")
    p.add_to_playlist("third")
    p.add_to_playlist("fourth")
    p.print_playlist()
    print(p.play(2))
    p.remove_song(3)
    p.print_playlist()

main()


#yes, the runtime would differ at move down and move up. They should be constant.
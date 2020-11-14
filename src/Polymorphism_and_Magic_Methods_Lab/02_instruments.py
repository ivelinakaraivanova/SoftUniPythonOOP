from abc import ABC, abstractmethod


class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass


def play_instrument(i):
    return i.play()



class Guitar:
    def play(self):
        print("playing the guitar")


guitar = Guitar()
play_instrument(guitar)


class Piano:
    def play(self):
        print("playing the piano")


piano = Piano()
play_instrument(piano)


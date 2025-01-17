class Rotor:
    def __init__(self, alphabet: str, rotor_position: int):
        self.alphabet = alphabet
        self.rotor_position = rotor_position

    def encode(self, letter: str) -> str:
        index = (self.alphabet.index(letter) + self.rotor_position) % len(self.alphabet)
        return self.alphabet[index]

    def rotate(self) -> bool:
        self.rotor_position = (self.rotor_position + 1) % len(self.alphabet)
        return self.rotor_position == 0

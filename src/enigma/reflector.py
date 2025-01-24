class Reflector:
    def __init__(self, alphabet: str):
        self.alphabet = alphabet

    def reflect(self, letter: str) -> str:
        index = ord(letter) - ord('A')
        return self.alphabet[index]

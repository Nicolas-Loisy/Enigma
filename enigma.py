from typing import List
from rotor import Rotor

class Enigma:
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ROTORS = [
        'JGDQOXUSCAMIFRVTPNEWKBLZYH',  # Rotor 1
        'NTZPSFBOKMWRCJDIVLAEYUXHGQ',  # Rotor 2
        'JVIUBHTCDYAKEQZPOSGXNRMWFL',  # Rotor 3
    ] # Rotor 02/1941

    def __init__(self, rotor_positions: List[int]):
        self.rotors = []
        self.set_rotors(rotor_positions)

    def set_rotors(self, rotor_positions: List[int]) -> None:
        if len(rotor_positions) != len(self.ROTORS):
            raise ValueError("Le nombre de configuration de positions de rotors doit correspondre au nombre de rotors.")
        
        if any(position > len(self.ALPHABET) or position < 1 for position in rotor_positions):
            raise ValueError("Les positions des rotors doivent être comprises entre 0 et la taille de l'alphabet.")
        
        self.rotors = [Rotor(alphabet, position-1) for alphabet, position in zip(self.ROTORS, rotor_positions)]

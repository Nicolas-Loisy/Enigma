from rotor import Rotor
from reflector import Reflector
from connection_board import ConnectionBoard

class Enigma:
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ROTORS = [
        'JGDQOXUSCAMIFRVTPNEWKBLZYH',  # Rotor 1
        'NTZPSFBOKMWRCJDIVLAEYUXHGQ',  # Rotor 2
        'JVIUBHTCDYAKEQZPOSGXNRMWFL',  # Rotor 3
    ]
    REFLECTOR = 'QYHOGNECVPUZTFDJAXWMKISRBL'
    # Configuration Enigma du 02/1941

    def __init__(self, rotor_positions: list[int], board_connections: list[str] = []):
        self.rotors = []
        self.reflector = None
        self.connection_board = None

        self.set_rotors(rotor_positions)
        self.set_reflector(self.REFLECTOR)
        self.set_connection_board(board_connections)

    def set_rotors(self, rotor_positions: list[int]) -> None:
        if len(rotor_positions) != len(self.ROTORS):
            raise ValueError("Le nombre de configuration de positions de rotors doit correspondre au nombre de rotors.")
        
        if any(position > len(self.ALPHABET) or position < 1 for position in rotor_positions):
            raise ValueError("Les positions des rotors doivent être comprises entre 0 et la taille de l'alphabet.")
        
        self.rotors = [Rotor(alphabet, position-1) for alphabet, position in zip(self.ROTORS, rotor_positions)]

    def set_reflector(self, reflector_alphabet: str) -> None:
        if len(reflector_alphabet) != len(self.ALPHABET):
            raise ValueError("La configuration du réflecteur doit correspondre à la taille de l'alphabet.")
        
        self.reflector = Reflector(reflector_alphabet)

    def set_connection_board(self, board_connections: list[str]) -> None:
        self.connection_board = ConnectionBoard(self.ALPHABET, board_connections)

    def run(self, message: str) -> str:
        encoded_message = ""
        message = message.upper()

        for letter in message:
            if letter not in self.ALPHABET:
                encoded_message += letter
                continue

            letter = self.connection_board.swap(letter)

            for rotor in self.rotors:
                letter = rotor.encode(letter)
            
            letter = self.reflector.reflect(letter)
            
            for rotor in reversed(self.rotors):
                letter = rotor.encode(letter, reverse=True)
            
            letter = self.connection_board.swap(letter)
                
            encoded_message += letter
            rotate_next = True
            
            for rotor in self.rotors:
                if rotate_next:
                    rotate_next = rotor.rotate()
                else:
                    break
        return encoded_message
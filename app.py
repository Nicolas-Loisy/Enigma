from enigma import Enigma

def main():
    initial_positions = [1, 1, 1]
    board_connections = ["AY", "CD", "EF"]

    message = "VIVE LA CRYPTO"

    enigma = Enigma(initial_positions, board_connections)
    encoded_message = enigma.run(message)
    print(f"Encoded message: {encoded_message}")
    
    enigma = Enigma(initial_positions, board_connections)  # Reset Enigma
    decoded_message = enigma.run(encoded_message)
    print(f"Decoded message: {decoded_message}")

if __name__ == "__main__":
    main()
from enigma import Enigma

def main():
    initial_positions = [1, 1, 1]
    enigma = Enigma(initial_positions)
    message = "SALUT"
    encoded_message = enigma.run(message)
    print(f"Encoded message: {encoded_message}")
    
    enigma = Enigma(initial_positions)  # Reset Enigma
    decoded_message = enigma.run(encoded_message)
    print(f"Decoded message: {decoded_message}")

if __name__ == "__main__":
    main()
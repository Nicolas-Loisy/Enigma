from src.enigma.enigma import Enigma
import tkinter as tk

class EnigmaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Machine Enigma")

        # Initial rotors positions input
        tk.Label(root, text="Positions Initiales:").grid(row=0, column=0)
        self.rotor_positions = [
            tk.Entry(root, width=5),
            tk.Entry(root, width=5),
            tk.Entry(root, width=5)
        ]
        for i, entry in enumerate(self.rotor_positions):
            entry.grid(row=0, column=i+1)
            entry.insert(0, "1")  # Example initial position

        # Board connections input
        tk.Label(root, text="Connexions du Tableau:").grid(row=1, column=0)
        self.board_connections = tk.Entry(root, width=20)
        self.board_connections.grid(row=1, column=1, columnspan=3)
        self.board_connections.insert(0, "AY CD EF")  # Example board connections

        # Message input
        tk.Label(root, text="Message :").grid(row=2, column=0)
        self.message = tk.Entry(root, width=20)
        self.message.grid(row=2, column=1, columnspan=3)
        self.message.insert(0, "VIVE LA CRYPTO")  # Example message

        # Run Enigma button
        tk.Button(root, text="Start Enigma", command=self.run_enigma).grid(row=3, column=0, columnspan=4)

        # Labels for encoded and decoded messages
        self.encoded_message = tk.Label(root, text="Message codé: ")
        self.encoded_message.grid(row=4, column=0, columnspan=4)

        self.decoded_message = tk.Label(root, text="Message décodé: ")
        self.decoded_message.grid(row=5, column=0, columnspan=4)

        # Error message label
        self.error_label = tk.Label(root, text="", fg="red")
        self.error_label.grid(row=6, column=0, columnspan=4)

    def run_enigma(self):
        try:
            # Get inputs from the UI
            initial_rotors_positions = [int(pos_entry.get()) for pos_entry in self.rotor_positions]
            board_connections = self.board_connections.get().split()
            message = self.message.get()

            # Encode the message
            enigma = Enigma(initial_rotors_positions, board_connections)
            encoded_message = enigma.run(message)
            self.encoded_message.config(text=f"Message codé: {encoded_message}")

            # Decode the message
            enigma = Enigma(initial_rotors_positions, board_connections)  # Reset Enigma
            decoded_message = enigma.run(encoded_message)
            self.decoded_message.config(text=f"Message décodé: {decoded_message}")
            
            self.error_label.config(text="")
        except Exception as e:
            self.error_label.config(text=f"Erreur: {str(e)}")

def main():
    root = tk.Tk()
    EnigmaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
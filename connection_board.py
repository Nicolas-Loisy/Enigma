class ConnectionBoard:
    def __init__(self, alphabet: str, connections: list):
        self.connections = self.parse_connections(alphabet, connections)

    def parse_connections(self, alphabet: str, connections: list[str]) -> list:
        connection_list = list(alphabet)
        used_letters = set()

        for pair in connections:
            if len(pair) != 2:
                raise ValueError("Chaque paire de connexions doit contenir exactement deux lettres.")
            
            a, b = pair
            if a in used_letters or b in used_letters:
                raise ValueError("Chaque lettre ne peut être utilisée qu'une seule fois dans les connexions.")
            
            used_letters.update(pair)

            index_a = ord(a) - ord('A')
            index_b = ord(b) - ord('A')
            connection_list[index_a], connection_list[index_b] = connection_list[index_b], connection_list[index_a]
        
        return connection_list

    def swap(self, letter: str) -> str:
        index = ord(letter) - ord('A')
        return self.connections[index]

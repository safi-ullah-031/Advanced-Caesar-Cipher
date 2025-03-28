class CaesarDESBase:
    def __init__(self, key: str, shift: int):
        self.key = key[:8].ljust(8, ' ')  # Ensure key is exactly 8 characters
        self.shift = shift % 26
        self.rounds = 16  # Total rounds

    def _apply_caesar_cipher(self, text: str, shift: int) -> str:
        return ''.join(self._shift_character(char, shift) for char in text)

    def _shift_character(self, char: str, shift: int) -> str:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

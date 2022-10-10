"""
Morse Code Translator: Morse code is an encoding scheme that uses dashes and dots to represent numbers and letters.
Implement a program that uses a dictionary to store the mapping from letters and numbers to Morse code.

- Your program should read a message from the user.
  Then it should translate each character in the message to its mapping code (function-name: `message_to_morse`).
  * Put a space between translated character.
    Example: Hello is translated into .... . .-.. .-.. ---
  * Put a 4 spaces when there is a space in the original message.
    Example: Hello World is translated into .... . .-.. .-.. ---    .-- --- .-. .-.. -...
- Your program should print the error message `Can't convert char [X]` if there is no mapping for specific characters.
  (where X is the character that is not found)
- Extend your program with functionality of decoding a morse code (function-name: `morse_to_message`).
- Extend your program with a function `translate_text` such that given a string it detects
  if it is a normal text or a morse code. Then based on the type of the message it translates to the other one.
"""

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..'}

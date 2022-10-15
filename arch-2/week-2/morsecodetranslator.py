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

from concurrent.futures.process import _system_limits_checked


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

def message_to_morse(message):
	messageInMorse = ''

	for char in message:
		if char == ' ':
			messageInMorse += '    '
		elif MORSE_CODE_DICT.get(char.upper()):
			morseChar = MORSE_CODE_DICT.get(char.upper())
			messageInMorse += morseChar + ' '
		else:
			return f'Can`t convert char [{char}]'
	return messageInMorse


def morse_to_message(morseCode):
	morseCode += ' '
	morseLetter = ''
	message = ''

	for char in morseCode:
		if char == ' ':
			if morseLetter in MORSE_CODE_DICT.values():
				message += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morseLetter)]
				morseLetter = ''
			else:
				continue
		else:
			morseLetter += char

	return message


def translate_text(message):
	if validateMorseCode(message):
		return morse_to_message(message)
	else:
		return message_to_morse(message)

def validateMorseCode(morseCode):
	morseChars = {'.', '-', ' '}

	for char in morseCode:
		if char not in morseChars:
			return False

	return True

if __name__ == '__main__':
	message = input('Enter a message: ')
	print(message_to_morse(message))
	print(morse_to_message(message))
	print(translate_text(message))

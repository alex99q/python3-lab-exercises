import os
import time

def encrypt_to_morse(input_str):
    morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.',
                       'D': '-..', 'E': '.', 'F': '..-.',
                       'G': '--.', 'H': '....', 'I': '..',
                       'J': '.---', 'K': '-.-', 'L': '.-..',
                       'M': '--', 'N': '-.', 'O': '---',
                       'P': '.--.', 'Q': '--.-', 'R': '.-.',
                       'S': '...', 'T': '-', 'U': '..-',
                       'V': '...-', 'W': '.--', 'X': '-..-',
                       'Y': '-.--', 'Z': '--..',

                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----',

                       ' ': ' ', '\n': '\n', ',': '--..--', '.': '.-.-.-',
                       '?': '..--..', '\'': '.----.', '/': '-..-.',
                       '-': '-....-', '(': '-.--.', ')': '-.--.-'}

    morse_str = ''

    for c in input_str.upper():
        if c in morse_code_dict:
            morse_str += morse_code_dict[c] + ' '

    return morse_str


def morse_to_sound(morse_code):
    for c in morse_code:
        if c == '.':
            os.system("morse_dot.mp3")
            time.sleep(0.03)
        elif c == '-':
            os.system("morse_dash.mp3")
            time.sleep(0.07)
        elif c == ' ':
            time.sleep(0.15)
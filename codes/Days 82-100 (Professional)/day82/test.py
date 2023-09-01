words_dict = {
    'A' :  '.-',
    'B' : '-...', 
    'C':  '-.-.',
    'D' :  '-..',
    'E' : '.',     
    'F' :  '..-.',
    'G' : '--.',
    'H' : '....',
    'I' :  '..',
    'J' :  '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' :  '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...', 'T': '-',
    'U' : '..-',
    'V' : '...-', 
    'W' : '.--', 
    'X' : '-..-', 
    'Y' : '-.--',     
    'Z ' :  '--..'
}

translate_word = input("Input a word to translate: ").upper()

translated_word = ''
for i in translate_word:
    try:
        translated_word += words_dict[i] + '  '
    except KeyError:
        translated_word += '   '

print(translated_word)
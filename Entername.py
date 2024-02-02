

def morsecodeinator():

    paragraph = input("Write a sentence: ")
    paragraph = paragraph.upper()
    option = int(input("Would you like english-morse[1] code or morse code-english[2]"))

    replacements = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
    }

    modified_paragraph = ""
    if option == 1:
        for letter in paragraph:
            if letter in replacements:
                modified_paragraph += replacements[letter] + " "
            else:
                modified_paragraph += letter

        print("New paragraph")
        print(modified_paragraph)

    elif option == 2:
        for morse in paragraph:
            reversed_replacements = {value: key for key, value in replacements.items()}
            
            if morse in reversed_replacements:
                modified_paragraph += reversed_replacements[morse] + " "
            else:
                modified_paragraph += morse + " "
        print("Here is your translated paragraph: ")
        print(modified_paragraph)

morsecodeinator()


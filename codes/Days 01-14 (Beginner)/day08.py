alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser (d, t, s):
    cipher = ''

    if d == 'encode':
        for i in t:
            if i not in alphabet:
                cipher += i
                continue
            else:
                index = alphabet.index(i) + s

                if index > 25:
                    x = index//26
                    index -= 26 * x

                cipher += alphabet[index]

        print(f"Here's the decoded result:\n{cipher}")

    elif d == 'decode':
        for i in t:
            if i not in alphabet:
                cipher += i
                continue
            else:
                index = alphabet.index(i) - s

                if index < 0:
                    x = -index//26
                    index += 26 * x

                cipher += alphabet[alphabet.index(i) - s]

        print(f"Here's the decoded result:\n{cipher}")
    else:
        print("Invalid input")



again = True
while again == True:

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(direction, text, shift)

    answer = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if answer == 'no':
        print('end')
        again = False
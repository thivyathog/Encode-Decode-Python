def encodeMessage(message, keycode):
    ciphertext = ""
    #alphabet = "abcdefghijklmnopqrstuvwxyz" # old
    alphabet = "!'^+%&/()=?_/*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ0123456789" # lower, upper and some special keys.
    for letter in message:

        if letter in alphabet:

            keyLetter = ((alphabet.index(letter)) + keycode) % len(alphabet)

            cipherLetter = alphabet[keyLetter]
            ciphertext = ciphertext + cipherLetter
        else:
            cipherLetter = letter
            ciphertext = ciphertext + cipherLetter

    return ciphertext


def decodeMessage(message, keycode):
    ciphertext = ""
    #alphabet = "abcdefghijklmnopqrstuvwxyz" # old
    alphabet = "!'^+%&/()=?_/*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ0123456789" # lower, upper and some special keys.
    for letter in message:

        if letter in alphabet:

            keyLetter = ((alphabet.index(letter)) - keycode) % len(alphabet)

            cipherLetter = alphabet[keyLetter]
            ciphertext = ciphertext + cipherLetter
        else:
            cipherLetter = letter
            ciphertext = ciphertext + cipherLetter

    return ciphertext


choice = 0
while choice < 9:
    choice = str(input("Press e to encode, d to decode, q to exit"))
    try:
        choice = str(input("Press 1 to encode, 2 to decode, 9 to exit "))
    except ValueError:
        print("Integer isnt allowed please Re enter.")
        continue
    if choice.lower == "e":
        message = input("What is the message ")
        keycode = int(input("Enter the key"))
        ciphertext = encodeMessage(message, keycode)

    elif choice.lower() == "d":
        message = input("What is the message ")
        keycode = int(input("Enter the key"))
        ciphertext = decodeMessage(message, keycode)

    elif choice.lower() == "q":
        exit(0)
    else:
        print("Invalid Choice")
        continue

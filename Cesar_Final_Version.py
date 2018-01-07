#!/usr/bin/python

def collectMessage():
    # get the input from the user
    # Never Trust The User :p
    from click._compat import raw_input
    message = raw_input("Enter the message you would like to translate:\n\n")
    return message

def collectKey():
    #get the key from the user input
    while True:
        from click._compat import raw_input
        key = raw_input("What is the key for your message? : \n")
        try:
            if int(key) == 0:
                print("The 0 key let your in a plaintext.\n")
                print("Please enter an integer between 1 and 127.\n")
                continue
            elif int(key) in range(255):
                return int(key)
            #else:
              #  print("Please enter an integer between 1 and 127.\n")
               # continue
        except ValueError:
            print("Please enter an integer between 1 and 127.\n")
            continue

def EncryptMessage(text,caeser_key):
    #match the key with the message
    ciphertext = ""
    for symbol in text:
        # Convert Symbols
        #E(x)=(X+K)%26
        X = ord(symbol)
        Y = (X + caeser_key) % 255
        ciphertext += chr(Y)
    return ciphertext

def DecryptMessage(text,caeser_key):
    #decryption of the message
    ciphertext = ""
    # Check for the negative key
    if caeser_key < 0:
        caeser_key = -caeser_key
        for symbol in text:
            # Convert Symbols
            # E(x)=(X-K)%26
            X = ord(symbol)
            Y = (X - caeser_key) % 255
            ciphertext += chr(Y)
    elif caeser_key >= 0:
        for symbol in text:
            # Convert Symbols
            X = ord(symbol)
            Y = (X - caeser_key) % 255
            ciphertext += chr(Y)
    return ciphertext

def ChooseMode():
    #Choose which mode of the program to launch
    while True:
         print('Do you wish to encrypt or decrypt a message?')
         from click._compat import raw_input
         mode = raw_input().lower()
         if mode in 'encrypt e decrypt d'.split():
             return mode
         else:
             print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def Cesar_Main():
    #The main program of Vigenere
    print("Do you want to use Cesar Cipher Mode ? (y):yes / (n):no")
    from click._compat import raw_input
    answer= raw_input().lower()
    answer.split()
    while answer[0] == 'y':
        choice_of_mode = ChooseMode()
        entered_message = collectMessage()
        entered_key = collectKey()
        if choice_of_mode[0] == 'e':
            final_form = EncryptMessage(entered_message,entered_key)
            print("Your Cipher Text is: " + final_form)
        elif choice_of_mode[0] == 'd':
            final_form = DecryptMessage(entered_message,entered_key)
            print("Your Plain Text is: " +final_form)
        print("Do you want to use Cesar Cipher Mode once again ? (y):yes / (n):no")
        from click._compat import raw_input
        answer = raw_input().lower()
        answer.split()
        if answer[0] == 'y':
            continue
        elif answer[0] == 'n':
            break
    print("Done!")

#launch the program YO!!!
Cesar_Main()

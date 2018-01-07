#!/usr/bin/python

import pyperclip

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
            if str(key):
                return str(key)
            else:
                print("Please enter a String key.\n")
                continue
        except ValueError:
            print("Please enter a String key.\n")
            continue

def Encryption(message,key):
        #Order The key
        key=key
        key_len=len(key)
        key_list=list(key)
        for i in range(0,key_len):
            key_list[i]=ord(key_list[i])
        k_list=sorted(key_list)
        for i in range(0,key_len):
            k_list[i]=chr(k_list[i])
        # Get The Message
        plaintext = message
        plaintext_len = len(plaintext)
        string = key + plaintext
        # Count The Number Of Lines
        nbr_lines=1
        for i in range(0,plaintext_len,key_len):
            nbr_lines+=1
        #Create The Matrice
        matlis=[[0 for x in range(key_len)] for z in range(nbr_lines)]
        #Make The Matrice
        mis=""
        j=0
        for i in range(0,len(string),key_len):
            if j == 0:
                mis+=str(pyperclip.copy(string[i:i+key_len]))
                mis=pyperclip.paste()
                lis=[i for i in pyperclip.paste()]
                matlis[j]=lis
            j+=1
            if (j > 0) and (j < nbr_lines):
                mis += str(pyperclip.copy(string[i+key_len:i + key_len+key_len]))
                mis = pyperclip.paste()
                lis = [i for i in pyperclip.paste()]
                matlis[j] = lis
                if j==(nbr_lines-1) and (len(matlis[j]) < key_len):
                    for q in range(0,(key_len-len(matlis[j]))):
                        matlis[j]+=" "
        #Reorder The Matrice
        matlst=[[0 for o2 in range(key_len)] for p2 in range(nbr_lines)]
        for i in range(0,len(k_list)):
                for j in range(0,key_len):
                    if k_list[i]==matlis[0][j]:
                        for s in range(0,(nbr_lines)):
                            matlst[s][i]=pyperclip.copy(matlis[s][j])
                            matlst[s][i]=pyperclip.paste()
                            matlis[0][j]=""
                        break
        #Collect The String
        crypt=""
        for i in range(1,nbr_lines):
            for j in range(key_len):
                crypt += str(matlst[i][j])

        return crypt

def Decryption(message, key):
    # Order The key
    key = key
    key_len = len(key)
    key_str_list = sorted(key)
    key_str_sorted = ""
    for i in range(0, len(key_str_list)):
        key_str_sorted += key_str_list[i]
    key_str_sorted_len = len(key_str_sorted)
    key_list = list(key)
    # Get The Message
    ciphertext = message
    ciphertext_len = len(ciphertext)
    string = key_str_sorted + ciphertext
    # Count The Number Of Lines
    nbr_lines = 1
    for i in range(0, ciphertext_len, key_str_sorted_len):
        nbr_lines += 1
    # Create The Matrice
    matlis = [[0 for x in range(key_str_sorted_len)] for z in range(nbr_lines)]
    # Make The Matrice
    mis = ""
    j = 0
    for i in range(0, len(string), key_str_sorted_len):
        if j == 0:
            mis += str(pyperclip.copy(string[i:i + key_str_sorted_len]))
            mis = pyperclip.paste()
            lis = [i for i in pyperclip.paste()]
            matlis[j] = lis
        j += 1
        if (j > 0) and (j < nbr_lines):
            mis += str(pyperclip.copy(string[i + key_str_sorted_len:i + key_str_sorted_len + key_str_sorted_len]))
            mis = pyperclip.paste()
            lis = [i for i in pyperclip.paste()]
            matlis[j] = lis
            if j == (nbr_lines - 1) and (len(matlis[j]) < key_str_sorted_len):
                for q in range(0, (key_len - len(matlis[j]))):
                    matlis[j] += " "
    #Reorder The Matrice
    matlst = [[0 for o2 in range(key_str_sorted_len)] for p2 in range(nbr_lines)]
    for i in range(0, len(key_list)):
        for j in range(0, key_str_sorted_len):
            if key_list[i] == matlis[0][j]:
                for s in range(0, (nbr_lines)):
                    matlst[s][i] = pyperclip.copy(matlis[s][j])
                    matlst[s][i] = pyperclip.paste()
                    matlis[0][j] = ""
                break
    #Collect The String
    decrypt = ""
    for i in range(1, nbr_lines):
        for j in range(key_str_sorted_len):
            decrypt += str(matlst[i][j])

    return decrypt

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

def Trans_Main():
    #The main program of Vigenere
    print("Do you want to use Transposition Cipher Mode ? (y):yes / (n):no")
    from click._compat import raw_input
    answer= raw_input().lower()
    answer.split()
    while answer[0] == 'y':
        choice_of_mode = ChooseMode()
        entered_message = collectMessage()
        entered_key = collectKey()
        if choice_of_mode[0] == 'e':
            final_form = Encryption(entered_message,entered_key)
            print("Your Cipher Text is: " + final_form)
        elif choice_of_mode[0] == 'd':
            final_form = Decryption(entered_message,entered_key)
            print("Your Plain Text is: " +final_form)
        print("Do you want to use Transposition Cipher Mode once again ? (y):yes / (n):no")
        from click._compat import raw_input
        answer = raw_input().lower()
        answer.split()
        if answer[0] == 'y':
            continue
        elif answer[0] == 'n':
            break
    print("Done!")

#launch the program YO!!!
Trans_Main()

#!/usr/bin/python

from tkinter import *
import test2
def OpenEncryption():
    algorithms=Tk()
    algorithms.title("Crypto Castle -Encryption-")
    algorithms.geometry("420x450-365-250")
    algorithms.configure(bg="black")
    #The First Frame of The New Widget
    frame_algorithms = Frame(algorithms)
    frame_algorithms.configure(bg="black")

    label_00 = Label(frame_algorithms, text="Welcome To Encryption", font=("arial", 23))
    label_00.configure(bg="black",fg="green")
    label_00.grid(row=0,column=2,sticky=N)

    # labels to make some space -_-
    label = Label(frame_algorithms, padx=10)
    label.configure(bg="black")
    label.grid(row=0, column=0)
    label = Label(frame_algorithms, padx=10)
    label.configure(bg="black")
    label.grid(row=0, column=1)

    def RunEncryptions():
        a=var1.get()
        b=var2.get()
        if (a==1) and (b==4):
            # Destroy the Frame of The New Widget
            frame_algorithms.destroy()
            algorithms.geometry("950x600-100-90")
            # The New Frame of Cesar
            frame1_algorithms = Frame(algorithms)
            frame1_algorithms.configure(bg="black")

            # The Function which make the BACK TO FIRST WIDGET
            def BackAlgorithms():
                algorithms.destroy()
                OpenEncryption()

            # introduction Entry
            label_00 = Label(frame1_algorithms, text="Welcome To Cesar Algorithm", font=("arial", 23))
            label_00.configure(padx=250, pady=10, bg="black", fg="green")
            label_00.grid(row=0, column=1)
            # here is the Key Entry
            label_01 = Label(frame1_algorithms, text="Enter The Key : ", padx=25, font=("arial", 20))
            label_01.configure(bg="black", fg="green")
            label_01.grid(row=1, column=1)
            keyText = Text(frame1_algorithms, font=("arial", 10))
            keyText.configure(fg="black", bg="green", width=20, height=1)
            keyText.grid(row=2, column=1)
            # labels to make some space -_-
            label = Label(frame1_algorithms, padx=10)
            label.configure(bg="black")
            label.grid(row=3, column=1)
            label = Label(frame1_algorithms, padx=10)
            label.configure(bg="black")
            label.grid(row=4, column=0, sticky=W)

            # Methods of Encryption and Decryption
            def EncryptingText():
                DecryptEntry.delete("1.0", END)
                key = keyText.get("1.0", "end-1c")
                PlainText = EncryptEntry.get("1.0", "end-1c")
                try:
                    if int(key) == 0:
                        DecryptEntry.insert("1.0", "The 0 key let your in a plaintext.\n")
                        DecryptEntry.insert("1.0", "Please enter an integer between 1 and 255.\n")
                        exit(0)
                except ValueError:
                    DecryptEntry.insert("1.0", "Please enter an integer between 1 and 255.\n")
                key1 = int(keyText.get("1.0", "end-1c"))
                EncryptText = test2.CesarEncryptMessage(PlainText, key1)
                DecryptEntry.insert("1.0", EncryptText)

            def DecryptingText():
                EncryptEntry.delete("1.0", END)
                key = int(keyText.get("1.0", "end-1c"))
                CipherText = DecryptEntry.get("1.0", "end-1c")
                DecryptText = test2.CesarDecryptMessage(CipherText, key)
                EncryptEntry.insert("1.0", DecryptText)

            # All The Buttons and Labels of Cesar Widgets
            # Text Cesar Entry
            EncryptEntry = Text(frame1_algorithms, font=("arial", 12))
            EncryptEntry.configure(fg="black", bg="green", width=50, height=8)
            EncryptEntry.grid(row=4, column=1, sticky=W)
            DecryptEntry = Text(frame1_algorithms, font=("arial", 12))
            DecryptEntry.configure(fg="black", bg="green", width=50, height=8)
            DecryptEntry.grid(row=4, column=1, sticky=E)
            # All Buttons of Cesar Widgets
            button_01 = Button(frame1_algorithms, text=" Encrypt ", command=EncryptingText, font=("arial", 15))
            button_01.configure(fg="green", bg="black")
            button_01.grid(row=5, column=1, sticky=W)
            button_02 = Button(frame1_algorithms, text=" Decrypt ", command=DecryptingText, font=("arial", 15))
            button_02.configure(fg="green", bg="black")
            button_02.grid(row=5, column=1, sticky=E)
            button_03 = Button(algorithms, text=" Quit ", command=algorithms.destroy, font=("Helvetica", 15))
            button_03.configure(fg="green", bg="black")
            button_03.place(x=431, y=500)
            button_04 = Button(algorithms, text=" Back ", command=BackAlgorithms, font=("arial", 15))
            button_04.configure(fg="green", bg="black")
            button_04.place(x=428, y=450)

            # clear function
            def ClearText():
                keyText.delete("1.0", END)
                EncryptEntry.delete("1.0", END)
                DecryptEntry.delete("1.0", END)

            label = Label(frame1_algorithms, text="Clear it before any new use Please")
            label.configure(bg="black")
            label.place(x=428, y=350)
            button_05 = Button(algorithms, text=" Clear ", command=ClearText, font=("arial", 15))
            button_05.configure(fg="green", bg="black")
            button_05.place(x=428, y=400)
            # Show The work
            frame1_algorithms.grid(column=1)
            algorithms.mainloop()
        if (a==1) and (b==5):
            # Destroy the Frame of The New Widget
            frame_algorithms.destroy()
            algorithms.geometry("950x600-100-90")
            # The New Frame of Cesar
            frame1_algorithms = Frame(algorithms)
            frame1_algorithms.configure(bg="black")

            # The Function which make the BACK TO FIRST WIDGET
            def BackAlgorithms():
                algorithms.destroy()
                OpenEncryption()

            # introduction Entry
            label_00 = Label(frame1_algorithms, text="Welcome To Cesar Algorithm", font=("arial", 23))
            label_00.configure(padx=250, pady=10, bg="black", fg="green")
            label_00.grid(row=0, column=1)
            # here is the Key Entry
            label_01 = Label(frame1_algorithms, text="Enter The SharedPrime : ", padx=25, font=("arial", 20))
            label_01.configure(bg="black", fg="green")
            label_01.grid(row=1, column=1,sticky=W)
            label_01 = Label(frame1_algorithms, text="Enter The SharedBase : ", padx=25, font=("arial", 20))
            label_01.configure(bg="black", fg="green")
            label_01.grid(row=1, column=1, sticky=E)
            keyText1 = Text(frame1_algorithms, font=("arial", 10))
            keyText1.configure(fg="black", bg="green", width=20, height=1)
            keyText1.grid(row=2, column=1,sticky=W)
            keyText2 = Text(frame1_algorithms, font=("arial", 10))
            keyText2.configure(fg="black", bg="green", width=20, height=1)
            keyText2.grid(row=2, column=1,sticky=E)
            # labels to make some space -_-
            label = Label(frame1_algorithms, padx=10)
            label.configure(bg="black")
            label.grid(row=3, column=1)
            label = Label(frame1_algorithms, padx=10)
            label.configure(bg="black")
            label.grid(row=4, column=0, sticky=W)

            # Methods of Encryption and Decryption
            SecretNumbertab = []

            def GetSecNum():
                secretN = int(keyText1.get("1.0","end-1c"))
                keyText1.delete(0, END)
                SecretNumbertab.append(int(secretN))
            def CalculateKey():
                sharedP = int(keyText1.get("1.0","end-1c"))
                sharedG = int(keyText2.get("1.0","end-1c"))
                SecretNumbertab1 = []
                SecretNumbertab1 = test2.DiffieHellmanEncryption(SecretNumbertab, sharedP, sharedG)
                return SecretNumbertab1[0]
            def EncryptingText():
                DecryptEntry.delete("1.0", END)
                key = int(CalculateKey())
                PlainText = EncryptEntry.get("1.0", "end-1c")
                try:
                    if int(key) == 0:
                        DecryptEntry.insert("1.0", "The 0 key let your in a plaintext.\n")
                        DecryptEntry.insert("1.0", "Please enter an integer between 1 and 255.\n")
                        exit(0)
                except ValueError:
                    DecryptEntry.insert("1.0", "Please enter an integer between 1 and 255.\n")
                key1 = int(CalculateKey())
                EncryptText = test2.CesarEncryptMessage(PlainText, key1)
                DecryptEntry.insert("1.0", EncryptText)

            def DecryptingText():
                EncryptEntry.delete("1.0", END)
                key = int(CalculateKey())
                CipherText = DecryptEntry.get("1.0", "end-1c")
                DecryptText = test2.CesarDecryptMessage(CipherText, key)
                EncryptEntry.insert("1.0", DecryptText)

            # All The Buttons and Labels of Cesar Widgets
            # Text Cesar Entry
            EncryptEntry = Text(frame1_algorithms, font=("arial", 12))
            EncryptEntry.configure(fg="black", bg="green", width=50, height=8)
            EncryptEntry.grid(row=4, column=1, sticky=W)
            DecryptEntry = Text(frame1_algorithms, font=("arial", 12))
            DecryptEntry.configure(fg="black", bg="green", width=50, height=8)
            DecryptEntry.grid(row=4, column=1, sticky=E)
            # All Buttons of Cesar Widgets
            button_01 = Button(frame1_algorithms, text=" Encrypt ", command=EncryptingText, font=("arial", 15))
            button_01.configure(fg="green", bg="black")
            button_01.grid(row=5, column=1, sticky=W)
            button_02 = Button(frame1_algorithms, text=" Decrypt ", command=DecryptingText, font=("arial", 15))
            button_02.configure(fg="green", bg="black")
            button_02.grid(row=5, column=1, sticky=E)
            button_03 = Button(algorithms, text=" Quit ", command=algorithms.destroy, font=("Helvetica", 15))
            button_03.configure(fg="green", bg="black")
            button_03.place(x=431, y=500)
            button_04 = Button(algorithms, text=" Back ", command=BackAlgorithms, font=("arial", 15))
            button_04.configure(fg="green", bg="black")
            button_04.place(x=428, y=450)

            # clear function
            def ClearText():
                keyText.delete("1.0", END)
                EncryptEntry.delete("1.0", END)
                DecryptEntry.delete("1.0", END)

            label = Label(frame1_algorithms, text="Clear it before any new use Please")
            label.configure(bg="black")
            label.place(x=428, y=350)
            button_05 = Button(algorithms, text=" Clear ", command=ClearText, font=("arial", 15))
            button_05.configure(fg="green", bg="black")
            button_05.place(x=428, y=400)
            # Show The work
            frame1_algorithms.grid(column=1)
            algorithms.mainloop()

    #Vars for Radiobuttons:

    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    #Labels of RadioButtons and RadioButtons
    label_02 = Label(frame_algorithms, text="1- Encryption Message \n Options:", font=("arial", 18))
    label_02.configure(bg="black", fg="green")
    label_02.grid(row=3,column=2,sticky=N)
    var1 = IntVar()
    Radiobutton1=Radiobutton(frame_algorithms, text="Cesar Algorithm            ", variable=var1,value=1,font=("arial", 15))
    Radiobutton1.configure(bg="black", fg="green", width=20,height=1)
    Radiobutton1.grid(row=4,column=2,sticky=N)
    Radiobutton2 = Radiobutton(frame_algorithms, text="Vigenere Algorithm       ", variable=var1,value=2,font=("arial", 15))
    Radiobutton2.configure(bg="black", fg="green", width=20, height=1)
    Radiobutton2.grid(row=5, column=2, sticky=N)
    Radiobutton3 = Radiobutton(frame_algorithms, text="Transposition Algorithm ", variable=var1,value=3,font=("arial", 15))
    Radiobutton3.configure(bg="black", fg="green", width=20, height=1)
    Radiobutton3.grid(row=6, column=2, sticky=N)
    label_01 = Label(frame_algorithms, text="2- Encryption Key \n Options:", font=("arial", 18))
    label_01.configure(bg="black", fg="green")
    label_01.grid(row=7,column=2,sticky=N)
    var2 = IntVar()
    Radiobutton4=Radiobutton(frame_algorithms, text="Your Choice   ", variable=var2,value=4,font=("arial", 15))
    Radiobutton4.configure(bg="black", fg="green", width=15,height=1)
    Radiobutton4.grid(row=8,column=2,sticky=N)
    Radiobutton5=Radiobutton(frame_algorithms, text="Diffie Hellman", variable=var2,value=5,font=("arial", 15))
    Radiobutton5.configure(bg="black", fg="green", width=15,height=1)
    Radiobutton5.grid(row=9,column=2,sticky=N)
    #Buttons of the use
    label = Label(frame_algorithms, padx=10)
    label.configure(bg="black")
    label.grid(row=10, column=2)
    button_Next = Button(frame_algorithms, text=" Next ", command=RunEncryptions, font=("arial", 15))
    button_Next.configure(fg="green", bg="black",borderwidth=5)
    button_Next.grid(row=11,column=2,sticky=N)
    button_Quit = Button(frame_algorithms, text=" Quit ", command=algorithms.destroy, font=("arial", 15))
    button_Quit.configure(fg="green", bg="black",borderwidth=5)
    button_Quit.grid(row=12,column=2,sticky=N)

    frame_algorithms.grid()
    algorithms.mainloop()

OpenEncryption()
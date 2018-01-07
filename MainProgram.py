#!/usr/bin/python
from tkinter import *
from tkinter import messagebox
import test2
#The ROOT WIDGET
root= Tk()
root.title("Crypto Castle")
root.geometry("648x650-250-150")
root.configure(bg="black")
#Functions:
#Function of Algorithms
def OpenAlgorithms():
    #The New Widget
    algorithms=Tk()
    algorithms.title("Crypto Castle -Algorithms-")
    algorithms.geometry("500x370-320-250")
    algorithms.configure(bg="black")
    #The First Frame of The New Widget
    frame_algorithms = Frame(algorithms)
    frame_algorithms.configure(bg="black")

    #The Cesar Button : For Encryption and Decryption
    def Cesar():
        #Destroy the Frame of The New Widget
        frame_algorithms.destroy()
        algorithms.geometry("950x600-100-90")
        # The New Frame of Cesar
        frame1_algorithms=Frame(algorithms)
        frame1_algorithms.configure(bg="black")
        #The Function which make the BACK TO FIRST WIDGET
        def BackAlgorithms():
            algorithms.destroy()
            OpenAlgorithms()
        #introduction Entry
        label_00 = Label(frame1_algorithms, text="Welcome To Cesar Algorithm", font=("arial", 23))
        label_00.configure(padx=250, pady=10, bg="black", fg="green")
        label_00.grid(row=0,column=1)
        #here is the Key Entry
        label_01=Label(frame1_algorithms, text="Enter The Key : ", padx=25,font=("arial",20))
        label_01.configure(bg="black", fg="green")
        label_01.grid(row=1,column=1)
        keyText = Text(frame1_algorithms, font=("arial", 10))
        keyText.configure(fg="black", bg="green", width=20,height=1)
        keyText.grid(row=2,column=1)
        #labels to make some space -_-
        label=Label(frame1_algorithms,padx=10)
        label.configure(bg="black")
        label.grid(row=3, column=1)
        label=Label(frame1_algorithms,padx=10)
        label.configure(bg="black")
        label.grid(row=4, column=0,sticky=W)
        #Methods of Encryption and Decryption
        def EncryptingText():
            #DecryptEntry.delete("1.0",END)
            key=keyText.get("1.0","end-1c")
            PlainText=EncryptEntry.get("1.0","end-1c")
            try:
                if int(key) == 0:
                    DecryptEntry.insert("1.0","The 0 key let your in a plaintext.\n")
                    DecryptEntry.insert("1.0","Please enter an integer between 1 and 255.\n")
                    exit(0)
            except ValueError:
                DecryptEntry.insert("1.0","Please enter an integer between 1 and 255.\n")
            key1=int(keyText.get("1.0","end-1c"))
            EncryptText = test2.CesarEncryptMessage(PlainText,key1)
            DecryptEntry.insert("1.0",EncryptText)
        def DecryptingText():
            EncryptEntry.delete("1.0",END)
            key = int(keyText.get("1.0","end-1c"))
            CipherText = DecryptEntry.get("1.0","end-1c")
            DecryptText = test2.CesarDecryptMessage(CipherText, key)
            EncryptEntry.insert("1.0", DecryptText)
        # All The Buttons and Labels of Cesar Widgets
        #Text Cesar Entry
        EncryptEntry = Text(frame1_algorithms, font=("arial", 12))
        EncryptEntry.configure(fg="black", bg="green", width=50,height=8)
        EncryptEntry.grid(row=4,column=1,sticky=W)
        DecryptEntry = Text(frame1_algorithms, font=("arial", 12))
        DecryptEntry.configure(fg="black", bg="green", width=50,height=8)
        DecryptEntry.grid(row=4, column=1,sticky=E)
        #All Buttons of Cesar Widgets
        button_01= Button(frame1_algorithms, text=" Encrypt ", command=EncryptingText, font=("arial", 15))
        button_01.configure(fg="green", bg="black")
        button_01.grid(row=5,column=1,sticky=W)
        button_02 = Button(frame1_algorithms, text=" Decrypt ", command=DecryptingText, font=("arial", 15))
        button_02.configure(fg="green", bg="black")
        button_02.grid(row=5,column=1,sticky=E)
        button_03 = Button(algorithms, text=" Quit ", command=algorithms.destroy, font=("Helvetica", 15))
        button_03.configure(fg="green", bg="black")
        button_03.place(x=431, y=500)
        button_04 = Button(algorithms, text=" Back ", command=BackAlgorithms, font=("arial", 15))
        button_04.configure(fg="green", bg="black")
        button_04.place(x=428, y=450)
        #clear function
        def ClearText():
            keyText.delete("1.0",END)
            EncryptEntry.delete("1.0",END)
            DecryptEntry.delete("1.0",END)
        label=Label(frame1_algorithms,text="Clear it before any new use Please")
        label.configure(bg="black")
        label.place(x=428, y=350)
        button_05 = Button(algorithms, text=" Clear ", command=ClearText, font=("arial", 15))
        button_05.configure(fg="green", bg="black")
        button_05.place(x=428, y=400)
        #Show The work
        frame1_algorithms.grid(column=1)
        algorithms.mainloop()
    # The Vigenere Button : For Encryption and Decryption
    def Vigenere():
        #Destroy the Frame of The New Widget
        algorithms.geometry("950x600-100-90")
        frame_algorithms.destroy()
        # The New Frame of Cesar
        frame2_algorithms=Frame(algorithms)
        frame2_algorithms.configure(bg="black")
        #The Function which make the BACK TO FIRST WIDGET
        def BackAlgorithms():
            algorithms.destroy()
            OpenAlgorithms()
        #introduction Entry
        label_00 = Label(frame2_algorithms, text="Welcome To Vigenere Algorithm", font=("arial", 23))
        label_00.configure(padx=250, pady=10, bg="black", fg="green")
        label_00.grid(row=0,column=1)
        #here is the Key Entry
        label_01=Label(frame2_algorithms, text="Enter The Key : ", padx=25,font=("arial",20))
        label_01.configure(bg="black", fg="green")
        label_01.grid(row=1,column=1)
        keyText = Text(frame2_algorithms, font=("arial", 10))
        keyText.configure(fg="black", bg="green", width=20,height=1)
        keyText.grid(row=2,column=1)
        #labels to make some space -_-
        label=Label(frame2_algorithms,padx=10)
        label.configure(bg="black")
        label.grid(row=3, column=1)
        def EncryptingText():
            DecryptEntry.delete("1.0",END)
            key=str(keyText.get("1.0","end-1c"))
            PlainText=EncryptEntry.get("1.0","end-1c")
            Matchedkey=test2.MatchedKey(PlainText,key)
            EncryptText = test2.VigenereEncryptMessage(PlainText,Matchedkey)
            DecryptEntry.insert("1.0",EncryptText)
        def DecryptingText():
            EncryptEntry.delete("1.0",END)
            key=str(keyText.get("1.0","end-1c"))
            CipherText = DecryptEntry.get("1.0","end-1c")
            Matchedkey=test2.MatchedKey(CipherText,key)
            DecryptText = test2.CesarDecryptMessage(CipherText,Matchedkey)
            EncryptEntry.insert("1.0", DecryptText)
        # All The Buttons and Labels of Cesar Widgets
        #Text Cesar Entry
        EncryptEntry = Text(frame2_algorithms, font=("arial", 12))
        EncryptEntry.configure(fg="black", bg="green", width=50,height=10)
        EncryptEntry.grid(row=4,column=1,sticky=W)
        DecryptEntry = Text(frame2_algorithms, font=("arial", 12))
        DecryptEntry.configure(fg="black", bg="green", width=50,height=10)
        DecryptEntry.grid(row=4, column=1,sticky=E)
        #All Buttons of Cesar Widgets
        button_01= Button(frame2_algorithms, text=" Encrypt ", command=EncryptingText, font=("arial", 15))
        button_01.configure(fg="green", bg="black")
        button_01.grid(row=5,column=1,sticky=W)
        button_02 = Button(frame2_algorithms, text=" Decrypt ", command=DecryptingText, font=("arial", 15))
        button_02.configure(fg="green", bg="black")
        button_02.grid(row=5,column=1,sticky=E)
        button_03 = Button(algorithms, text=" Quit ", command=algorithms.destroy, font=("Helvetica", 15))
        button_03.configure(fg="green", bg="black")
        button_03.place(x=431, y=500)
        button_04 = Button(algorithms, text=" Back ", command=BackAlgorithms, font=("arial", 15))
        button_04.configure(fg="green", bg="black")
        button_04.place(x=428, y=450)
        #clear function
        def ClearText():
            keyText.delete("1.0",END)
            EncryptEntry.delete("1.0",END)
            DecryptEntry.delete("1.0",END)
        button_05 = Button(algorithms, text=" Clear ", command=ClearText, font=("arial", 15))
        button_05.configure(fg="green", bg="black")
        button_05.place(x=428, y=400)
        #Show The work
        frame2_algorithms.grid(column=1)
        algorithms.mainloop()
    # The Transposition Button : For Encryption and Decryption
    def Transposition():
        #Destroy the Frame of The New Widget
        frame_algorithms.destroy()
        algorithms.geometry("1010x600-100-90")
        # The New Frame of Cesar
        frame3_algorithms=Frame(algorithms)
        frame3_algorithms.configure(bg="black")
        #The Function which make the BACK TO FIRST WIDGET
        def BackAlgorithms():
            algorithms.destroy()
            OpenAlgorithms()
        #introduction Entry
        label_00 = Label(frame3_algorithms, text="Welcome To Transposition Algorithm", font=("arial", 23))
        label_00.configure(padx=250, pady=10, bg="black", fg="green")
        label_00.grid(row=0,column=1)
        #here is the Key Entry
        label_01=Label(frame3_algorithms, text="Enter The Key : ", padx=25,font=("arial",20))
        label_01.configure(bg="black", fg="green")
        label_01.grid(row=1,column=1)
        keyText = Text(frame3_algorithms, font=("arial", 10))
        keyText.configure(fg="black", bg="green", width=20,height=1)
        keyText.grid(row=2,column=1)
        #labels to make some space -_-
        label=Label(frame3_algorithms,padx=10)
        label.configure(bg="black")
        label.grid(row=3, column=1)
        def EncryptingText():
            DecryptEntry.delete("1.0",END)
            key=str(keyText.get("1.0","end-1c"))
            PlainText=EncryptEntry.get("1.0","end-1c")
            EncryptText = test2.TranspositionEncryption(PlainText,key)
            DecryptEntry.insert("1.0",EncryptText)
        def DecryptingText():
            EncryptEntry.delete("1.0",END)
            key=str(keyText.get("1.0","end-1c"))
            CipherText = DecryptEntry.get("1.0","end-1c")
            DecryptText = test2.TranspositionDecryption(CipherText,key)
            EncryptEntry.insert("1.0", DecryptText)
        # All The Buttons and Labels of Cesar Widgets
        #Text Cesar Entry
        EncryptEntry = Text(frame3_algorithms, font=("arial", 12))
        EncryptEntry.configure(fg="black", bg="green", width=50,height=10)
        EncryptEntry.grid(row=4,column=1,sticky=W)
        DecryptEntry = Text(frame3_algorithms, font=("arial", 12))
        DecryptEntry.configure(fg="black", bg="green", width=50,height=10)
        DecryptEntry.grid(row=4, column=1,sticky=E)
        #All Buttons of Cesar Widgets
        button_01= Button(frame3_algorithms, text=" Encrypt ", command=EncryptingText, font=("arial", 15))
        button_01.configure(fg="green", bg="black")
        button_01.grid(row=5,column=1,sticky=W)
        button_02 = Button(frame3_algorithms, text=" Decrypt ", command=DecryptingText, font=("arial", 15))
        button_02.configure(fg="green", bg="black")
        button_02.grid(row=5,column=1,sticky=E)
        button_03 = Button(algorithms, text=" Quit ", command=algorithms.destroy, font=("Helvetica", 15))
        button_03.configure(fg="green", bg="black")
        button_03.place(x=462, y=500)
        button_04 = Button(algorithms, text=" Back ", command=BackAlgorithms, font=("arial", 15))
        button_04.configure(fg="green", bg="black")
        button_04.place(x=459, y=450)
        #clear function
        def ClearText():
            keyText.delete("1.0",END)
            EncryptEntry.delete("1.0",END)
            DecryptEntry.delete("1.0",END)
        button_05 = Button(algorithms, text=" Clear ", command=ClearText, font=("arial", 15))
        button_05.configure(fg="green", bg="black")
        button_05.place(x=459, y=400)
        #Show The work
        frame3_algorithms.grid(column=1)
        algorithms.mainloop()
    def DiffieHellman():
        # Destroy the Frame of The New Widget
        frame_algorithms.destroy()
        algorithms.geometry("600x650-250-90")
        # The New Frame of Cesar
        frame4_algorithms = Frame(algorithms)
        frame4_algorithms.configure(bg="black")

        def BackAlgorithms():
            algorithms.destroy()
            OpenAlgorithms()
        SecretNumbertab=[]
        def GetSecNum():
            secretN = keyText_04.get()
            keyText_04.delete(0,END)
            numberU = keyText_03.get()
            SecretNumbertab.append(int(secretN))
            if (len(SecretNumbertab) == int(numberU)):
                button_01E.pack_forget()
        def CalculateKey():
            sharedP=int(keyText_01.get())
            sharedG=int(keyText_02.get())
            numberU = int(keyText_03.get())
            SecretNumbertab1=[]
            SecretNumbertab1 =test2.DiffieHellmanEncryption(SecretNumbertab,sharedP,sharedG)
            EncryptEntry.insert("1.0",SecretNumbertab1)
        # introduction Entry
        label_00 = Label(frame4_algorithms, text="Welcome To DiffieHellman Algorithm", font=("arial", 23))
        label_00.configure(padx=50, pady=10, bg="black", fg="green")
        label_00.grid(row=0, column=1)
        #here is the Key Entry
        label_01=Label(frame4_algorithms, text="Enter The Shared Prime Key : ", padx=25,font=("arial",15))
        label_01.configure(bg="black", fg="green")
        label_01.grid(row=1,column=1)
        keyText_01 = Entry(frame4_algorithms, font=("arial", 10))
        keyText_01.configure(fg="black", bg="green", width=20)
        keyText_01.grid(row=2,column=1)
        label_02 = Label(frame4_algorithms, text="Enter The Shared Base Key : ", padx=25, font=("arial", 15))
        label_02.configure(bg="black", fg="green")
        label_02.grid(row=3, column=1)
        keyText_02 = Entry(frame4_algorithms, font=("arial", 10))
        keyText_02.configure(fg="black", bg="green", width=20)
        keyText_02.grid(row=4, column=1)
        label_03 = Label(frame4_algorithms, text="Enter The Number of Users: ", padx=25, font=("arial", 15))
        label_03.configure(bg="black", fg="green")
        label_03.grid(row=5, column=1)
        keyText_03 = Entry(frame4_algorithms, font=("arial", 10))
        keyText_03.configure(fg="black", bg="green", width=20)
        keyText_03.grid(row=6, column=1)
        label_04 = Label(frame4_algorithms, text="Enter The Secret Numbers(One by One): ", padx=25, font=("arial", 15))
        label_04.configure(bg="black", fg="green")
        label_04.grid(row=7, column=1)
        keyText_04 = Entry(frame4_algorithms, font=("arial", 10))
        keyText_04.configure(fg="black", bg="green", width=20)
        keyText_04.grid(row=8, column=1)
        button_01E = Button(frame4_algorithms, text=" Enter ", command=GetSecNum, font=("arial", 15))
        button_01E.configure(fg="green", bg="black")
        button_01E.grid(row=9, column=1)
        label_05 = Label(frame4_algorithms, text="All The Keys : ", padx=25, font=("arial", 15))
        label_05.configure(bg="black", fg="green")
        label_05.grid(row=10, column=1)
        EncryptEntry = Text(frame4_algorithms, font=("arial", 12))
        EncryptEntry.configure(fg="black", bg="green", width=50, height=10)
        EncryptEntry.grid(row=11, column=1, sticky=N)
        button_02 = Button(frame4_algorithms, text=" Calculate ", command=CalculateKey, font=("arial", 15))
        button_02.configure(fg="green", bg="black")
        button_02.grid(row=12, column=1)
        button_03 = Button(algorithms, text=" Back ", command=BackAlgorithms, font=("arial", 15))
        button_03.configure(fg="green", bg="black")
        button_03.place(x=240, y=600)
        button_04 = Button(algorithms, text=" Quit ", command=algorithms.destroy, font=("arial", 15))
        button_04.configure(fg="green", bg="black")
        button_04.place(x=500, y=600)
        # clear function
        def ClearText():
            keyText_01.delete(0,END)
            keyText_02.delete(0,END)
            keyText_03.delete(0,END)
            keyText_04.delete(0,END)
            EncryptEntry.delete("1.0", END)
        button_05 = Button(algorithms, text=" Clear ", command=ClearText, font=("arial", 15))
        button_05.configure(fg="green", bg="black")
        button_05.place(x=340, y=600)
        # Show The work
        frame4_algorithms.grid(column=1)
        algorithms.mainloop()
        # The Function which make the BACK TO FIRST WIDGET

#All The Buttons and Labels of Algorithms Widgets
    label_00 = Label(frame_algorithms, text=" Welcome To Algorithms", font=("arial", 23))
    label_00.configure(bg="black", fg="green")
    label_00.pack(side=TOP, fill=Y, expand=0)
    label_01 = Label(frame_algorithms, text="  Choose an Algorithm to Test Please  ", font=("arial", 23))
    label_01.configure(bg="black", fg="green")
    label_01.pack(side=TOP, fill=Y, expand=0)
    #Button Cesar in Algorithms Widget
    label_02 = Button(frame_algorithms, text=" </Cesar> ",command=Cesar, font=("arial", 23))
    label_02.configure(bg="black", fg="green",borderwidth=5)
    label_02.pack(side=TOP, fill=Y, expand=0)
    # Button Vignere in Algorithms Widget
    label_03 = Button(frame_algorithms, text=" </Vigenere> ",command=Vigenere, font=("arial", 23))
    label_03.configure(bg="black", fg="green",borderwidth=5)
    label_03.pack(side=TOP, fill=Y, expand=0)
    label_04 = Button(frame_algorithms, text=" </Transposition> ",command=Transposition, font=("arial", 23))
    label_04.configure(bg="black", fg="green",borderwidth=5)
    label_04.pack(side=TOP, fill=Y, expand=0)
    label_05 = Button(frame_algorithms, text=" </Diffie Hellman> ",command=DiffieHellman, font=("arial", 23))
    label_05.configure(bg="black", fg="green",borderwidth=5)
    label_05.pack(side=TOP, fill=Y, expand=0)
    button_03 = Button(frame_algorithms, text=" </Quit> ", command=algorithms.destroy, font=("arial", 15))
    button_03.configure(fg="green", bg="black",borderwidth=5)
    button_03.pack(side=BOTTOM,anchor=N, fill=Y, expand=1)

    frame_algorithms.pack(expand=0)
    algorithms.mainloop()



var1 = IntVar()
var2 = IntVar()

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
        # global var1
        a = var1.get()
        b = var2.get()
        print(var1.get())
        print(b)
        # if (a==1) and (b==4):
    #Vars for Radiobuttons:

    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    #Labels of RadioButtons and RadioButtons
    label_02 = Label(frame_algorithms, text="1- Encryption Message \n Options:", font=("arial", 18))
    label_02.configure(bg="black", fg="green")
    label_02.grid(row=3,column=2,sticky=N)
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

def OpenDecryption():
    algorithms=Tk()
    algorithms.title("Crypto Castle -Decryption-")
    algorithms.geometry("420x450-365-250")
    algorithms.configure(bg="black")
    #The First Frame of The New Widget
    frame_algorithms = Frame(algorithms)
    frame_algorithms.configure(bg="black")

    label_00 = Label(frame_algorithms, text="Welcome To Decryption", font=("arial", 23))
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
        print(a)
        #if (a==1) and (b==4):

    #Vars for Radiobuttons:

    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    #Labels of RadioButtons and RadioButtons
    label_02 = Label(frame_algorithms, text="1- Decryption Message \n Options:", font=("arial", 18))
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
    label_01 = Label(frame_algorithms, text="2- Decryption Key \n Options:", font=("arial", 18))
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


#Frame The root Widget
fram_00=Frame(root)
fram_00.configure(bg="black")
#Label Photo
photo=PhotoImage(file="matrix2.png")
label_04=Label(fram_00,image=photo)
label_04.configure(padx=10,pady=10,bg="black")
label_04.pack(side=TOP,fill=X,expand=0)
#Label One
label_00=Label(fram_00, text=" Welcome To Crypto Castle ", font=("arial", 23))
label_00.configure(padx=50,pady=10,bg="black",fg="green")
label_00.pack(side=TOP,fill=X,expand=0)
#Label Two
label_05=Label(fram_00, text="  Choose an Option Please  ", font=("arial", 23))
label_05.configure(padx=50,pady=10,bg="black",fg="green")
label_05.pack(side=TOP,fill=X,expand=0)
#All The Work is Here:
#Label Three Button of Algorithms
button_00=Button(fram_00, text=" </Algorithms> ",command=OpenAlgorithms, font=("arial", 23))
button_00.configure(padx=20,pady=8,fg="green",bg="black",relief="ridge",borderwidth=10)
button_00.pack(side=TOP,fill=Y,expand=1)
#Label Four Button of Encryption
button_01=Button(fram_00, text=" </Encryption> ",command=OpenEncryption, font=("arial", 23))
button_01.configure(padx=20,pady=8,fg="green",bg="black",relief="ridge",borderwidth=10)
button_01.pack(side=TOP,fill=Y,expand=1)
#Label Six Button of Decryption
button_02=Button(fram_00, text=" </Decryption> ",command=OpenDecryption, font=("arial", 23))
button_02.configure(padx=20,pady=8,fg="green",bg="black",relief="ridge",borderwidth=10)
button_02.pack(side=TOP,fill=Y,expand=1)
# The Widget of Quit -Done-
button_06=Button(root, text=" Quit ",command=root.destroy, font=("arial", 15))
button_06.configure(padx=20,pady=5,fg="green",bg="black")
button_06.pack(side=BOTTOM,fill=Y,expand=0,anchor=N)
fram_00.pack(expand=0)
root.mainloop()

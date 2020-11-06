from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random
window=Tk()
window.title("Hangman")
word_list=["AUSTRALIA","INDIA","SINGAPORE","NORWAY","UAE","NIGERIA","MOROCCO","SPAIN","MEXICO","SWEDEN","FINLAND","UKRAINE","GERMANY","USA","BELGIUM","TURKEY","COLOMBIA","CHILE","BAHRAIN","GEORGIA","FRANCE","POLAND","EGYPT","DENMARK","QATAR"]

photos=[PhotoImage(file='C:/Users/AISHWARYA/Downloads/images/images/hang0.png'),PhotoImage(file='C:/Users/AISHWARYA/Downloads/images/images/hang1.png'),PhotoImage(file='C:/Users/AISHWARYA/Downloads/images/images/hang2.png'),PhotoImage(file="C:/Users/AISHWARYA/Downloads/images/images/hang3.png"),PhotoImage(file="C:/Users/AISHWARYA/Downloads/images/images/hang4.png"),PhotoImage(file="C:/Users/AISHWARYA/Downloads/images/images/hang5.png"),PhotoImage(file="C:/Users/AISHWARYA/Downloads/images/images/hang6.png"),PhotoImage(file="C:/Users/AISHWARYA/Downloads/images/images/hang7.png"),PhotoImage(file="C:/Users/AISHWARYA/Downloads/images/images/hang8.png"),PhotoImage(file="C:/Users/AISHWARYA/Downloads/images/images/hang9.png"),PhotoImage(file="C:/Users/AISHWARYA/Downloads/images/images/hang10.png"),PhotoImage(file="C:/Users/AISHWARYA/Downloads/images/images/hang11.png")]

                   
def newgame():
    global the_word_withSpaces
    global numberofguesses
    numberofguesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_list)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))
def guess(letter):
    global numberofguesses
    if numberofguesses<11:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangman","you guessed it!")
                    newgame()
        else:
            numberofguesses+=1
            imgLabel.config(image=photos[numberofguesses])
            if numberofguesses==11 :
                    messagebox.showwarning("Hangman","Game over!")
        
imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window, textvariable=lblWord,font=("Consolas 24 bold")).grid(row=0, column=0, columnspan=15, padx=10)




n=0
for c in ascii_uppercase:
    Button(window,text=c,command=lambda c=c: guess(c),font=("Helvetica 18"), width=4).grid(row=1+n//9,column=n%9)
    n+=1

Button(window,text="New\nGame", command=lambda:newgame(), font=("Helvetica 10")).grid(row=3,column=8,sticky="NSWE")
newgame()
window.mainloop()

from tkinter import *
import random
from PIL import ImageTk ,Image

root=Tk()
root.configure(background="orange")
root.title("Endless Pokemon Game")
root.geometry("800x600")

btn_img=ImageTk.PhotoImage(Image.open ("button1.png"))
pikachu=ImageTk.PhotoImage(Image.open ("pikachu.png"))
squirtle=ImageTk.PhotoImage(Image.open ("squirtle.png"))
bulbasaur=ImageTk.PhotoImage(Image.open ("bulbasaur.png"))
luxray=ImageTk.PhotoImage(Image.open ("luxray.png"))
oddish=ImageTk.PhotoImage(Image.open ("oddish.jpg"))

labelplayer1=Label(root,text="player 1",background="red",fg="white")
labelplayer1.place(relx=0.1,rely=0.3,anchor=CENTER)
labelplayer2=Label(root,text="player 2",background="red",fg="white")
labelplayer2.place(relx=0.8,rely=0.3,anchor=CENTER)

labelcard=Label(root)
labelcard.place(relx=0.5,rely=0.5,anchor=CENTER)

labelscorep1=Label(root)
labelscorep1.place(relx=0.1,rely=0.4,anchor=CENTER)
labelscorep2=Label(root)
labelscorep2.place(relx=0.8,rely=0.4,anchor=CENTER)
pokemon_list=[pikachu,squirtle,bulbasaur,luxray,oddish]
power_list=[200,50,60,150,100]
player1score=0
player2score=0
def player1():
    global player1score
    randomno1=random.randint(0,4)
    random_pokemon1=pokemon_list[randomno1]
    labelcard["image"]=random_pokemon1
    random_power1=power_list[randomno1]
    player1score=player1score+random_power1
    labelscorep1["text"]=str(player1score)
    
def player2():
    global player2score
    randomno2=random.randint(0,4)
    random_pokemon2=pokemon_list[randomno2]
    labelcard["image"]=random_pokemon2
    random_power2=power_list[randomno2]
    player2score=player2score+random_power2
    labelscorep2["text"]=str(player2score)    
    
    
    
buttonp1=Button(root,image=btn_img,command=player1)
buttonp1.place(relx=0.1,rely=0.6,anchor=CENTER)

buttonp2=Button(root,image=btn_img,command=player2)
buttonp2.place(relx=0.8,rely=0.6,anchor=CENTER)

root.mainloop()
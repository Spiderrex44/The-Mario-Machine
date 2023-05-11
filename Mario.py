#This will inform the user about Mario Characters
#Logan Litchfield
#M08 Final Exam
#5/11/2023


#This is where everything gets impoted
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


#This creates the window
window = tk.Tk()
window.title('The Mario Machine')
window.geometry("1920x1080")
window.configure(bg="black")

     
#This is where text gets added
label1 = tk.Label(window,font=(500), text='PLEASE SELECT PLAYER')
label1.place(x=400, y=10)
label1.configure(bg="black",fg="white" )
label1.place(x=650, y=60)


#This is where the awnser box gets made
ansBox = tk.Label(window, text='')
ansBox.place(x=70, y=140)
ansBox.configure(bg="black",fg="white" )


#Exit Button
def close_window (): 
    window.destroy()


#MARIO WINDOW----------------------------------------------------------------------------------------------------------


def open_mario_window():

    # Create the second window
    mario_window = tk.Toplevel()
    
    mario_window.title('Mario')
    
    mario_window.geometry("965x900")
    
    mario_window.configure(bg="black")


    # Add a label to the second window
    labelM = tk.Label(mario_window,font=(500), text='Mr. Video Game Himself!')
    
    labelM.pack(padx=35, pady=35)
    
    labelM.configure(bg="black",fg="white" )
    
    
    
    #Add the paragraph to the second window
    paraM = tk.Label(mario_window, text="Mario is arguably the most iconic video game character of all time, even being referred \n to as the mickey mouse of video games. Nintendo decided on the name Mario when the \n landlord of the warehouse of Nintendo of America “Mario Segale” barged into a meeting room \n demanding late rent, he is also the same man that inspired the team to make Mario Italian. \n Mario wears his iconic blue overalls because Miyamoto needed a way for his arms to not blend \n in with his torso, so he made him wear a red shirt and blue overalls. Mario didn't always wear \n these colors, he's had quite a few changes through the years. In his first few appearances he \n had red and even black pairs of overalls. It wasn't till “Super Mario World” that the color scheme \n we know and love today set in. Mario has been featured in over 210 games. But is mainly \n known for his mainline and spin-off games. Super Mario Bros, Mario Kart, Mario Party to name a \n few. Nintendo's effort to make every Mario game accessible and fun for everyone is why \n everyone around the world has a memory of the world's most famous plumber.")
    
    paraM.configure(bg="black",fg="white" )
    
    paraM.pack(padx=0, pady=0)
    
    
    #Add Timeline Image
    global mario_tl, new_mariotl
    
    mario_tl = Image.open("Mariotl.png")

    resized = mario_tl.resize((960, 540), Image.ANTIALIAS)

    new_mariotl = ImageTk.PhotoImage(resized)

    mariotl_label = tk.Label(mario_window, image=new_mariotl)
    
    mariotl_label.place(x=0, y=310)
    
    mariotl_label.pack
    
    
    
#LUIGI WINDOW----------------------------------------------------------------------------------------------------------

def open_luigi_window():

    # Create the second window
    luigi_window = tk.Toplevel()
    
    luigi_window.title('Luigi')
    
    luigi_window.geometry("965x900")
    
    luigi_window.configure(bg="black")


    # Add a label to the second window
    labelL = tk.Label(luigi_window,font=(500), text='The Eternal Understudy!')
    
    labelL.pack(padx=35, pady=35)
    
    labelL.configure(bg="black",fg="white" )
    
    
    
    #Add the paragraph to the second window
    paraL = tk.Label(luigi_window, text="Luigi, also referred to as Player 2, Green Mario, and Mario's shadow was Mario's brother \n ever since the original Mario bros. Luigi was named after the second most iconic Italian name. \n Luigi can also mean “Similar” in Japanese, adding to the fact that Luigi will always be Marios \n player 2. Despite typically being a color swap of Mario, Luigi eventually got his own \n characteristics. While Mario is short and a bit round, Luigi is tall and skinny. Having a slightly \n different mustache, darker overalls, and even sometimes stripped socks. He also plays \n differently than Mario, Luigi is a lot more slippery to control, and his jumps are much higher, \n making him stand out from Mario. Luigi wasn't always player 2 though, 2001s GameCube \n launch title, Luigi's Mansion was Luigi's first solo adventure. This time, Luigi was on a mission to \n save his brother from a ghost filled mansion. Other than Luigi's Mansion sequels, that was his \n only time in the main spotlight. That was until 2013, when Nintendo announced that year would \n be Deemed “The Year of Luigi”. With games like New Super Luigi U, and Dr. Luigi. Our loveable \n green plumber finally got his spotlight.")
    
    paraL.configure(bg="black",fg="white" )
    
    paraL.pack(padx=0, pady=0)
    
    
    #Add Timeline Image
    global luigi_tl, new_luigitl
    
    luigi_tl = Image.open("luigitl.png")

    resized = luigi_tl.resize((960, 540), Image.ANTIALIAS)

    new_luigitl = ImageTk.PhotoImage(resized)

    luigitl_label = tk.Label(luigi_window, image=new_luigitl)
    
    luigitl_label.place(x=0, y=310)
    
    luigitl_label.pack
    


#PEACH WINDOW----------------------------------------------------------------------------------------------------------

def open_peach_window():

    # Create the second window
    peach_window = tk.Toplevel()
    
    peach_window.title('Peach')
    
    peach_window.geometry("965x900")
    
    peach_window.configure(bg="black")


    # Add a label to the second window
    labelP = tk.Label(peach_window,font=(500), text='Princess of Toadstools!')
    
    labelP.pack(padx=35, pady=35)
    
    labelP.configure(bg="black",fg="white" )
    
    
    
    #Add the paragraph to the second window
    paraP = tk.Label(peach_window, text="Princess Peach, the ruler of the Mushroom kingdom, and the classic damsel in distress \n stolen by the evil king of the Koopas. In the majority of the Mario games, Bowser steals Peach, \n and Mario has to save her. That's the main reason Mario goes on his adventures. Peach has \n had two different names throughout her life. In Japan, she was always called Princess Peach. \n But here in North America, Peach was named Princess Toadstool, in reference to her being the \n ruler of the Mushroom Kingdom. Peach has also been through many design iterations. Many \n people think Peach started out pink in the game “Donkey Kong”, but that was a different girl \n named Pauline. Peach actually started out in a White and Red dress with Red hair, that dress \n would later on be referenced by her fire flower dress. From Mario 2 onward peaches have been \n pink. In the Mario cartoons peach was a Redhead with a Pink dress, which seemed to be a \n combination of the two early designs. Peach wasn't always a damsel in distress, in 2005, peach \n got her own game. Super Princess Peach was a 2D puzzle platformer where you take control of \n Peach on a quest to save Mario, with her “Vibe Scepter”, that “Controls Her Emotions”. Yikes.")
    
    paraP.configure(bg="black",fg="white" )
    
    paraP.pack(padx=0, pady=0)
    
    
    #Add Timeline Image
    global peach_tl, new_peachtl
    
    peach_tl = Image.open("peachtl.png")

    resized = peach_tl.resize((960, 540), Image.ANTIALIAS)

    new_peachtl = ImageTk.PhotoImage(resized)

    peachtl_label = tk.Label(peach_window, image=new_peachtl)
    
    peachtl_label.place(x=0, y=310)
    
    peachtl_label.pack
    
    
    
#TOAD WINDOW----------------------------------------------------------------------------------------------------------

def open_toad_window():

    # Create the second window
    toad_window = tk.Toplevel()
    
    toad_window.title('Toad')
    
    toad_window.geometry("965x900")
    
    toad_window.configure(bg="black")


    # Add a label to the second window
    labelT = tk.Label(toad_window,font=(500), text='Everyones Favorite Bipedal Fungus!')
    
    labelT.pack(padx=35, pady=35)
    
    labelT.configure(bg="black",fg="white" )
    
    
    
    #Add the paragraph to the second window
    paraT = tk.Label(toad_window, text="Toad is Princess Peach's right hand man. Toad isn't just one person though. There are \n hundreds of toads that live in the Mushroom Kingdom. Toads can vary in color, from Pink, Tan, \n Green, Purple, Red, Blue, and Yellow. Few colors are significantly more prominent than others. \n Red toad is typically there to give information or to assist. While Yellow and Blue Toad are \n playable. Toad has been through very little design change, that being because he is without \n flaw. Captain Toad was first introduced in Super Mario Galaxy, where he was the leader of a \n group of toads called the Toad Brigade. Captain Toad, and the Toad Brigade travel around the \n galaxy. He was once again introduced in Super Mario 3D World, but this time, he's playable. \n You take control of Captain Toad and help him solve 3D block based puzzles. The only problem \n is that his backpack is too heavy, and he can't jump. People seemed to like theses puzzles so \n much, Captain Toad got his own game. Captain Toad: Treasure Tracker, came out on the Wii U \n in 2014. It was later ported to the 3Ds, and the Nintendo Switch.")
    
    paraT.configure(bg="black",fg="white" )
    
    paraT.pack(padx=0, pady=0)
    
    
    #Add Timeline Image
    global toad_tl, new_toadtl
    
    toad_tl = Image.open("toadtl.png")

    resized = toad_tl.resize((960, 540), Image.ANTIALIAS)

    new_toadtl = ImageTk.PhotoImage(resized)

    toadtl_label = tk.Label(toad_window, image=new_toadtl)
    
    toadtl_label.place(x=0, y=310)
    
    toadtl_label.pack
    
    
    
#MAIN MENU IMAGES----------------------------------------------------------------------------------------------------------

#Mario Image
mario_pic = Image.open("Mario.png")

resized = mario_pic.resize((300, 400), Image.ANTIALIAS)

new_mario = ImageTk.PhotoImage(resized)

alt="Mario Image"

# Image size
mario_label = tk.Label(window, image=new_mario)
mario_label.place(x=20, y=200)


#Luigi Image
luigi_pic = Image.open("Luigi.png")

resized = luigi_pic.resize((300, 400), Image.ANTIALIAS)

new_luigi = ImageTk.PhotoImage(resized)

alt="Luigi Image"

# Image size
luigi_label = tk.Label(window, image=new_luigi)
luigi_label.place(x=400, y=200)



#Peach Image
peach_pic = Image.open("Peach.png")

resized = peach_pic.resize((300, 400), Image.ANTIALIAS)

new_peach = ImageTk.PhotoImage(resized)

alt="Peach Image"

# Image size
peach_label = tk.Label(window, image=new_peach)
peach_label.place(x=800, y=200)



#Toad Image
toad_pic = Image.open("Toad.png")

resized = toad_pic.resize((300, 400), Image.ANTIALIAS)

new_toad = ImageTk.PhotoImage(resized)

alt="Toad Image"

# Image size
toad_label = tk.Label(window, image=new_toad)
toad_label.place(x=1200, y=200)

#MAIN MENU BUTTONS----------------------------------------------------------------------------------------------------------

#This is the Mario Button
buttonM = tk.Button(text="  Mario  ", command=open_mario_window)
buttonM.place(x=150, y=620)


#This is the Luigi Button
buttonL = tk.Button(text="  Luigi  ", command=open_luigi_window)
buttonL.place(x=530, y=620)


#This is the Peach Button
buttonP = tk.Button(text="  Peach  ", command=open_peach_window)
buttonP.place(x=920, y=620)


#This is the Toad Button
buttonT = tk.Button(text="  Toad  ", command=open_toad_window)
buttonT.place(x=1350, y=620)

#This is the Exit Button
buttonE = tk.Button(text="    Exit    ",bg="red",fg="white", command = close_window)
buttonE.place(x=730, y=700)

#-------------------------------------------------------------------------------------------------------------------------

window.mainloop()
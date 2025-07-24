import pygame
import os
pygame.init()
f = "assets/"
def load(file):
    return pygame.image.load(f + file).convert_alpha()
def loadaudio(file):
    return pygame.mixer.Sound(f+file)
def loadfont(file, size):
    lf = "assets/fonts/"
    return pygame.font.Font(lf + file, size)
wait = []
for i in os.listdir("assets/object/wait"):
    if i.endswith(".png"):
        wait.append(load("object/wait/" + i))
lang = {
    "en": {
        "play": "Play",
        "quit": "Quit",
        "lang": "English",
        "ein":"Press E to Interact",
        "garden": "Garden",
        "menu": "Menu",
        "cs":"Choose a save file",
        "sa":"Save As",
    },
    "trtr": {
        "play": "Oyna",
        "quit": "Çık",
        "lang": "Türkçe",
        "ein":"translation yok.",
        "garden": "Bahçe",
        "menu": "Menü",
        "cs":"Bir kayıt dosyası seçin",
        "sa":"Farklı Kaydet",
    }
    
}
arrow = load("object/"+"arrow.png")
arrow2 = pygame.transform.flip(arrow, True, False)
splashes = [
    "For the love of Python",
    "For the love of Pygame",
    "For the love of Programming",
    "For the love of Games",
    "For the love of Learning",
    "For the love of Fun",
    "For the love of ChatGPT",
    "For the love of Open Source",
    "i am a python",
    "i am a pygame",
    "i am a programmer",
    "i am a gamer",
    "i am a learner",
    "i am a fun",
    "i am a chatgpt",
    "i am an open source",
    "i am a pythonista",
    "I am f*cking awesome",
    "i am forcing my friends to play this",
    "i am forcing my friends to play this game",
    "40% of the code is written by ChatGPT",
    "60% of the code is written by me",
    "honk shooooo",
    "its 7:47 pm",
    "MacOS is the best OS",
    "GOOOOOOOBER",
    "i made this game in 2025",
    "This is the oven",
    "your mom is the oven",
    "YO G.C.",
    "bombardino crocadillo tung tung tung sahur trippi troppi tralalero tralalà",
    "WAFFLES AT 2 PM!!!",
    "its 5:00 pm",
    "hello you mother ducker",
    "hello you mother ducker, i am a python",
    "i am coding on a plane to london",
    "Merhaba, ben bir pythonum",
    "Merhaba, laundry! Oh sorry, i meant london",
    "a pigeon Shitted on my leg",
    "Double Bacon Cheeseburger",
    "i am a python, i am a pygame, i am a programmer, i am a gamer, i am a learner, i am a fun, i am a chatgpt, i am an open source, i am a pythonista",
    "AAAAAAAAAHAHHAHAAHHAHAHA",
    "AAAAAAAAAHAHHAHAAHHAHAHA, i am a python",
    "eeeeek",
    "eeeeek, i am a pygame",
    "whats up, i am a programmer",
    "Watch out for killed: 9! Its MacOS giving the middle finger 🖕 to your code!",
    "No bobbleheads were harmed in the making of this game",
    "This game is not sponsored by anyone",
    "No animals were harmed in the making of this game",
    "This game is not sponsored by anyone, i am a python",
    "KDOWJADIOHJAIOFHWIOIOH0OIˆØÓˆØÎÓ∑ÅˆØÎ˜ˆÍØÅÓÔ∑Øª",
    "uuuu",
    "dick in turkish is 'sik'",
    "R-rated!",
    "",
    "Fuck.",
    "geez",
    "im considering deleting Screen Time.app"
]

ph = load("object/"+"placeholder.png")
dev = load("object/"+"DEV.png")
garden = load("map/"+"garden.png")
quest1 = load("map/"+"quest1.png")
school = load("object/"+"school.png")
loa = load("object/"+"load.png")
loa = pygame.transform.scale(loa, (50,100))
loar = loa.get_rect()
sr = school.get_rect()
idiot = load("object/"+"idiot.png")
idiot2 = load("object/"+"idiot2.png")
player = load("object/"+"default.png")
title = load("object/"+"title.png")
menu = load("map/"+"menu.png")

pointers = loadaudio("music/"+"pointers.mp3")
ensure = loadaudio("pygame.mixer_ensurance.wav")
quest1a = loadaudio("music/"+"quest1.wav")
gardena = loadaudio("music/"+"garden.wav")
lycan = loadaudio("music/"+"lycanthropy.wav")
a1 = loadaudio("music/"+"1_a.ogg")
b1 = loadaudio("music/"+"1_b.ogg")
bb2 = loadaudio("music/"+"2_bb.ogg")

dots = loadfont("dots.ttf", 20)
gi = loadfont("gi.ttf", 20)
gr = loadfont("gr.ttf", 20)
wingding = loadfont("wingding.ttf", 20)
messedup = loadfont("messed_up.ttf", 20)
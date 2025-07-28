import pygame
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
import os,sys,pickle,subprocess,time,random,math
import threading as th
import appletalk.Finder as fi
import appletalk.display as d
import platform as p

level = "menu"
ismovinglevel = True
lang = "en"
def animate(folder, speed, ):
    items = os.listdir(folder)
def code():
    codee = d.display_text_input("Enter Code")
    out = subprocess.run(
        ["python3", "-c", str(codee)],
        capture_output=True,
    )
    print(out.stdout, out.stderr, out.returncode)
def dirname():
    if getattr(sys, 'frozen', False):
        # If the application is frozen (e.g., PyInstaller)
        return os.path.dirname(sys.executable)
    else:
        # If the application is not frozen (e.g., running from source)
        return os.path.dirname(os.path.abspath(__file__))

os.chdir(dirname())
try:
    import assets as a # has pygame.init()
except pygame.error as e:
    print("Error loading assets:", e)
    print("Make sure the 'assets' directory exists and contains the required files.")
    print("or your display is f*cked")
    sys.exit(1)
bg = a.menu
savemi = False
def savecore():
        with open("core.binsave", "wb") as f:
            pickle.dump({"lang":lang}, f)
def savesave(save):
    with open(save, "wb") as f:
        pickle.dump({"level":level, "px":px, "py":py}, f)
        
def loadcore():
    global lang
    try:
        with open("core.binsave", "rb") as f:
            data = pickle.load(f)
            print(f.read())
            lang = data["lang"]
    except:
        with open("core.binsave", "wb") as f:
            pickle.dump({"lang":lang}, f)

clock = pygame.time.Clock()
px = py = 0
pr = a.player.get_rect()
pygame.display.set_icon(a.dev)
#wing = a.wingding.render("hello you mother ducker", True, (255, 255, 255))
#screen.blit(wing, (0, 0))
#pygame.display.flip()
#time.sleep(10)
pygame.mixer.music.load(os.path.join("assets", "music", "2_bb.ogg"))
pygame.mixer.music.play(-1)  # Loop the music indefinitely
levelbounds = (0,0)
posc = [0,0]
play:pygame.Rect
arrowr = a.arrow.get_rect()
arrowr2 = a.arrow2.get_rect()

def draw():
    global play,bg,ismovinglevel,levelbounds, px,py
    size = pygame.display.get_window_size()
    sc = pygame.Rect(pr.x,pr.y,size[0], size[1])
    play = pygame.Rect(size[0]/2, size[1]/2, 100, 50)
    screen.fill((0, 0, 0))
    a.loar.x = round(size[0] / 2 + 200)
    a.loar.y = size[1] - 300
    
    if level == "menu":
        screen.blit(bg, (0, 0))
        ismovinglevel = False
        arrowr2.x = size[0] - 300
        arrowr2.y = size[1] - 100
        arrowr.x = arrowr2.x - 170
        arrowr.y = size[1] - 100
        bg = a.menu
        bg = pygame.transform.scale(bg, size)
        screen.blit(splash, (size[0]/2-100, size[1]/2 - 100))
        pygame.draw.rect(screen, "blue", play)
        screen.blit(playt, (play.x + 10, play.y + 10))
        screen.blit(a.title, (size[0]/2 - 300, size[1]/2 - 300))
        screen.blit(langtext, (size[0] - 400, size[1] - 50))
        screen.blit(a.arrow, (arrowr.x, arrowr.y))
        screen.blit(a.arrow2, (arrowr2.x, arrowr2.y))
        screen.blit(a.loa, (a.loar.x, a.loar.y))
    if level == "garden":
        bg = a.garden
        bg = pygame.transform.scale(bg, (1000,900))
        garden.blit(bg, (0, 0))
        screen.blit(garden, (0,0), sc)
        ismovinglevel = True

    if ismovinglevel:
        px = pr.x
        py = pr.y
        screen.blit(a.player, (px,py))


fonts = [
    a.dots, a.gi, a.wingding, a.gr, 
]
garden = pygame.Surface((1000, 900), pygame.SRCALPHA)
splash_text = random.choice(a.splashes)
splash = random.choice(fonts).render(splash_text, True, "yellow")

#saveth = th.Thread(None, savecore)
#saveth.run()
running = True
loadcore()
langtext = a.dots.render(a.lang[lang]["lang"], True, "green")
pygame.display.set_caption(a.lang[lang]["menu"])
while running:

    #st = th.Timer(5, savecore).start()  # Save core every 5 seconds
    playt = a.dots.render(a.lang[lang]["play"], True, "white")
    draw()
    #for i in a.wait:
    #    screen.blit(i, (0, 0))
    #    pygame.display.flip()
    #    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                # Example action on space key press
                print("Space key pressed")
            # move
            if ismovinglevel:
                if event.key == pygame.K_w:
                    posc[1] = -5
                elif event.key == pygame.K_s:
                    posc[1] = 5
                elif event.key == pygame.K_d:
                    posc[0] = 5
                elif event.key == pygame.K_a:
                    posc[0] = -5

        elif event.type == pygame.KEYUP:
            posc = [0,0]

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if play.collidepoint(event.pos) and level == "menu":
                    print("Play button clicked")
                    if not savemi:
                        file = fi.save_file(a.lang[lang]["sa"], "save.binsave")
                    level = "garden"
                    pygame.mixer.music.stop()
                    pygame.display.set_caption(a.lang[lang]["garden"])
                    pygame.mixer.music.load(os.path.join("assets", "music", "garden.wav"))
                    pygame.mixer.music.play(-1)
                if arrowr.collidepoint(event.pos) and level == "menu":
                    print("Arrow left clicked")
                    lang = "en" if lang == "trtr" else "trtr"
                    langtext = a.dots.render(a.lang[lang]["lang"], True, "green")
                    savecore()
                if arrowr2.collidepoint(event.pos) and level == "menu":
                    print("Arrow right clicked")
                    lang = "en" if lang == "trtr" else "trtr"
                    langtext = a.dots.render(a.lang[lang]["lang"], True, "green")
                    savecore()
                if a.loar.collidepoint(event.pos) and level == "menu":
                    if not savemi:
                        file = fi.open_file(a.lang[lang]["cs"])
                        print(file)
                        try:
                            with open(file, "rb") as f:
                                data = pickle.load(f)
                                level = data["level"]
                                px = data["px"]
                                py = data["py"]
                                pr.x = px
                                pr.y = py
                        except Exception as e:
                            print("Error loading save:", e)
                            level = "menu"
    # restrict movement to level bounds
    if ismovinglevel:
        pr.x = max(0, min(pr.x, 1000 - pr.width))
        pr.y = max(0, min(pr.y, 900 - pr.height))
        pr.x += posc[0]
        pr.y += posc[1]
    #posc = [0,0]
    pygame.display.flip()
    clock.tick(60)
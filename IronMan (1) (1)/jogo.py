import pygame
pygame.init()
import time
import random

################ Variáveis Globais ################
display_width = 1000
display_height = 520
gameDisplay=pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)

ironManImg = pygame.image.load('assets/ironLarge.png')
missile = pygame.image.load('assets/missile.png')

gameIcon = pygame.image.load('assets/ironIcon.png')
pygame.display.set_icon(gameIcon)
pygame.display.set_caption('Iron Man - Marcão')

bg = pygame.image.load("assets/fundo.jpg")
explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
missileSound = pygame.mixer.Sound("assets/missile.wav")


################ Funções Controladoras ################
def mostraIron(x,y):
    gameDisplay.blit(ironManImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def dead():
    pygame.mixer.Sound.play(explosaoSound)
    pygame.mixer.music.stop()
    message_display('Você Morreu')

def mostraArmas(posicaoX, posicaoY):
    gameDisplay.blit(missile,(posicaoX, posicaoY))

def escrevendoPlacar(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Desvios: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))


################ Looping do Jogo ################
def game_loop():
    pygame.mixer.music.load('assets/ironsound.mp3')
    pygame.mixer.music.play(-1)

    ironPosicaoX = (display_width * 0.45)
    ironPosicaoY = (display_height * 0.8)
    iron_width = 120
    movimentoX = 0 
    missileX = random.randrange(0, display_width)
    missileY = -600
    missileHeight = 250
    missileWidht = 50
    missileXSpped = 7
    desvios =0 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoX = -5
                elif event.key == pygame.K_RIGHT:
                    movimentoX = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    movimentoX = 0
        ironPosicaoX += movimentoX

        if ironPosicaoX > display_width - iron_width or ironPosicaoX < 0:
            #quit()
            dead()

        gameDisplay.fill(white)
        gameDisplay.blit(bg, (0,0))
        mostraIron(ironPosicaoX,ironPosicaoY)
        escrevendoPlacar(desvios)

        mostraArmas(missileX, missileY)
        missileY += missileXSpped

        if missileY > display_height:
            pygame.mixer.Sound.play(missileSound)
            missileY = 0 - missileHeight
            missileX = random.randrange(0, display_width)
            missileXSpped+=1
            desvios += 1


        if ironPosicaoY < missileY + missileHeight:
            #print("Analisando Colisão")
            #print(ironPosicaoX, ironPosicaoX+iron_width)
            #print(missileX, missileX+missileWidht)
            if ironPosicaoX < missileX and ironPosicaoX+iron_width > missileX or missileX+missileWidht > ironPosicaoX and missileX+missileWidht < ironPosicaoX+iron_width:
                dead()


        pygame.display.update()
        clock.tick(60)


game_loop()
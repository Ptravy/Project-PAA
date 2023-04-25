import pygame
import random
import sys
from pygame.locals import *

pygame.init()

white = (255,255,255)
black = (0,0,0)
bg = black
red = (175,0,0)
fps = 30
dispWidth = 800
dispHeight = 600
cellSize = 50

UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

deadZones = []

def maketextObjs(text,font,tcolor):
    textSurface = font.render(text,True,tcolor)
    return textSurface,textSurface.get_rect()

def whatNext():
    for event in pygame.event.get([KEYDOWN,KEYUP,QUIT]):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            continue
        return event.key
    return None

            

def msgSurface(text,textColor):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    largeText = pygame.font.Font('freesansbold.ttf',150)
    titleTextSurf,titleTextRect = maketextObjs(text,largeText,textColor)
    titleTextRect.center = (int(dispWidth/2),int(dispHeight/2))
    setDisplay.blit(titleTextSurf,titleTextRect)
    typTextSurf,typTextRect = maketextObjs('Press key To continue',smallText,white)
    typTextRect.center = (int(dispWidth/2),int(dispHeight/2)+120)
    setDisplay.blit(typTextSurf,typTextRect)
    pygame.display.update()
    fpsTime.tick()
    while whatNext()==None:
        for event in pygame.event.get([QUIT]):
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsTime.tick()
    runGame()

def evilMove(evilCoords):
    evilCoord = []
    randomx = random.randrange(-1,2)
    randomy = random.randrange(-1,2)
    newCell = {'x':evilCoords[0]['x']+randomx,'y':evilCoords[0]['y']+randomy}
    if(newCell['x']<0 or newCell['y']<0 or newCell['x']>dispWidth/cellSize or newCell['y']>dispHeight/cellSize):
        newCell = {'x': dispWidth/(2*cellSize) ,'y': dispHeight/(2*cellSize)}
    del evilCoords[-1]
    evilCoord.append(newCell['x'])
    evilCoord.append(newCell['y'])
    deadZones.append(evilCoord)
    evilCoords.insert(0,newCell)

def runGame():
    global deadZones
    startx = 3
    starty = 3
    isAlive = 'yes'
    coords = [{'x' : startx , 'y' : starty}]
    evilCoords1 = [{'x': dispWidth/(2*cellSize) ,'y': dispHeight/(2*cellSize)}]
    evilCoords2 = [{'x': dispWidth/(2*cellSize) ,'y': dispHeight/(2*cellSize)}]
    evilCoords3 = [{'x': dispWidth/(2*cellSize) ,'y': dispHeight/(2*cellSize)}]
    evilCoords4 = [{'x': dispWidth/(2*cellSize) ,'y': dispHeight/(2*cellSize)}]
    evilCoords5 = [{'x': dispWidth/(2*cellSize) ,'y': dispHeight/(2*cellSize)}]
    evilCoords6 = [{'x': dispWidth/(2*cellSize) ,'y': dispHeight/(2*cellSize)}]
    evilCoords7 = [{'x': dispWidth/(2*cellSize) ,'y': dispHeight/(2*cellSize)}]
    evilCoords8 = [{'x': dispWidth/(2*cellSize) ,'y': dispHeight/(2*cellSize)}]
    direction = RIGHT

    while True:
        while isAlive == 'yes':
            deadZones = []
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        direction = LEFT
                    elif event.key == K_RIGHT:
                        direction = RIGHT
                    elif event.key == K_DOWN:
                        direction = DOWN
                    elif event.key == K_UP:
                        direction = UP
                if direction == UP:
                    newCell = {'x':coords[0]['x'] , 'y':coords[0]['y']-1}

                elif direction == DOWN:
                    newCell = {'x':coords[0]['x'] , 'y':coords[0]['y']+1}

                elif direction == LEFT:
                    newCell = {'x':coords[0]['x']-1 , 'y':coords[0]['y']}

                elif direction == RIGHT:
                    newCell = {'x':coords[0]['x']+1 , 'y':coords[0]['y']}

                del coords[-1]
                coords.insert(0,newCell)
                setDisplay.fill(bg)
                evilMove(evilCoords1)
                evilMove(evilCoords2)
                evilMove(evilCoords3)
                evilMove(evilCoords4)
                evilMove(evilCoords5)
                evilMove(evilCoords6)
                evilMove(evilCoords7)
                evilMove(evilCoords8)
                drawCell(coords,white)
                drawCell(evilCoords1,red)
                drawCell(evilCoords2,red)
                drawCell(evilCoords3,red)
                drawCell(evilCoords4,red)
                drawCell(evilCoords5,red)
                drawCell(evilCoords6,red)
                drawCell(evilCoords7,red)
                drawCell(evilCoords8,red)

                currentPos = [newCell['x'],newCell['y']]
                for eachDeadCoord in deadZones:
                    if eachDeadCoord == currentPos:
                        isAlive = 'no'
                
                pygame.display.update()
                fpsTime.tick(fps)

                if(newCell['x']<0 or newCell['y']<0 or newCell['x']>dispWidth/cellSize or newCell['y']>dispHeight/cellSize):
                    isAlive = 'no'
        msgSurface('You Died!',red)
        
def drawCell(coords,cColor):
        for coords in coords:
            x = coords['x']*cellSize
            y = coords['y']*cellSize
            makeCell = pygame.Rect(x,y,cellSize,cellSize)
            pygame.draw.rect(setDisplay,cColor,makeCell)

while True:
        global fpsTime
        global setDisplay

        fpsTime = pygame.time.Clock()
        setDisplay = pygame.display.set_mode((dispWidth,dispHeight))
        pygame.display.set_caption('Controlling')
        runGame()
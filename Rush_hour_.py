import pygame
import time

pygame.init()

#var

display_width = 800
display_height = 600
# Ok - first you calculate a few things (Aspect Ratio)
car_y = display_height /8
car_y = display_height - car_y * 2
# This'll place it close to the bottom of the screen, in ratio with the Display Height
print(car_y)

#colors

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

car_width = 75

#display

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Rush Hour')
clock = pygame.time.Clock()

backImg = pygame.image.load('straight.png')
carImg = pygame.image.load('blue-car-top-view-90-md.png')
carImg = pygame.transform.scale(carImg, (75, 150))
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_object(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Suck!')

def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    car(200,200)

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                    

        x += x_change
                    
        gameDisplay.fill(white)
        car(x,car_y)

        if x > display_width - car_width or x < 0:
            crash()

        
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()




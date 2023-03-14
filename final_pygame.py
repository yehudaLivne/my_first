import pygame
import random
from shapes import Ball

WINDOW_WIDTH = 500
WINDOW_HIEGHT = 500
screen_size = (WINDOW_WIDTH,WINDOW_HIEGHT)
NUMBER_OF_PLAINS = 4
BACKGROUND_IMAGE = 'imagepuma.jpg'
REFRESH_RATE = 100
BALL_SIZE = 40
turns = 0
contis = 0


img = pygame.image.load(BACKGROUND_IMAGE)
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Game")
screen.blit(img, (0, 0))
clock = pygame.time.Clock()

x_locations=[]
y_locations=[]
for x in range(11):
        x_locations.append(5+40*x)
for y in range(11):
       y_locations.append(5+40*y)

plains_list = pygame.sprite.Group()
for i in range(NUMBER_OF_PLAINS):
    x,y = random.randint(0,10), random.randint(0,10)
    x,y = x_locations[x],y_locations[y]
    plane = Ball(x,y)
    plains_list.add(plane)


new_balls_list = pygame.sprite.Group()

notRAN =False
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    fobidden_list = [0, 0, 0, 0]
    ii = 0
    for plane in plains_list:
        new_balls_list.empty()
        for plane in plains_list:
            a ,b = plane.get_pos()
            ball = Ball(a,b)
            new_balls_list.add(ball)
        danger_level = 0
        notRAN = False  # print(danger_level)

        for ball in new_balls_list:
            for i in range(100):
                x, y = ball.get_pos()
                new_move = random.randint(1, 4)
                if new_move == 4 and x < 450:
                    ball.rect.x = x + 50
                elif new_move == 1 and x > 50:
                    ball.rect.x = x - 50
                elif new_move == 2 and y > 50:
                    ball.rect.y = y - 50
                elif new_move == 3 and y < 450:
                    ball.rect.y = y + 50
                for ball in new_balls_list:
                    balls_hit_list = pygame.sprite.spritecollide(ball, new_balls_list, False)
                    if len(balls_hit_list) > 1:

                        movemove = new_move
                        if not (movemove in fobidden_list):
                            fobidden_list[ii] = movemove
                            ii += 1
                        danger_level += 1
        if danger_level > 5:
            contis +=1
            notRAN = True

        x, y = plane.get_pos()
        #print('xxx {} yyy {}'.format(x,y))

        new_move = random.randint(1,4)
        if notRAN:
            new_move = 10 - sum(fobidden_list)
            if new_move > 6:
                new_move = 4
            elif new_move == 6:
                new_move = 2
            elif new_move == 5:
                if 4 in fobidden_list:
                    new_move = 3
                else:
                    new_move = 4

        if new_move == 4 and x<450:
            plane.rect.x = x + 50
        elif new_move == 1 and x>50:
            plane.rect.x = x - 50
        elif new_move == 2 and y>50:
            plane.rect.y = y - 50
        elif new_move == 3 and y < 450:
            plane.rect.y = y + 50
    for plane in plains_list:
        balls_hit_list = pygame.sprite.spritecollide(plane, plains_list, False)
        if len(balls_hit_list) > 1:
            finish = True
    screen.blit(img, (0, 0))
    plains_list.draw(screen)
    pygame.display.flip()
    turns  += 1
    if turns == 1000:
        finish = True
#    print(turns)
    clock.tick(REFRESH_RATE)
print(turns)
print(contis)
pygame.quit()



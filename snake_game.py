import pygame
import sys
import random

#print("_____________  YILAN OYUNU  _____________")

#anaconda cmd.exe prompt 
#1-)conda activate myenv
#2-)conda remove pygame
#2-)conda install -c cogsci pygame
#4-)python snake_game.py




#ekran boyutlarr
Width,Height = 700, 700 #default 400 400

#renkler
Black = (0,0,0)
White  = (255,255,255)
Red = (255,0,0)

class Snake:
    def __init__(self):
        self.body=[(100,50),(90,50),(80,50)]
        self.direction = "Right"
    
    def move(self, food_pos):
        if self.direction == "Right":
            new_head = (self.body[0][0] + 10, self.body[0][1])
        if self.direction == "Left":
            new_head = (self.body[0][0] - 10, self.body[0][1])
        if self.direction =="Up":
            new_head = (self.body[0][0] , self.body[0][1] - 10)
        if self.direction =="Down":
            new_head = (self.body[0][0] , self.body[0][1] + 10)
        self.body.insert(0,new_head)

        if self.body[0] == food_pos:
            return True
        else:
            self.body.pop()
            return False
    
    
    def change_direction(self, new_direction):
        if new_direction == "Right" and not self.direction == "Left":
            self.direction = "Right"
        if new_direction == "Left" and not self.direction == "Right":
            self.direction = "Left"
        if new_direction == "Up" and not self.direction == "Down":
            self.direction = "Up"
        if new_direction == "Down" and not self.direction == "Up":
            self.direction = "Down"
        
    def check_collision(self):
        if self.body[0][0] >= Width or self.body[0][0] <= 0:
            return True
        if self.body[0][1] >= Height or self.body[0][1] <= 0:
            return True
        
        for segment in self.body[1:]:
            if self.body[0] == segment:
                return True
        return False
    
class Food:
    def __init__(self):
        self.position=(random.randrange(1,(Width//10)) * 10 , random.randrange(1, Height // 10) * 10) 
        self.is_food_on_screen = True
    
    def spawner_food(self):
        if not self.is_food_on_screen:
            self.position = (random.randrange(1,(Width//10)) * 10, random.randrange(1, Height // 10) * 10)
            self.is_food_on_screen = True
        return self.position

    def set_food_on_screen(self,choice):
        self.is_food_on_screen = choice

def main():
    pygame.init()
    screen = pygame.display.set_mode((Width,Height))
    pygame.display.set_caption("__SNAKE GAME__")

    snake = Snake()
    food = Food()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("Up")
                if event.key == pygame.K_DOWN:
                    snake.change_direction("Down")
                if event.key == pygame.K_LEFT:
                    snake.change_direction("Left")
                if event.key == pygame.K_RIGHT:
                    snake.change_direction("Right")
        
        food_position = food.spawner_food()
        if snake.move(food_position):
            food.set_food_on_screen(False)

        if snake.check_collision():
            break
        
        screen.fill(Black)

        for pos in snake.body:
            pygame.draw.rect(screen, White,pygame.Rect(pos[0],pos[1],10,10))

        pygame.draw.rect(screen,Red,pygame.Rect(food.position[0],food.position[1],10,10))
        pygame.display.update()
        clock.tick(10) 


if __name__ == "__main__":
    main()
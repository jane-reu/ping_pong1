from pygame import *

colour = (200, 200, 200)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(colour)

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed, width, height):
        self.image = transform.scale(image.load(player_image),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.rect.width = width
        self.rect.height = height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed


MOVE_LEFT_RIGHT = False
game = True
finish = False
clock = time.Clock()
FPS = 60

fence_l = Player("fence.png", 30, 200, 4, 50, 150)
fence_r = Player("fence.png", 520, 200, 4, 50, 150)
ball = GameSprite("ball.png", 200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(colour)
        fence_l.update_l()
        fence_r.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        fence_l.reset()
        fence_r.reset()
        ball.reset()
        if ball.RECT.colliderect(fence_r.RECT):
            MOVE_LEFT_RIGHT = True
        if ball.X > win_width - ball.HEIGHT:
                text = pygame.font.Font(path_font, 50)
                text1 = text.render("You Lose", True, (255,0,0))
                window.blit(text1, (win_width / 2 - 50, win_height /2))
                ball.SPEED = 0
                ball.SPEED_X = 0

  




    display.update()
    clock.tick(FPS)
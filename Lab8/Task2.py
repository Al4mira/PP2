import pygame
import random

pygame.init()



W, H = 1200, 650
FPS = 60

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# paddle
paddleW = 300  # 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


# Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(3)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
              for i in range(10) for j in range(4)]
# random number of unbreakable bricks 3-7
unbreakable_bricks_count = random.randrange(3, 8)
# random number of bonus bricks less or equal 6
bonus_bricks_count = random.randrange(1, 6)
# 0 - breakable, 1 - unbreakable, 2 - bonus
type_list = [1] * unbreakable_bricks_count + [2] * bonus_bricks_count + [0] * (
        len(block_list) - unbreakable_bricks_count - bonus_bricks_count)
random.shuffle(type_list)

unbreakable_bricks_indices = [i for i, brick_type in enumerate(type_list) if brick_type == 1]

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Adding an event to increase speed (every 3 seconds)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 3000)
# Adding an event to shrink paddle (every 5 seconds)
SHRINK_PADDLE = pygame.USEREVENT + 2
pygame.time.set_timer(SHRINK_PADDLE, 5000)

while not done:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            ballSpeed += 0.5
            # print(ballSpeed)
        if event.type == SHRINK_PADDLE:
            paddleW -= 20
            paddle.width = paddleW
            # print(paddleW)
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)

    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]

    pygame.draw.rect(screen, pygame.Color('blue'), paddle)
    pygame.draw.circle(screen, pygame.Color('red'), ball.center, ballRadius)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if keys[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    ball.x += dx * ballSpeed
    ball.y += dy * ballSpeed

    if ball.left < 0 or ball.right > W:
        dx = -dx
    if ball.top < 0:
        dy = -dy

    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)
        collision_sound.play()

    hit_index = ball.collidelist(block_list)

    if hit_index != -1:
        if type_list[hit_index] == 0 or type_list[hit_index] == 2:
            hit_rect = block_list.pop(hit_index)
            hit_color = color_list.pop(hit_index)
            dx, dy = detect_collision(dx, dy, ball, hit_rect)
            if type_list[hit_index] == 0:
                game_score += 1
            elif type_list[hit_index] == 2:
                if game_score > 0:
                    game_score = game_score * 2
                else:
                    game_score += 5
        else:
            type_list[hit_index] = 0
            hit_rect = block_list[hit_index]
            dx, dy = detect_collision(dx, dy, ball, hit_rect)
        collision_sound.play()

        if hit_index in unbreakable_bricks_indices:
            unbreakable_bricks_indices.remove(hit_index)

    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))

    if ball.bottom > H:
        screen.fill(bg)
        screen.blit(losetext, losetextRect)
        pygame.display.flip()
        pygame.time.wait(2000)
        done = True

    if len(block_list) == 0:
        screen.fill(bg)
        screen.blit(wintext, wintextRect)
        pygame.display.flip()
        pygame.time.wait(2000)
        done = True

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
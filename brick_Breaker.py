import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BALL_RADIUS = 10
MINI_BALL_RADIUS = 5
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
FPS = 60
POWERUP_SIZE = 20
PAUSE_TIME = 5  # Seconds for level start pause
SLOW_FALL_SPEED = 2  # Ball slow fall speed when getting extra life

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # HP 1
ORANGE = (255, 165, 0)  # HP 2
PURPLE = (160, 32, 240)  # HP 3
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker")

font = pygame.font.Font(None, 36)

# Powerups
powerup_types = ['expand', 'speed', 'extra_life', 'paddle_speed']

# Game Variables
levels = 3
current_level = 1
score = 0
lives = 3
score_milestone = 100
powerups = []
mini_balls = []
multi_balls = []  # Balls shot out on hitting 100 points


def draw_text(text, x, y, color=WHITE):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))


def create_bricks(level):
    """Create bricks with different health levels."""
    bricks = []
    rows = 5 + level  # Increase rows with each level
    for i in range(rows):
        for j in range(10):
            hp = random.randint(1, 3)  # Randomly assign brick HP between 1 and 3
            brick = pygame.Rect(j * (BRICK_WIDTH + 5) + 35, i * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
            bricks.append({'rect': brick, 'hp': hp})  # Store brick as dict with rect and hp
    return bricks


def spawn_mini_balls(ball):
    """Spawn 5 miniature balls in random directions."""
    mini_balls = []
    for _ in range(5):
        angle = random.uniform(-1, 1)  # Random angle between -1 and 1
        mini_speed_x = random.choice([-3, 3]) * angle
        mini_speed_y = random.choice([-3, 3]) * (1 - abs(angle))
        mini_ball = {
            'rect': pygame.Rect(ball.x, ball.y, MINI_BALL_RADIUS * 2, MINI_BALL_RADIUS * 2),
            'speed': [mini_speed_x, mini_speed_y]
        }
        mini_balls.append(mini_ball)
    return mini_balls


def shoot_multi_balls(paddle):
    """Shoot multiple balls from the paddle."""
    balls = []
    for _ in range(5):
        angle = random.uniform(-1, 1)
        speed_x = random.choice([-3, 3]) * angle
        speed_y = -5
        ball = pygame.Rect(paddle.centerx, paddle.top - BALL_RADIUS * 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
        balls.append({'rect': ball, 'speed': [speed_x, speed_y]})
    return balls


def random_powerup(paddle, ball_speed):
    """Randomly choose a power-up effect."""
    powerup_type = random.choice(powerup_types)
    if powerup_type == 'expand':
        paddle.width = min(paddle.width + 50, SCREEN_WIDTH)
    elif powerup_type == 'speed':
        ball_speed[0] *= 1.2
        ball_speed[1] *= 1.2
    elif powerup_type == 'extra_life':
        global lives
        lives += 1
    elif powerup_type == 'paddle_speed':
        return 2  # Return extra paddle speed
    return 0  # No change in paddle speed


def game(level):
    global score, lives, score_milestone, mini_balls, multi_balls

    paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
    main_ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
    ball_speed = [random.choice([-4, 4]), -4]
    bricks = create_bricks(level)
    powerups.clear()
    mini_balls.clear()
    multi_balls.clear()

    clock = pygame.time.Clock()
    running = True
    paddle_speed = 5
    slow_fall = False
    first_hit = False

    # Pause for 5 seconds before starting a new level
    screen.fill(BLACK)
    draw_text(f"Level {level} starting in...", SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2)
    pygame.display.flip()
    time.sleep(PAUSE_TIME)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
            paddle.x += paddle_speed

        # Move the main ball
        if slow_fall:
            main_ball.y += SLOW_FALL_SPEED  # Slow fall when gaining a new life
        else:
            main_ball.x += ball_speed[0]
            main_ball.y += ball_speed[1]

        # Ball collision with walls
        if main_ball.left <= 0 or main_ball.right >= SCREEN_WIDTH:
            ball_speed[0] = -ball_speed[0]
        if main_ball.top <= 0:
            ball_speed[1] = -ball_speed[1]
        if main_ball.bottom >= SCREEN_HEIGHT:
            lives -= 1
            if lives == 0:
                return False  # Game over if no more lives
            else:
                main_ball.x, main_ball.y = SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2  # Reset ball position
                slow_fall = True  # Slow ball fall for new life

        # Ball collision with paddle
        if main_ball.colliderect(paddle):
            ball_speed[1] = -ball_speed[1]
            main_ball.y = paddle.top - BALL_RADIUS * 2
            if slow_fall:
                slow_fall = False  # Resume normal speed after first hit

        # Ball collision with bricks
        for brick in bricks[:]:
            if main_ball.colliderect(brick['rect']):
                ball_speed[1] = -ball_speed[1]
                brick['hp'] -= 1
                score += 10  # Increment score for each hit
                if brick['hp'] <= 0:
                    bricks.remove(brick)

                    # Randomly spawn power-ups
                    if random.random() < 0.1:  # 10% chance of power-up
                        powerup_type = random.choice(powerup_types)
                        powerup_rect = pygame.Rect(brick['rect'].x, brick['rect'].y, POWERUP_SIZE, POWERUP_SIZE)
                        powerups.append((powerup_type, powerup_rect))

        # Spawn power-up and mini balls after every 100 points
        if score >= score_milestone:
            score_milestone += 100  # Update the next milestone
            mini_balls.extend(spawn_mini_balls(main_ball))  # Add mini balls to the game
            paddle_speed += random_powerup(paddle, ball_speed)  # Random power-up
            multi_balls.extend(shoot_multi_balls(paddle))  # Shoot multiple balls from the paddle

        # Handle powerups
        for powerup in powerups[:]:
            powerup_type, powerup_rect = powerup
            powerup_rect.y += 5

            if powerup_rect.colliderect(paddle):
                if powerup_type == 'expand':
                    paddle.width = min(paddle.width + 50, SCREEN_WIDTH)
                elif powerup_type == 'speed':
                    ball_speed[0] *= 1.2
                    ball_speed[1] *= 1.2
                elif powerup_type == 'extra_life':
                    lives += 1
                elif powerup_type == 'paddle_speed':
                    paddle_speed += 2
                powerups.remove(powerup)

            if powerup_rect.top > SCREEN_HEIGHT:
                powerups.remove(powerup)

        # Miniature ball movement
        for mini_ball in mini_balls[:]:
            mini_ball['rect'].x += mini_ball['speed'][0]
            mini_ball['rect'].y += mini_ball['speed'][1]

            # Remove miniature balls when they hit the top or a brick
            if mini_ball['rect'].top <= 0:
                mini_balls.remove(mini_ball)
            for brick in bricks[:]:
                if mini_ball['rect'].colliderect(brick['rect']):
                    mini_balls.remove(mini_ball)
                    brick['hp'] -= 1
                    if brick['hp'] <= 0:
                        bricks.remove(brick)
                    break

        # Multi-ball movement (balls shot out every 100 points)
        for ball in multi_balls[:]:
            ball['rect'].x += ball['speed'][0]
            ball['rect'].y += ball['speed'][1]
            if ball['rect'].top <= 0 or ball['rect'].colliderect(paddle):
                multi_balls.remove(ball)
            for brick in bricks[:]:
                if ball['rect'].colliderect(brick['rect']):
                    multi_balls.remove(ball)
                    brick['hp'] -= 1
                    if brick['hp'] <= 0:
                        bricks.remove(brick)
                    break

        # Win condition (all bricks destroyed)
        if not bricks:
            return True  # Proceed to the next level

        # Drawing
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, paddle)
        pygame.draw.ellipse(screen, BLUE, main_ball)  # Use main_ball for drawing

        # Draw bricks with different colors based on their HP
        for brick in bricks:
            if brick['hp'] == 1:
                color = RED
            elif brick['hp'] == 2:
                color = ORANGE
            elif brick['hp'] == 3:
                color = PURPLE
            pygame.draw.rect(screen, color, brick['rect'])

        # Draw power-ups
        for powerup_type, powerup_rect in powerups:
            if powerup_type == 'expand':
                pygame.draw.rect(screen, GREEN, powerup_rect)
            elif powerup_type == 'speed':
                pygame.draw.rect(screen, YELLOW, powerup_rect)
            elif powerup_type == 'extra_life':
                pygame.draw.rect(screen, BLUE, powerup_rect)
            elif powerup_type == 'paddle_speed':
                pygame.draw.rect(screen, PURPLE, powerup_rect)

        # Draw mini balls
        for mini_ball in mini_balls:
            pygame.draw.ellipse(screen, YELLOW, mini_ball['rect'])

        # Draw multi balls
        for ball in multi_balls:
            pygame.draw.ellipse(screen, ORANGE, ball['rect'])

        draw_text(f"Score: {score}", 10, 10)
        draw_text(f"Level: {level}", SCREEN_WIDTH - 100, 10)
        draw_text(f"Lives: {lives}", SCREEN_WIDTH // 2 - 50, 10)

        pygame.display.flip()
        clock.tick(FPS)


def game_loop():
    global current_level, lives

    while current_level <= levels:
        if game(current_level):
            current_level += 1
        else:
            draw_text("Game Over", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)
            pygame.display.flip()
            pygame.time.delay(2000)
            current_level = 1
            lives = 3  # Reset lives
            return

    draw_text("You Win!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)
    pygame.display.flip()
    pygame.time.delay(2000)


if __name__ == "__main__":
    game_loop()
    pygame.quit()

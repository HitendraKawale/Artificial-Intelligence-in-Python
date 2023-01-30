import pygame

# Initialize Pygame
pygame.init()

# Set screen size
screen_size = (500, 500)
screen = pygame.display.set_mode(screen_size)

# Set paddle size and initial position
paddle_size = (20, 100)
paddle_pos = [(screen_size[0] - paddle_size[0]) / 2, (screen_size[1] - paddle_size[1]) / 2]

# Set ball size and initial position
ball_size = (20, 20)
ball_pos = [(screen_size[0] - ball_size[0]) / 2, (screen_size[1] - ball_size[1]) / 2]

# Set ball speed
ball_speed = [3, 3]

# Set AI speed
ai_speed = 5

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the AI paddle
    if paddle_pos[1] + paddle_size[1] / 2 < ball_pos[1]:
        paddle_pos[1] += ai_speed
    elif paddle_pos[1] + paddle_size[1] / 2 > ball_pos[1]:
        paddle_pos[1] -= ai_speed

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Check for ball collision with walls
    if ball_pos[0] <= 0 or ball_pos[0] + ball_size[0] >= screen_size[0]:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= 0 or ball_pos[1] + ball_size[1] >= screen_size[1]:
        ball_speed[1] = -ball_speed[1]

    # Check for ball collision with paddle
    if (ball_pos[0] <= paddle_pos[0] + paddle_size[0] and
            ball_pos[1] >= paddle_pos[1] and
            ball_pos[1] <= paddle_pos[1] + paddle_size[1]):
        ball_speed[0] = -ball_speed[0]

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the paddle
    pygame.draw.rect(screen, (255, 255, 255), (paddle_pos[0], paddle_pos[1], paddle_size[0], paddle_size[1]))

    # Draw the ball
    pygame.draw.rect(screen, (255, 255, 255), (ball_pos[0], ball_pos[1], ball_size[0], ball_size[1]))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BASKET_SPEED = 5
INITIAL_APPLE_SPEED = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Apple")

font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect)
    text_surface = small_font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def main_game():
    basket = pygame.Rect(WIDTH // 2 - 40, HEIGHT - 60, 80, 20)
    apple = pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20)

    running = True
    score = 0
    apple_speed = INITIAL_APPLE_SPEED

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket.left > 0:
            basket.move_ip(-BASKET_SPEED, 0)
        if keys[pygame.K_RIGHT] and basket.right < WIDTH:
            basket.move_ip(BASKET_SPEED, 0)

        apple.move_ip(0, apple_speed)

        if basket.colliderect(apple):
            score += 1
            apple.topleft = (random.randint(0, WIDTH - 20), 0)
            apple_speed += 0.5

        if apple.top > HEIGHT:
            return score

        level = score

        pygame.draw.rect(screen, BLUE, basket)
        pygame.draw.ellipse(screen, RED, apple)

        level_text = small_font.render(f"Level: {level}", True, BLACK)
        screen.blit(level_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

def game_over_screen(score):
    while True:
        screen.fill(WHITE)

        game_over_text = font.render("Game Over!", True, RED)
        score_text = small_font.render(f"Score: {score}", True, BLACK)

        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)

        restart_button = pygame.Rect(WIDTH // 2 - 60, HEIGHT // 2 + 50, 120, 50)
        draw_button("Restart", restart_button, GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    while True:
        final_score = main_game()
        game_over_screen(final_score)

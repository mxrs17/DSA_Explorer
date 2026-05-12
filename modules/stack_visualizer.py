import pygame
from stack import Stack

WIDTH, HEIGHT = 800, 600

def run(screen):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    stack = Stack()
    counter = 1

    running = True

    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    stack.push(counter)
                    counter += 1

                if event.key == pygame.K_BACKSPACE:
                    stack.pop()

                if event.key == pygame.K_ESCAPE:
                    running = False


        for i, value in enumerate(stack.data):

            rect = pygame.Rect(
                300,
                500 - i * 50,
                200,
                40
            )

            pygame.draw.rect(screen, (100, 200, 255), rect)

            text = font.render(str(value), True, (0, 0, 0))
            screen.blit(text, (390, 510 - i * 50))


        info = font.render(
            "SPACE = Push | BACKSPACE = Pop | ESC = Back",
            True,
            (255, 255, 255)
        )
        screen.blit(info, (80, 30))

        pygame.display.flip()
        clock.tick(60)
import pygame

def run(screen):
    queue = []
    counter = 1
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_SPACE:
                    queue.append(counter)
                    counter += 1


                if event.key == pygame.K_BACKSPACE:
                    if queue:
                        queue.pop(0)

                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((30, 30, 30))

        start_x = 300 - (len(queue) * 35)

        for i, val in enumerate(queue):

            x = start_x + i * 70
            y = 300

            rect = pygame.Rect(x, y, 60, 60)
            pygame.draw.rect(screen, (200, 150, 250), rect)

            text = font.render(str(val), True, (0, 0, 0))
            screen.blit(text, (x + 20, y + 20)) 
  


        info = font.render(
            "SPACE = Enqueue | BACKSPACE = Dequeue | ESC = Back",
            True,
            (255, 255, 255)
        )
        screen.blit(info, (20, 20))

        pygame.display.flip()
        clock.tick(30)
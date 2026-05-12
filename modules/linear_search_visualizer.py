import pygame

def run(screen):

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)


    array = [5, 12, 7, 3, 9, 20, 15]
    target = 9

    i = 0
    comparisons = 0
    found = False

    running = True


    while running:

        screen.fill((30, 30, 30))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return


        bar_width = 50
        base_y = 500

        for j, val in enumerate(array):

            color = (100, 200, 255)

            if j == i:
                color = (255, 80, 80)

            height = val * 5  # scale for visibility

            pygame.draw.rect(
                screen,
                color,
                (100 + j * 70, base_y - height, bar_width, height)
            )


        if i < len(array) and not found:

            comparisons += 1

            if array[i] == target:
                found = True

            i += 1
            pygame.time.delay(500)

        else:
            running = False


        text1 = font.render(f"Comparisons: {comparisons}", True, (255, 255, 255))
        screen.blit(text1, (20, 20))

        text2 = font.render(f"Target: {target}", True, (255, 255, 255))
        screen.blit(text2, (20, 50))

        pygame.display.flip()
        clock.tick(30)

    screen.fill((0, 0, 0))

    msg = "FOUND" if found else "NOT FOUND"
    result = font.render(msg, True, (0, 255, 0))

    screen.blit(result, (300, 250))
    pygame.display.flip()
    pygame.time.delay(1500)
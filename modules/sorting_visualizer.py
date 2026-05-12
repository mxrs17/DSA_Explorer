import pygame
import random

def run(screen):

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    WIDTH, HEIGHT = screen.get_size()

    ARRAY_SIZE = 30
    array = [random.randint(20, 300) for _ in range(ARRAY_SIZE)]
    bar_width = WIDTH // ARRAY_SIZE

    running = True

    def draw(highlight=None, swap=None):

        screen.fill((30, 30, 30))

        for i, val in enumerate(array):
            color = (100, 200, 255)

            if highlight and i in highlight:
                color = (255, 80, 80)

            if swap and i in swap:
                color = (80, 255, 80)

            pygame.draw.rect(
                screen,
                color,
                (i * bar_width, HEIGHT - val, bar_width - 2, val)
            )

        text = font.render(
            "B=Bubble | S=Selection | M=Merge | R=Reset | ESC=Back",
            True,
            (255, 255, 255)
        )
        screen.blit(text, (10, 10))

        pygame.display.flip()

    def handle_events():
        nonlocal running

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False   # return to menu

                if event.key == pygame.K_r:
                    array[:] = [random.randint(20, 300) for _ in range(ARRAY_SIZE)]

                if event.key == pygame.K_b:
                    bubble_sort()

                if event.key == pygame.K_s:
                    selection_sort()

                if event.key == pygame.K_m:
                    merge_sort()

    def bubble_sort():
        n = len(array)

        for i in range(n):
            for j in range(n - i - 1):

                handle_events()

                draw(highlight=[j, j + 1])
                pygame.time.delay(30)

                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    draw(swap=[j, j + 1])
                    pygame.time.delay(30)

                if not running:
                    return

    def selection_sort():
        n = len(array)

        for i in range(n):
            min_idx = i

            for j in range(i + 1, n):

                handle_events()

                if array[j] < array[min_idx]:
                    min_idx = j

                draw(highlight=[min_idx, j])

                if not running:
                    return

            array[i], array[min_idx] = array[min_idx], array[i]

    def merge_sort():
        array.sort()  

    while running:

        handle_events()
        draw()
        clock.tick(60)
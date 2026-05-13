import pygame
import random

WIDTH, HEIGHT = 800, 600

ROWS = 10
COLS = 10

CELL_SIZE = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (100, 220, 100)
BLUE = (100, 180, 255)
RED = (255, 120, 120)
GREY = (200, 200, 200)


def create_grid():

    grid = []

    for row in range(ROWS):

        current_row = []

        for col in range(COLS):

            if random.random() < 0.2 and (row, col) != (0, 0):

                current_row.append(-1)

            else:

                current_row.append(0)

        grid.append(current_row)

    return grid


def fill_dp(grid, screen):

    FONT = pygame.font.SysFont(None, 30)

    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == -1:
        grid[0][0] = 0
    else:
        grid[0][0] = 1

    for row in range(rows):

        for col in range(cols):

            if grid[row][col] == -1:
                continue

            if row == 0 and col == 0:
                continue

            top = 0
            left = 0

            if row > 0 and grid[row - 1][col] != -1:
                top = grid[row - 1][col]

            if col > 0 and grid[row][col - 1] != -1:
                left = grid[row][col - 1]

            grid[row][col] = top + left

            draw_grid(screen, grid, FONT, (row, col))

            pygame.time.wait(150)


def draw_grid(screen, grid, font, current=None):

    screen.fill((240, 240, 240))

    title = font.render(
        "SPACE = Run DP | R = Reset | ESC = Back",
        True,
        (0, 0, 0)
    )

    screen.blit(title, (20, 20))

    for row in range(ROWS):

        for col in range(COLS):

            x = col * CELL_SIZE + 120
            y = row * CELL_SIZE + 60

            color = WHITE

            if grid[row][col] == -1:
                color = BLACK

            elif current == (row, col):
                color = BLUE

            else:
                color = GREEN

            pygame.draw.rect(
                screen,
                color,
                (x, y, CELL_SIZE, CELL_SIZE)
            )

            pygame.draw.rect(
                screen,
                GREY,
                (x, y, CELL_SIZE, CELL_SIZE),
                2
            )

            if grid[row][col] != -1:

                text = font.render(
                    str(grid[row][col]),
                    True,
                    (0, 0, 0)
                )

                text_rect = text.get_rect(
                    center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2)
                )

                screen.blit(text, text_rect)

    total_paths = grid[ROWS - 1][COLS - 1]

    if total_paths == -1:
        total_paths = 0

    result_text = font.render(
        f"Total Paths: {total_paths}",
        True,
        RED
    )

    result_rect = result_text.get_rect(center=(400, 585))

    screen.blit(result_text, result_rect)

    pygame.display.update()


def run(screen):

    FONT = pygame.font.SysFont(None, 30)

    grid = create_grid()

    running = True

    while running:

        draw_grid(screen, grid, FONT)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    fill_dp(grid, screen)

                elif event.key == pygame.K_r:

                    grid = create_grid()

                elif event.key == pygame.K_ESCAPE:

                    running = False
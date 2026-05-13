import pygame
from queue import PriorityQueue

WIDTH, HEIGHT = 800, 600

ROWS = 20
CELL_SIZE = WIDTH // ROWS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
GREY = (180, 180, 180)


class Spot:

    def __init__(self, row, col):

        self.row = row
        self.col = col

        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE

        self.color = WHITE

        self.neighbors = []

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, CELL_SIZE, CELL_SIZE)
        )

        pygame.draw.rect(
            screen,
            GREY,
            (self.x, self.y, CELL_SIZE, CELL_SIZE),
            1
        )

    def update_neighbors(self, grid):

        self.neighbors = []

        # DOWN
        if self.row < ROWS - 1:
            neighbor = grid[self.row + 1][self.col]
            if neighbor.color != BLACK:
                self.neighbors.append(neighbor)

        # UP
        if self.row > 0:
            neighbor = grid[self.row - 1][self.col]
            if neighbor.color != BLACK:
                self.neighbors.append(neighbor)

        # RIGHT
        if self.col < ROWS - 1:
            neighbor = grid[self.row][self.col + 1]
            if neighbor.color != BLACK:
                self.neighbors.append(neighbor)

        # LEFT
        if self.col > 0:
            neighbor = grid[self.row][self.col - 1]
            if neighbor.color != BLACK:
                self.neighbors.append(neighbor)


def heuristic(a, b):

    return abs(a.row - b.row) + abs(a.col - b.col)


def make_grid():

    grid = []

    for row in range(ROWS):

        grid.append([])

        for col in range(ROWS):

            spot = Spot(row, col)

            grid[row].append(spot)

    return grid


def draw(screen, grid):

    screen.fill(WHITE)

    FONT = pygame.font.SysFont(None, 28)

    instructions = FONT.render(
        "Left Click: Start/End/Walls | Right Click: Remove | SPACE: Solve | C: Clear | ESC: Back",
        True,
        (0, 0, 0)
    )

    screen.blit(instructions, (10, 10))

    for row in grid:

        for spot in row:

            spot.draw(screen)

    pygame.display.update()


def reconstruct_path(came_from, current, draw_function):

    while current in came_from:

        current = came_from[current]

        if current.color != GREEN:
            current.color = YELLOW

        draw_function()


def algorithm(draw_function, grid, start, end):

    count = 0

    open_set = PriorityQueue()

    open_set.put((0, count, start))

    came_from = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = heuristic(start, end)

    open_set_hash = {start}

    while not open_set.empty():

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]

        open_set_hash.remove(current)

        if current == end:

            reconstruct_path(came_from, end, draw_function)

            end.color = RED
            start.color = GREEN

            return True

        for neighbor in current.neighbors:

            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:

                came_from[neighbor] = current

                g_score[neighbor] = temp_g_score

                f_score[neighbor] = (
                    temp_g_score + heuristic(neighbor, end)
                )

                if neighbor not in open_set_hash:

                    count += 1

                    open_set.put(
                        (f_score[neighbor], count, neighbor)
                    )

                    open_set_hash.add(neighbor)

                    if neighbor != end:
                        neighbor.color = BLUE

        draw_function()

        if current != start:
            current.color = GREY

    return False


def get_clicked_pos(pos):

    x, y = pos

    row = y // CELL_SIZE
    col = x // CELL_SIZE

    return row, col


def run(screen):

    grid = make_grid()

    start = None
    end = None

    running = True

    while running:

        draw(screen, grid)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                return

            # LEFT CLICK
            if pygame.mouse.get_pressed()[0]:

                pos = pygame.mouse.get_pos()

                row, col = get_clicked_pos(pos)

                if row < ROWS and col < ROWS:

                    spot = grid[row][col]

                    if not start and spot != end:

                        start = spot
                        start.color = GREEN

                    elif not end and spot != start:

                        end = spot
                        end.color = RED

                    elif spot != end and spot != start:

                        spot.color = BLACK

            # RIGHT CLICK
            elif pygame.mouse.get_pressed()[2]:

                pos = pygame.mouse.get_pos()

                row, col = get_clicked_pos(pos)

                if row < ROWS and col < ROWS:

                    spot = grid[row][col]

                    spot.color = WHITE

                    if spot == start:
                        start = None

                    if spot == end:
                        end = None

            if event.type == pygame.KEYDOWN:

                # RUN PATHFINDING
                if event.key == pygame.K_SPACE and start and end:

                    for row in grid:

                        for spot in row:

                            spot.update_neighbors(grid)

                    algorithm(
                        lambda: draw(screen, grid),
                        grid,
                        start,
                        end
                    )

                # CLEAR GRID
                elif event.key == pygame.K_c:

                    start = None
                    end = None

                    grid = make_grid()

                # RETURN TO MENU
                elif event.key == pygame.K_ESCAPE:

                    running = False
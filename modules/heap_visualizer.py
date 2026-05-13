import pygame
import random
from heap_logic import MinHeap

WIDTH, HEIGHT = 800, 600

heap = MinHeap()

processed_event = ""


def draw_heap(screen):

    global processed_event

    FONT = pygame.font.SysFont(None, 30)

    screen.fill((25, 25, 35))

    title = FONT.render(
        "SPACE = Add Event | ENTER = Process Event | ESC = Back",
        True,
        (255, 255, 255)
    )

    screen.blit(title, (20, 20))

    if processed_event != "":

        processed_text = FONT.render(
            f"Processed: {processed_event}",
            True,
            (255, 220, 100)
        )

        screen.blit(processed_text, (20, 60))

    if heap.is_empty():

        empty_text = FONT.render(
            "No Events in Queue",
            True,
            (200, 200, 200)
        )

        screen.blit(empty_text, (280, 300))

    else:

        for i, value in enumerate(heap.heap):

            priority = value[0]
            event_name = value[1]

            x = WIDTH // 2 + (i % 4) * 120 - 180
            y = 170 + (i // 4) * 120

            pygame.draw.circle(screen, (100, 200, 255), (x, y), 40)

            priority_text = FONT.render(
                str(priority),
                True,
                (0, 0, 0)
            )

            screen.blit(priority_text, (x - 10, y - 15))

            event_text = FONT.render(
                event_name,
                True,
                (255, 255, 255)
            )

            screen.blit(event_text, (x - 35, y + 45))

            if i > 0:

                parent = (i - 1) // 2

                parent_x = WIDTH // 2 + (parent % 4) * 120 - 180
                parent_y = 170 + (parent // 4) * 120

                pygame.draw.line(
                    screen,
                    (255, 255, 255),
                    (parent_x, parent_y),
                    (x, y),
                    2
                )

    pygame.display.flip()


def run(screen):

    global processed_event

    running = True

    while running:

        draw_heap(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    priority = random.randint(1, 99)

                    event_name = f"Task {chr(random.randint(65, 90))}"

                    heap.insert((priority, event_name))

                elif event.key == pygame.K_RETURN:

                    removed = heap.extract_min()

                    if removed:
                        processed_event = (
                            f"{removed[1]} (Priority {removed[0]})"
                        )

                elif event.key == pygame.K_ESCAPE:

                    running = False
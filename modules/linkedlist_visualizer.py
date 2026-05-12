import pygame

def run(screen):

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)

    WIDTH, HEIGHT = screen.get_size()

    NODE_RADIUS = 25

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, value):
            if not self.head:
                self.head = Node(value)
                return
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(value)

        def insert_at(self, index, value):
            new_node = Node(value)

            if index == 0:
                new_node.next = self.head
                self.head = new_node
                return

            cur = self.head
            i = 0

            while cur and i < index - 1:
                cur = cur.next
                i += 1

            if cur:
                new_node.next = cur.next
                cur.next = new_node
            else:
                self.append(value)

        def delete(self, value):
            cur = self.head

            if cur and cur.value == value:
                self.head = cur.next
                return

            prev = None
            while cur:
                if cur.value == value:
                    prev.next = cur.next
                    return
                prev = cur
                cur = cur.next

        def reverse(self):
            prev = None
            cur = self.head

            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            self.head = prev

        def to_list(self):
            out = []
            cur = self.head
            while cur:
                out.append(cur.value)
                cur = cur.next
            return out

    ll = LinkedList()
    counter = 1

    running = True

    def draw():

        screen.fill((240, 240, 240))

        cur = ll.head
        x = 80
        y = HEIGHT // 2

        while cur:

            pygame.draw.circle(screen, (100, 200, 255), (x, y), NODE_RADIUS)

            text = font.render(str(cur.value), True, (0, 0, 0))
            screen.blit(text, (x - 10, y - 10))

            if cur.next:
                pygame.draw.line(screen, (0, 0, 0),
                                 (x + NODE_RADIUS, y),
                                 (x + 120 - NODE_RADIUS, y), 3)

            cur = cur.next
            x += 120

        info = font.render(
            "SPACE=Add | A=Insert | D=Delete | R=Reverse | ESC=Back",
            True,
            (0, 0, 0)
        )
        screen.blit(info, (20, 20))

        pygame.display.flip()

    while running:

        draw()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_ESCAPE:
                    running = False


                if event.key == pygame.K_SPACE:
                    ll.append(counter)
                    counter += 1

                if event.key == pygame.K_a:
                    ll.insert_at(0, counter)
                    counter += 1

  
                if event.key == pygame.K_d:
                    ll.delete(counter - 1)


                if event.key == pygame.K_r:
                    ll.reverse()

        clock.tick(60)
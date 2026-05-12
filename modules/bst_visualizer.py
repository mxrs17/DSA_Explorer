import pygame

def run(screen):

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    WIDTH, HEIGHT = screen.get_size()

    NODE_RADIUS = 20



    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BST:
        def __init__(self):
            self.root = None

        def insert(self, value):
            def _insert(node, value):
                if not node:
                    return Node(value)
                if value < node.value:
                    node.left = _insert(node.left, value)
                else:
                    node.right = _insert(node.right, value)
                return node

            self.root = _insert(self.root, value)

        def inorder(self):
            res = []

            def dfs(node):
                if node:
                    dfs(node.left)
                    res.append(node)
                    dfs(node.right)

            dfs(self.root)
            return res

        def preorder(self):
            res = []

            def dfs(node):
                if node:
                    res.append(node)
                    dfs(node.left)
                    dfs(node.right)

            dfs(self.root)
            return res

        def postorder(self):
            res = []

            def dfs(node):
                if node:
                    dfs(node.left)
                    dfs(node.right)
                    res.append(node)

            dfs(self.root)
            return res

        def search(self, value):
            path = []
            node = self.root

            while node:
                path.append(node)
                if value == node.value:
                    break
                elif value < node.value:
                    node = node.left
                else:
                    node = node.right

            return path

        def delete(self, node, value):
            if not node:
                return None

            if value < node.value:
                node.left = self.delete(node.left, value)
            elif value > node.value:
                node.right = self.delete(node.right, value)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                temp = node.right
                while temp.left:
                    temp = temp.left

                node.value = temp.value
                node.right = self.delete(node.right, temp.value)

            return node


    def draw_tree(node, x, y, spacing, highlight_set):

        if not node:
            return

        color = (255, 80, 80) if node in highlight_set else (100, 200, 255)

        pygame.draw.circle(screen, color, (x, y), NODE_RADIUS)

        text = font.render(str(node.value), True, (0, 0, 0))
        screen.blit(text, (x - 10, y - 10))

        if node.left:
            pygame.draw.line(screen, (0, 0, 0), (x, y), (x - spacing, y + 80), 2)
            draw_tree(node.left, x - spacing, y + 80, spacing // 2, highlight_set)

        if node.right:
            pygame.draw.line(screen, (0, 0, 0), (x, y), (x + spacing, y + 80), 2)
            draw_tree(node.right, x + spacing, y + 80, spacing // 2, highlight_set)



    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]

    for v in values:
        bst.insert(v)

    traversal = []
    index = 0
    highlight_set = set()

    search_path = []
    search_index = 0
    searching = False

    search_value = 60

    running = True


    while running:

        screen.fill((240, 240, 240))

        draw_tree(bst.root, WIDTH // 2, 80, 150, highlight_set)

        info = font.render(
            "I=Insert | O=In | P=Pre | T=Post | S=Search | D=Delete | ESC=Back",
            True,
            (0, 0, 0)
        )
        screen.blit(info, (10, 10))


        if traversal:
            highlight_set = set(traversal[:index])

            index += 1
            if index > len(traversal):
                traversal = []
                index = 0



        if searching and search_path:
            highlight_set = set(search_path[:search_index])

            search_index += 1
            if search_index > len(search_path):
                searching = False

        pygame.display.flip()



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False


                if event.key == pygame.K_i:
                    bst.insert(10)


                if event.key == pygame.K_o:
                    traversal = bst.inorder()
                    index = 0

                if event.key == pygame.K_p:
                    traversal = bst.preorder()
                    index = 0


                if event.key == pygame.K_t:
                    traversal = bst.postorder()
                    index = 0


                if event.key == pygame.K_s:
                    search_path = bst.search(search_value)
                    search_index = 0
                    searching = True


                if event.key == pygame.K_d:
                    bst.root = bst.delete(bst.root, 20)

        clock.tick(2)
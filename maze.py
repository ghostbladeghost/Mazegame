import pygame

# Define constants for colors and directions
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (75, 0, 130)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([13, 13])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):
        self.rect.move_ip(self.velocity)

    def move(self, direction):
        self.velocity = pygame.math.Vector2(direction) * 8

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([13, 13])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):
        self.rect.move_ip(self.velocity)

    def move(self, direction):
        self.velocity = pygame.math.Vector2(direction) * 8

class Room:
    def __init__(self):
        self.wall_list = pygame.sprite.Group()

    def update(self):
        self.wall_list.update()

    def draw(self, screen):
        self.wall_list.draw(screen)

class Room1(Room):
    def __init__(self):
        super().__init__()
        walls = [
            [0, 0, 3, 700, GREY],
            [0, 0, 20, 250, BLACK],
            # ... (define other walls)
        ]
        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)

# ... (define other Room classes)

def main():
    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    pygame.display.set_caption('MAZEGAME')

    player = Player(50.0, 50.0)
    enemy = Enemy(37, 63)
    player_group = pygame.sprite.Group(player)
    enemy_group = pygame.sprite.Group(enemy)

    rooms = [Room1(), Room2(), Room3(), Room4(), Room5(),
             Room6(), Room7(), Room8(), Room9(), Room10(),
             Room11(), Room12()]
    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move(LEFT)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move(RIGHT)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move(UP)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.move(DOWN)

        if keys[pygame.K_f]:
            enemy.move(LEFT)
        if keys[pygame.K_h]:
            enemy.move(RIGHT)
        if keys[pygame.K_t]:
            enemy.move(UP)
        if keys[pygame.K_g]:
            enemy.move(DOWN)

        player_group.update()
        enemy_group.update()

        if pygame.sprite.spritecollide(player, current_room.wall_list, False):
            player.rect.move_ip(-player.velocity[0], -player.velocity[1])

        if pygame.sprite.spritecollide(enemy, current_room.wall_list, False):
            enemy.rect.move_ip(-enemy.velocity[0], -enemy.velocity[1])

        if player.rect.left < 0:
            current_room_no = (current_room_no - 1) % len(rooms)
            current_room = rooms[current_room_no]
            player.rect.right = screen.get_width()
        elif player.rect.right > screen.get_width():
            current_room_no = (current_room_no + 1) % len(rooms)
            current_room = rooms[current_room_no]
            player.rect.left = 0

        if enemy.rect.left < 0:
            current_room_no = (current_room_no - 1) % len(rooms)
            current_room = rooms[current_room_no]
            enemy.rect.right = screen.get_width()
        elif enemy.rect.right > screen.get_width():
            current_room_no = (current_room_no + 1) % len(rooms)
            current_room = rooms[current_room_no]
            enemy.rect.left = 0

        screen.fill(GREY)
        current_room.draw(screen)
        player_group.draw(screen)
        enemy_group.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
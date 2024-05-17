import pygame

#perry u do room 5

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (75, 0, 130)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color):
        super().__init__()

        # Make a BLACK wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        if self.image.fill(color):
            self.rect = self.image.get_rect()
            self.rect.y = y
            self.rect.x = x

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Enemy(pygame.sprite.Sprite):
    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        super().__init__()
        # Set height, width
        self.image = pygame.Surface([13, 13])
        self.image.fill(GREEN)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def speed(self, x, y):
        # Change the speed of the player. Called with a keypress.
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        # Find a new position for the player
        if walls == RED:
            self.change_x = 50
            self.change_y = 290

        # Move left/right
        self.rect.x += self.change_x
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            # if walls == RED:
            # self.change_x = 50
            # self.change_y = 290
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Player(pygame.sprite.Sprite):
    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        super().__init__()
        # Set height, width
        self.image = pygame.Surface([13, 13])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def speed(self, x, y):
        # Change the speed of the player. Called with a keypress.
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        # Find a new position for the player
        if walls == RED:
            self.change_x = 50
            self.change_y = 290

        # Move left/right
        self.rect.x += self.change_x
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            # if walls == RED:
            # self.change_x = 50
            # self.change_y = 290
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Room(object):
    # Base class for all rooms.

    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = True

    def __init__(self):
        # Constructor, create our lists. #
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


#perry work on this
class Room1(Room):
    # This creates all the walls in room 1

    def __init__(self):
        Room.__init__(self)
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [
            [0, 0, 3, 700, GREY],  # invisible wall
            [0, 0, 20, 250, BLACK],  # top left
            [0, 350, 20, 250, BLACK],  # bottom left
            [780, 0, 20, 250, BLACK],  # top right
            [780, 350, 20, 250, BLACK],  # bottom right
            [20, 0, 760, 20, BLACK],  # top
            [20, 580, 760, 20, BLACK],  # bottom
            [200, 20, 400, 450, PURPLE],
            [20, 50, 150, 50, GREY],
            [20, 50, 150, 50, GREY],
            [50, 200, 150, 50, GREY],
            [20, 350, 150, 50, GREY],
            [33, 413, 167, 57, GREY],
            [300, 483, 150, 97, GREY],
            [80, 483, 20, 90, GREY],
            [150, 470, 20, 90, GREY],
            [625, 350, 160, 230, GREY],
            [625, 50, 100, 525, GREY],
            ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

    # Make the walls. (x_pos, y_pos, width, height)


#done
class Room2(Room):
    # This creates all the walls in room 2
    def __init__(self):
        Room.__init__(self)

        walls = [
            [500, 350, 15, 250, GREY],
            [400, 350, 15, 310, GREY],
            [0, 0, 20, 250, GREY],
            [0, 350, 20, 500, GREY],
            [780, 350, 20, 250, BLACK],
            [20, 0, 380, 20, GREY],
            # increase to 780 to get ride of width and 400 for x
            [400, 0, 780, 20, GREY],
            # bottom one is below
            [20, 580, 760, 20, GREY],
            [100, 15, 15, 250, GREY],
            [200, 50, 15, 240, GREY],
            [300, 15, 15, 250, GREY],
            [400, 15, 15, 250, GREY],
            [500, 15, 15, 250, GREY],
            [600, 50, 15, 240, GREY],
            [700, 15, 15, 250, GREY],
            [100, 310, 15, 250, GREY],
            [200, 350, 15, 250, GREY],
            [300, 350, 15, 250, GREY],
            #[400, 300, 15, 250, GREY],
            [600, 350, 15, 250, GREY],
            [700, 310, 15, 250, GREY],
            [40, 290, 700, 20, GREY],  # bottom
            [780, 0, 20, 250, BLACK],  # top right]
        ]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


#done
class Room3(Room):
    # This creates all the walls in room 3
    def __init__(self):
        Room.__init__(self)

        walls = [[0, 0, 20, 250, RED], [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED], [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED], [20, 580, 760, 20, RED]]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):
            for y in range(0, 550, 350):
                wall = Wall(x, y, 20, 320, RED)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, RED)
            self.wall_list.add(wall)


class Room4(Room):
    # This creates all the walls in room 4
    def __init__(self):
        Room.__init__(self)
        # Make the walls. (x_pos, y_pos, width, height)
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [
            [0, 0, 20, 250, BLACK],  # top left
            [0, 350, 20, 500, RED],  # bottom left
            [780, 0, 20, 250, BLACK],  # top right
            [780, 350, 20, 250, RED],  # bottom right
            [20, 0, 760, 20, BLACK],  # top
            [20, 580, 760, 20, RED],
            [60, 537, 30, 30, YELLOW],
            [65, 535, 30, 30, YELLOW],
            [70, 532, 30, 30, YELLOW],
            [75, 529, 30, 30, YELLOW],
            [80, 526, 30, 30, YELLOW],
            [85, 523, 30, 30, YELLOW],
            [90, 520, 30, 30, YELLOW],
            [95, 517, 30, 30, YELLOW],
            [100, 514, 30, 30, YELLOW],
            [105, 511, 30, 30, YELLOW],
            [110, 508, 30, 30, YELLOW],
            [115, 505, 30, 30, YELLOW],
            [120, 502, 30, 30, YELLOW],
            [125, 499, 30, 30, YELLOW],
            [130, 496, 30, 30, YELLOW],
            [135, 493, 30, 30, YELLOW],
            [140, 490, 30, 30, YELLOW],
            [145, 487, 30, 30, YELLOW],
            [150, 484, 30, 30, YELLOW],
            [155, 481, 30, 30, YELLOW],
            [160, 478, 30, 30, YELLOW],
            [165, 475, 30, 30, YELLOW],
            [170, 472, 30, 30, YELLOW],
            [175, 469, 30, 30, YELLOW],
            [180, 466, 30, 30, YELLOW],
            [185, 463, 30, 30, YELLOW],
            [190, 460, 30, 30, YELLOW],
            [195, 457, 30, 30, YELLOW],
            [200, 454, 30, 30, YELLOW],
            [205, 451, 30, 30, YELLOW],
            [210, 448, 30, 30, YELLOW],
            [215, 445, 30, 30, YELLOW],
            [220, 442, 30, 30, YELLOW],
            [225, 439, 30, 30, YELLOW],
            [230, 436, 30, 30, YELLOW],
            [235, 433, 30, 30, YELLOW],
            [240, 430, 30, 30, YELLOW],
            [245, 427, 30, 30, YELLOW],
            [250, 424, 30, 30, YELLOW],
            [255, 421, 30, 30, YELLOW],
            [260, 418, 30, 30, YELLOW],
            [265, 415, 30, 30, YELLOW],
            [270, 412, 30, 30, YELLOW],
            [275, 409, 30, 30, YELLOW],
            [280, 406, 30, 30, YELLOW],
            [285, 403, 30, 30, YELLOW],
            [290, 400, 30, 30, YELLOW],
            [295, 397, 30, 30, YELLOW],
            [300, 394, 30, 30, YELLOW],
            [305, 391, 30, 30, YELLOW],
            [310, 388, 30, 30, YELLOW],
            [315, 385, 30, 30, YELLOW],
            [320, 382, 30, 30, YELLOW],
            [325, 379, 30, 30, YELLOW],
            [330, 376, 30, 30, YELLOW],
            [335, 373, 30, 30, YELLOW],
            [340, 370, 30, 30, YELLOW],
            [345, 367, 30, 30, YELLOW],
            [350, 364, 30, 30, YELLOW],
            [355, 361, 30, 30, YELLOW],
            [360, 358, 30, 30, YELLOW],
            [365, 355, 30, 30, YELLOW],
            [370, 352, 30, 30, YELLOW],
            [375, 349, 30, 30, YELLOW],
            [380, 346, 30, 30, YELLOW],
            [385, 343, 30, 30, YELLOW],
            [390, 340, 30, 30, YELLOW],
            [395, 337, 30, 30, YELLOW],
            [400, 334, 30, 30, YELLOW],
            [405, 331, 30, 30, YELLOW],
            [410, 328, 30, 30, YELLOW],
            [415, 325, 30, 30, YELLOW],
            [420, 322, 30, 30, YELLOW],
            [425, 319, 30, 30, YELLOW],
            [430, 316, 30, 30, YELLOW],
            [435, 313, 30, 30, YELLOW],
            [440, 310, 30, 30, YELLOW],
            [445, 307, 30, 30, YELLOW],
            [450, 304, 30, 30, YELLOW],
            [455, 301, 30, 30, YELLOW],
            [460, 298, 30, 30, YELLOW],
            [465, 295, 30, 30, YELLOW],
            [470, 292, 30, 30, YELLOW],
            [475, 289, 30, 30, YELLOW],
            [480, 286, 30, 30, YELLOW],
            [485, 283, 30, 30, YELLOW],
            [490, 280, 30, 30, YELLOW],
            [495, 277, 30, 30, YELLOW],
            [500, 274, 30, 30, YELLOW],
            [505, 271, 30, 30, YELLOW],
            [510, 268, 30, 30, YELLOW],
            [515, 265, 30, 30, YELLOW],
            [520, 262, 30, 30, YELLOW],
            [525, 259, 30, 30, YELLOW],
            [530, 256, 30, 30, YELLOW],
            [535, 253, 30, 30, YELLOW],
            [540, 250, 30, 30, YELLOW],
            [545, 247, 30, 30, YELLOW],
            [550, 244, 30, 30, YELLOW],
            [555, 241, 30, 30, YELLOW],
            [560, 238, 30, 30, YELLOW],
            [565, 235, 30, 30, YELLOW],
            [570, 232, 30, 30, YELLOW],
            [575, 229, 30, 30, YELLOW],
            [580, 226, 30, 30, YELLOW],
            [585, 223, 30, 30, YELLOW],
            [590, 220, 30, 30, YELLOW],
            [595, 217, 30, 30, YELLOW],
            [600, 214, 30, 30, YELLOW],
            [605, 211, 30, 30, YELLOW],
            [610, 208, 30, 30, YELLOW],
            [615, 205, 30, 30, YELLOW],
            [620, 202, 30, 30, YELLOW],
            [625, 199, 30, 30, YELLOW],
            [630, 196, 30, 30, YELLOW],
            [635, 193, 30, 30, YELLOW],
            [640, 190, 30, 30, YELLOW],
            [645, 187, 30, 30, YELLOW],
            [650, 184, 30, 30, YELLOW],
            [655, 181, 30, 30, YELLOW],
            [660, 178, 30, 30, YELLOW],
            [665, 175, 30, 30, YELLOW],
            [670, 172, 30, 30, YELLOW],
            [675, 169, 30, 30, YELLOW],
            [680, 166, 30, 30, YELLOW],
            [685, 163, 30, 30, YELLOW],
            [690, 160, 30, 30, YELLOW],
            [695, 157, 30, 30, YELLOW],
            [700, 154, 30, 30, YELLOW],
            [705, 151, 30, 30, YELLOW],
            [710, 148, 30, 30, YELLOW],
            [715, 145, 30, 30, YELLOW],
            [720, 142, 30, 30, YELLOW],
            [725, 139, 30, 30, YELLOW],
            [730, 136, 30, 30, YELLOW],
        ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


#Perry work on this one
class Room5(Room):
    # This creates all the walls in room 2
    def __init__(self):
        Room.__init__(self)
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, BLACK], [0, 350, 20, 250, BLACK],
                 [780, 0, 20, 250, BLACK], [780, 350, 20, 250, BLACK],
                 [20, 0, 760, 20, BLACK], [20, 580, 760, 20, BLACK]]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

    # Make the walls. (x_pos, y_pos, width, height)


#done
class Room6(Room):
    # This creates all the walls in room 6
    def __init__(self):
        Room.__init__(self)
        # Make the walls. (x_pos, y_pos, width, height)
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [
            [0, 0, 20, 250, RED],  # top left
            [0, 350, 20, 500, RED],  # bottom left
            [780, 0, 20, 250, RED],  # top right
            [780, 350, 20, 250, RED],  # bottom right
            [20, 0, 760, 20, RED],  # top
            [20, 580, 760, 20, RED],  # bottom
            [380, 20, 20, 20, RED],
            [380, 65, 20, 20, RED],
            [380, 110, 20, 20, RED],
            [380, 155, 20, 20, RED],
            [380, 200, 20, 20, RED],
            [380, 245, 20, 20, RED],
            [380, 290, 20, 20, RED],
            [380, 335, 20, 20, RED],
            [380, 380, 20, 20, RED],
            [380, 425, 20, 20, RED],
            [380, 470, 20, 20, RED],
            [380, 515, 20, 20, RED],
            [380, 560, 20, 20, RED],
            [425, 45, 20, 20, RED],
            [425, 90, 20, 20, RED],
            [425, 135, 20, 20, RED],
            [425, 180, 20, 20, RED],
            [425, 225, 20, 20, RED],
            [425, 270, 20, 20, RED],
            [425, 315, 20, 20, RED],
            [425, 360, 20, 20, RED],
            [425, 405, 20, 20, RED],
            [425, 450, 20, 20, RED],
            [425, 495, 20, 20, RED],
            [425, 540, 20, 20, RED],
            [335, 45, 20, 20, RED],
            [335, 90, 20, 20, RED],
            [335, 135, 20, 20, RED],
            [335, 180, 20, 20, RED],
            [335, 225, 20, 20, RED],
            [335, 270, 20, 20, RED],
            [335, 315, 20, 20, RED],
            [335, 360, 20, 20, RED],
            [335, 405, 20, 20, RED],
            [335, 450, 20, 20, RED],
            [335, 495, 20, 20, RED],
            [335, 540, 20, 20, RED],
            [290, 20, 20, 20, RED],
            [290, 65, 20, 20, RED],
            [290, 110, 20, 20, RED],
            [290, 155, 20, 20, RED],
            [290, 200, 20, 20, RED],
            [290, 245, 20, 20, RED],
            [290, 290, 20, 20, RED],
            [290, 335, 20, 20, RED],
            [290, 380, 20, 20, RED],
            [290, 425, 20, 20, RED],
            [290, 470, 20, 20, RED],
            [290, 515, 20, 20, RED],
            [290, 560, 20, 20, RED],
            [245, 45, 20, 20, RED],
            [245, 90, 20, 20, RED],
            [245, 135, 20, 20, RED],
            [245, 180, 20, 20, RED],
            [245, 225, 20, 20, RED],
            [245, 270, 20, 20, RED],
            [245, 315, 20, 20, RED],
            [245, 360, 20, 20, RED],
            [245, 405, 20, 20, RED],
            [245, 450, 20, 20, RED],
            [245, 495, 20, 20, RED],
            [245, 540, 20, 20, RED],
            [470, 20, 20, 20, RED],
            [470, 65, 20, 20, RED],
            [470, 110, 20, 20, RED],
            [470, 155, 20, 20, RED],
            [470, 200, 20, 20, RED],
            [470, 245, 20, 20, RED],
            [470, 290, 20, 20, RED],
            [470, 335, 20, 20, RED],
            [470, 380, 20, 20, RED],
            [470, 425, 20, 20, RED],
            [470, 470, 20, 20, RED],
            [470, 515, 20, 20, RED],
            [470, 560, 20, 20, RED],
            [515, 45, 20, 20, RED],
            [515, 90, 20, 20, RED],
            [515, 135, 20, 20, RED],
            [515, 180, 20, 20, RED],
            [515, 225, 20, 20, RED],
            [515, 270, 20, 20, RED],
            [515, 315, 20, 20, RED],
            [515, 360, 20, 20, RED],
            [515, 405, 20, 20, RED],
            [515, 450, 20, 20, RED],
            [515, 495, 20, 20, RED],
            [515, 540, 20, 20, RED],
            [560, 20, 20, 20, RED],
            [560, 65, 20, 20, RED],
            [560, 110, 20, 20, RED],
            [560, 155, 20, 20, RED],
            [560, 200, 20, 20, RED],
            [560, 245, 20, 20, RED],
            [560, 290, 20, 20, RED],
            [560, 335, 20, 20, RED],
            [560, 380, 20, 20, RED],
            [560, 425, 20, 20, RED],
            [560, 470, 20, 20, RED],
            [560, 515, 20, 20, RED],
            [560, 560, 20, 20, RED],
            [470, 537.5, 20, 20, GREY],  # invisible blocks after this
            [470, 492.5, 20, 20, GREY],
            [470, 402.5, 20, 20, GREY],
            [470, 87.5, 20, 20, GREY],
            [470, 177.5, 20, 20, GREY],
            [245, 382.5, 20, 20, GREY],
            [245, 472.5, 20, 20, GREY],
            [245, 292.5, 20, 20, GREY]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room7(Room):
    # This creates all the walls in room 5
    def __init__(self):
        Room.__init__(self)
        # Make the walls. (x_pos, y_pos, width, height)
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, BLACK], [0, 350, 20, 250, BLACK],
                 [780, 0, 20, 250, BLACK], [780, 350, 20, 250, BLACK],
                 [20, 0, 760, 20, BLACK], [20, 580, 760, 20, BLACK]]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room8(Room):
    # This creates all the walls in room 5
    def __init__(self):
        Room.__init__(self)
        # Make the walls. (x_pos, y_pos, width, height)
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, BLACK], [0, 350, 20, 250, BLACK],
                 [780, 0, 20, 250, BLACK], [780, 350, 20, 250, BLACK],
                 [20, 0, 760, 20, BLACK], [20, 580, 760, 20, BLACK]]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room9(Room):
    # This creates all the walls in room 5
    def __init__(self):
        Room.__init__(self)
        # Make the walls. (x_pos, y_pos, width, height)
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [
            [0, 0, 20, 250, RED],  # top left
            [0, 350, 20, 500, RED],  # bottom left
            [780, 0, 20, 250, RED],  # top right
            [780, 350, 20, 250, RED],  # bottom right
            [20, 0, 760, 20, RED],  # top
            [20, 580, 760, 20, RED],  # bottom
        ]

        # Loop through the list. Create the wall, add it to the list

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


#finaly room northing much
class Room10(Room):
    # This creates all the walls in room 5
    def __init__(self):
        Room.__init__(self)
        # Make the walls. (x_pos, y_pos, width, height)
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [
            [0, 0, 20, 250, BLUE],  # top lefWt
            [0, 350, 20, 500, BLUE],  # bottom left
            [780, 0, 20, 900, PURPLE],  # top right
            [780, 350, 20, 900, PURPLE],  # bottom right
            [20, 0, 760, 20, BLACK],  # top
            [20, 580, 760, 20, BLACK],
        ]  # bottom
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room11(Room):
    # This creates all the walls in room 11
    def __init__(self):
        Room.__init__(self)
        # Make the walls. (x_pos, y_pos, width, height)
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [
            [0, 0, 20, 1000, BLACK],  # top left
            [0, 275, 20, 1000, BLACK],  # bottom left
            [780, 0, 20, 250, BLACK],  # top right
            [780, 350, 20, 250, BLACK],  # bottom right
            [20, 0, 760, 20, BLACK],  # top
            [20, 580, 760, 20, BLACK],  # bottom
        ]
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room12(Room):
    # This creates all the walls in room 11
    def __init__(self):
        Room.__init__(self)
        # Make the walls. (x_pos, y_pos, width, height)
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [
            [0, 0, 20, 1000, BLACK],  # top left
            [0, 275, 20, 1000, BLACK],  # bottom left
            [780, 0, 20, 250, BLACK],  # top right
            [780, 350, 20, 250, BLACK],  # bottom right
            [20, 0, 760, 20, BLACK],  # top
            [20, 580, 760, 20, BLACK],  # bottom
        ]
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


def main():
    pygame.init()

    # screen size
    screen = pygame.display.set_mode([800, 600])
    screen2 = pygame.display.set_mode([800, 600])
    # Set the title of the window
    pygame.display.set_caption('MAZEGAME')
    player = Player(50.0, 50.0)
    enemy = Enemy(37, 63)
    moving = pygame.sprite.Group()
    moving1 = pygame.sprite.Group()
    moving1.add(enemy)
    moving.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    room = Room4()
    rooms.append(room)

    room = Room5()
    rooms.append(room)

    room = Room6()
    rooms.append(room)

    room = Room7()
    rooms.append(room)

    room = Room8()
    rooms.append(room)

    room = Room9()
    rooms.append(room)

    room = Room10()
    rooms.append(room)

    room = Room11()
    rooms.append(room)

    room = Room12()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()
    done = False

    while not done:

        # Event

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speed(-8, 0)
                if event.key == pygame.K_RIGHT:
                    player.speed(8, 0)
                if event.key == pygame.K_UP:
                    player.speed(0, -8)
                if event.key == pygame.K_DOWN:
                    player.speed(0, 8)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speed(8, 0)
                if event.key == pygame.K_RIGHT:
                    player.speed(-8, 0)
                if event.key == pygame.K_UP:
                    player.speed(0, 8)
                if event.key == pygame.K_DOWN:
                    player.speed(0, -8)

            # keys = pygame.key.get_pressed()

            # if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_a:
            # player.speed(-1, 0)
            # if event.key == pygame.K_d:
            # player.speed(1, 0)
            # if event.key == pygame.K_w:
            # player.speed(0, -1)
            # if event.key == pygame.K_s:
            # player.speed(0, 1)

            # if event.type == pygame.KEYUP:
            # if event.key == pygame.K_a:
            # player.speed(1, 0)
            # if event.key == pygame.K_d:
            # player.speed(-1, 0)
            # if event.key == pygame.K_w:
            # player.speed(0, 1)
            # if event.key == pygame.K_s:
            # player.speed(0, -1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    player.speed(-1, 0)
                if event.key == pygame.K_l:
                    player.speed(1, 0)
                if event.key == pygame.K_i:
                    player.speed(0, -1)
                if event.key == pygame.K_k:
                    player.speed(0, 1)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_j:
                    player.speed(1, 0)
                if event.key == pygame.K_l:
                    player.speed(-1, 0)
                if event.key == pygame.K_i:
                    player.speed(0, 1)
                if event.key == pygame.K_k:
                    player.speed(0, -1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    enemy.speed(-8, 0)
                if event.key == pygame.K_d:
                    enemy.speed(8, 0)
                if event.key == pygame.K_w:
                    enemy.speed(0, -8)
                if event.key == pygame.K_s:
                    enemy.speed(0, 8)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    enemy.speed(8, 0)
                if event.key == pygame.K_d:
                    enemy.speed(-8, 0)
                if event.key == pygame.K_w:
                    enemy.speed(0, 8)
                if event.key == pygame.K_s:
                    enemy.speed(0, -8)

            # keys = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    enemy.speed(-1, 0)
                if event.key == pygame.K_h:
                    enemy.speed(1, 0)
                if event.key == pygame.K_t:
                    enemy.speed(0, -1)
                if event.key == pygame.K_g:
                    enemy.speed(0, 1)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    enemy.speed(1, 0)
                if event.key == pygame.K_h:
                    enemy.speed(-1, 0)
                if event.key == pygame.K_t:
                    enemy.speed(0, 1)
                if event.key == pygame.K_g:
                    enemy.speed(0, -1)

        # Game Logic
        # add or remove below just for testing
        player.move(current_room.wall_list)
        enemy.move(current_room.wall_list)
        # below is to show coordinates
        # print(player.rect.x, player.rect.y, current_room)
        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 9
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 9:
                current_room_no = 8
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 8:
                current_room_no = 7
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 7:
                current_room_no = 6
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 6:
                current_room_no = 5
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 5:
                current_room_no = 4
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 4:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 3:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 1:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790
                # else:
                # current_room_no = 0
                # current_room = rooms[current_room_no]

                player.rect.x = 790

        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 2:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 3:
                current_room_no = 4
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 4:
                current_room_no = 5
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 5:
                current_room_no = 6
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 6:
                current_room_no = 7
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 7:
                current_room_no = 8
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 8:
                current_room_no = 9
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 9 or current_room_no == 10:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 11:
                current_room_no = 9
                current_room = rooms[current_room_no]
                player.rect.x = 0
        if player.rect.y > 599:
            if current_room_no == 0 or current_room_no == 1 or (
                    current_room_no == 2 or current_room_no == 3) or (
                        current_room_no == 4 or current_room_no == 5 or
                        (current_room_no == 6 or current_room_no == 7)) or (
                            current_room_no == 8 or current_room_no == 11):
                current_room_no = 10
                current_room = rooms[current_room_no]
                player.rect.x = 380
                player.rect.y = 250
            elif current_room_no == 9:
                current_room_no = 11
                current_room = rooms[current_room_no]
                player.rect.x = 380
                player.rect.y = 250
        if player.rect.y < -11:
            if current_room_no == 0 or current_room_no == 1 or (
                    current_room_no == 2 or current_room_no == 3) or (
                        current_room_no == 4 or current_room_no == 5 or
                        (current_room_no == 6
                         or current_room_no == 7)) or current_room_no == 8:
                current_room_no = 10
                current_room = rooms[current_room_no]
                player.rect.x = 380
                player.rect.y = 250
            elif current_room_no == 9:
                current_room_no = 11
                current_room = rooms[current_room_no]
                player.rect.x = 380
                player.rect.y = 250
            elif current_room_no == 11:
                current_room_no = 10
                current_room = rooms[current_room_no]
                player.rect.x = 380
                player.rect.y = 250
        if enemy.rect.y > 599:
            if current_room_no == 0:
                current_room_no = 10
                current_room = rooms[current_room_no]
                player.rect.x = 380
                player.rect.y = 250
            elif current_room_no == 1:
                current_room_no = 10
                current_room = rooms[current_room_no]
                #player.rect.x =
                #player.rect.y =
            elif current_room_no == 1 or current_room_no == 2 or (
                    current_room_no == 3 or current_room_no
                    == 4) or (current_room_no == 5 or current_room_no == 6 or
                              (current_room_no == 7 or current_room_no == 8)):
                current_room_no = 10
                current_room = rooms[current_room_no]
                player.rect.x = 380
                player.rect.y = 250
            elif current_room_no == 9:
                current_room_no = 11
                current_room = rooms[current_room_no]
                player.rect.x = 380
                player.rect.y = 250
            elif current_room_no == 11:
                current_room_no = 10
                current_room = rooms[current_room_no]
                player.rect.x = 380
                player.rect.y = 250

        if enemy.rect.y < -12:
            if current_room_no == 0 or current_room_no == 1 or (
                    current_room_no == 2 or current_room_no == 3) or (
                        current_room_no == 4 or current_room_no == 5 or
                        (current_room_no == 6
                         or current_room_no == 7)) or current_room_no == 8:
                current_room_no = 10
                current_room = rooms[current_room_no]
                enemy.rect.x = 380
                enemy.rect.y = 250
            elif current_room_no == 9:
                current_room_no = 11
                current_room = rooms[current_room_no]
                enemy.rect.x = 380
                enemy.rect.y = 250
            elif current_room_no == 11:
                current_room_no = 10
                current_room = rooms[current_room_no]
                player.rect.x = 380
                player.rect.y = 250
        # Player
        # vs
        # Player 2
        # Code
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         done = True
        #
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_a:
        #             enemy.speed(-8, 0)
        #         if event.key == pygame.K_d:
        #             enemy.speed(8, 0)
        #         if event.key == pygame.K_w:
        #             enemy.speed(0, -8)
        #         if event.key == pygame.K_s:
        #             enemy.speed(0, 8)
        #
        #     if event.type == pygame.KEYUP:
        #         if event.key == pygame.K_a:
        #             enemy.speed(8, 0)
        #         if event.key == pygame.K_d:
        #             enemy.speed(-8, 0)
        #         if event.key == pygame.K_w:
        #             enemy.speed(0, 8)
        #         if event.key == pygame.K_s:
        #             enemy.speed(0, -8)
        #
        #     #keys = pygame.key.get_pressed()
        #
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_f:
        #             enemy.speed(-1, 0)
        #         if event.key == pygame.K_h:
        #             enemy.speed(1, 0)
        #         if event.key == pygame.K_t:
        #             enemy.speed(0, -1)
        #         if event.key == pygame.K_g:
        #             enemy.speed(0, 1)
        #
        #     if event.type == pygame.KEYUP:
        #         if event.key == pygame.K_f:
        #             enemy.speed(1, 0)
        #         if event.key == pygame.K_h:
        #             enemy.speed(-1, 0)
        #         if event.key == pygame.K_t:
        #             enemy.speed(0, 1)
        #         if event.key == pygame.K_g:
        #             enemy.speed(0, -1)

        # if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_j:
        # player.speed(-16, 0)
        # if event.key == pygame.K_l:
        # player.speed(16, 0)
        # if event.key == pygame.K_i:
        # player.speed(0, -16)
        # if event.key == pygame.K_k:
        # player.speed(0, 16)

        # if event.type == pygame.KEYUP:
        # if event.key == pygame.K_j:
        # player.speed(16, 0)
        # if event.key == pygame.K_l:
        # player.speed(-16, 0)
        # if event.key == pygame.K_i:
        # player.speed(0, 16)
        # if event.key == pygame.K_k:
        # player.speed(0, -16)

        # Game Logic
        # add or remove below just for testing
        player.move(current_room.wall_list)
        print(player.rect.x, player.rect.y, current_room)
        if enemy.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 9
                current_room = rooms[current_room_no]
                enemy.rect.x = 790
            elif current_room_no == 9:
                current_room_no = 8
                current_room = rooms[current_room_no]
                enemy.rect.x = 790
            elif current_room_no == 8:
                current_room_no = 7
                current_room = rooms[current_room_no]
                enemy.rect.x = 790
            elif current_room_no == 7:
                current_room_no = 6
                current_room = rooms[current_room_no]
                enemy.rect.x = 790
            elif current_room_no == 6:
                current_room_no = 5
                current_room = rooms[current_room_no]
                enemy.rect.x = 790
            elif current_room_no == 5:
                current_room_no = 4
                current_room = rooms[current_room_no]
                enemy.rect.x = 790
            elif current_room_no == 4:
                current_room_no = 3
                current_room = rooms[current_room_no]
                enemy.rect.x = 790
            elif current_room_no == 3:
                current_room_no = 2
                current_room = rooms[current_room_no]
                enemy.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                enemy.rect.x = 790
            elif current_room_no == 1:
                current_room_no = 0
                current_room = rooms[current_room_no]
                enemy.rect.x = 790
                # else:
                # current_room_no = 0
                # current_room = rooms[current_room_no]

                # player.rect.x = 790

        if enemy.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                enemy.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                enemy.rect.x = 0
            elif current_room_no == 2:
                current_room_no = 3
                current_room = rooms[current_room_no]
                enemy.rect.x = 0
            elif current_room_no == 3:
                current_room_no = 4
                current_room = rooms[current_room_no]
                enemy.rect.x = 0
            elif current_room_no == 4:
                current_room_no = 5
                current_room = rooms[current_room_no]
                enemy.rect.x = 0
            elif current_room_no == 5:
                current_room_no = 6
                current_room = rooms[current_room_no]
                enemy.rect.x = 0
            elif current_room_no == 6:
                current_room_no = 7
                current_room = rooms[current_room_no]
                enemy.rect.x = 0
            elif current_room_no == 7:
                current_room_no = 8
                current_room = rooms[current_room_no]
                enemy.rect.x = 0
            elif current_room_no == 8:
                current_room_no = 9
                current_room = rooms[current_room_no]
                enemy.rect.x = 0
            elif current_room_no == 9 or current_room_no == 10:
                current_room_no = 0
                current_room = rooms[current_room_no]
                enemy.rect.x = 0
            elif current_room_no == 11:
                current_room_no = 9
                current_room = rooms[current_room_no]
                player.rect.x = 380
                player.rect.y = 250
        if enemy.rect.y > 599:
            if current_room_no == 0 or current_room_no == 1 or (
                    current_room_no == 2 or current_room_no == 3) or (
                        current_room_no == 4 or current_room_no == 5 or
                        (current_room_no == 6
                         or current_room_no == 7)) or current_room_no == 8:
                current_room_no = 10
                current_room = rooms[current_room_no]
                enemy.rect.x = 380
                enemy.rect.y = 250
            elif current_room_no == 9:
                current_room_no = 11
                current_room = rooms[current_room_no]
                enemy.rect.x = 380
                enemy.rect.y = 250

        if enemy.rect.y < -12:
            if current_room_no == 0 or current_room_no == 1 or (
                    current_room_no == 2 or current_room_no == 3) or (
                        current_room_no == 4 or current_room_no == 5 or
                        (current_room_no == 6
                         or current_room_no == 7)) or current_room_no == 8:
                current_room_no = 10
                current_room = rooms[current_room_no]
                enemy.rect.x = 380
                enemy.rect.y = 250
            elif current_room_no == 9:
                current_room_no = 11
                current_room = rooms[current_room_no]
                enemy.rect.x = 380
                enemy.rect.y = 250
                # if enemy in current_room_no == 10:
                #     current_room_no = 10
                #     current_room = rooms[current_room_no]
                #     player.rect.x = 380
                #     player.rect.y = 250
            # else:
            # current_room_no = 0
            # current_room = rooms[current_room_no]
            # enemy.rect.x = 0

        screen.fill(GREY)

        moving.draw(screen)
        moving1.draw(screen)
        current_room.wall_list.draw(screen)

        screen2.fill(GREY)

        moving.draw(screen2)
        moving1.draw(screen2)
        current_room.wall_list.draw(screen2)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


#the check wall collisions is still not working
screen = pygame.display.set_mode([800, 600])


def check_wall_collision(Enemy, RED):
    """CHECKS IF THE SPRITE HAS COLLIDED WITH A RED WALL"""
    sprite_rect = Enemy.get_rect()
    for x in range(sprite_rect.left, sprite_rect.right):
        for y in range(sprite_rect.top, sprite_rect.bottom):
            # Get the color of the pixel at the current position
            color = screen.get_at((x, y))
            # Check if the color matches the wall color
            if color == RED:
                return True
    return False


if __name__ == "__main__":
    main()

import pygame

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


class Room:
    def __init__(self):
        self.wall_list = pygame.sprite.Group()

    def update(self):
        self.wall_list.update()

    def draw(self, screen):
        self.wall_list.draw(screen)



class Room1(Room):
    # This creates all the walls in room 1

    def __init__(self):
        Room.__init__(self)
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [
            [0, 0, 3, 700, GREY],  # invisible wall
            [0, 0, 20, 250, PURPLE],  # top left
            [0, 350, 20, 250, PURPLE],  # bottom left
            [780, 0, 20, 250, PURPLE],  # top right
            [780, 350, 20, 250, PURPLE],  # bottom right
            [20, 0, 760, 20, PURPLE],  # top
            [20, 580, 760, 20, PURPLE],  # bottom
            [200, 20, 400, 450, PURPLE],
            [20, 50, 150, 50, PURPLE],
            [20, 50, 150, 50, PURPLE],
            [50, 200, 150, 50, PURPLE],
            [20, 350, 150, 50, PURPLE],
            [33, 413, 167, 57, PURPLE],
            [300, 483, 150, 97, PURPLE],
            [80, 483, 20, 97, PURPLE],
            [150, 470, 20, 90, PURPLE],
            [625, 350, 160, 230, PURPLE],
            [625, 50, 100, 525, PURPLE],
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



class Room5(Room):
    # This creates all the walls in room 2
    def __init__(self):
        Room.__init__(self)
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, BLACK], 
                 [0, 350, 20, 250, BLACK],
                 [780, 0, 20, 250, BLACK],
                 [780, 350, 20, 250, BLACK],
                 [20, 0, 760, 20, BLACK], 
                 [20, 580, 760, 20, BLACK],
                 
                 [500,500, 300, 300, BLACK],
                 [500, 20, 300, 217, BLACK],
                 [40, 33, 447, 204, BLACK],
                 [487, 224, 13, 13, GREY],
                 [487,237, 13, 250, GREY],
                 [474,487, 13, 30, GREY],
                 [60,487, 414, 30, GREY],
                 [60, 350, 13, 137, GREY],
                 ]

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
        walls = [[390, 60, 15, 600, BLACK],
             [340, -10, 15, 550, BLACK],
             [290, 60, 15, 600, BLACK],
             [240, -10, 15, 550, BLACK],
             [190, 60, 15, 600, BLACK],
             [140, -10, 15, 550, BLACK],
             # [90, 60, 15, 600, BLACK],
             [440, -10, 15, 550, BLACK],
             [490, 60, 15, 600, BLACK],
             [540, -10, 15, 550, BLACK],
             [590, 60, 15, 600, BLACK],
             [640, -10, 15, 550, BLACK],
             [0, 0, 20, 250, BLUE],  # top left
             [0, 350, 20, 500, GREEN],  # bottom left
             [780, 0, 20, 250, BLUE],  # top right
             [780, 350, 20, 250, GREEN],  # bottom right
             [0, 0, 900, 20, BLUE],  # top
             [20, 580, 760, 20, GREEN],  # bottom
                ]

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
        walls = [[80, 50, 640, 20, RED],
               [130, 100, 640, 20, RED],
               [80, 150, 640, 20, RED],
               [130, 200, 640, 20, RED],
               [80, 250, 620, 20, RED],
               [130, 300, 620, 20, RED],
               [80, 350, 620, 20, RED],
               [130, 400, 620, 20, RED],
               [80, 450, 620, 20, RED],
               [130, 500, 620, 20, RED],
               [80, 550, 620, 20, RED],

               [730, 200, 20, 350, RED],
               [70, 50, 20, 600, RED],

               [0, 0, 20, 250, RED],
               [0, 350, 20, 250, RED],
               [780, 0, 20, 250, RED],
               [780, 350, 20, 250, RED],
               [20, 0, 760, 20, RED],
               [20, 580, 760, 20, RED],
               ]

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
             [390, 60, 15, 600, RED],
             [340, -10, 15, 550, BLACK],
             [290, 60, 15, 600, BLACK],
             [240, -10, 15, 550, BLACK],
             [190, 60, 15, 600, RED],
             [140, -10, 15, 550, BLACK],
             [90, 60, 15, 600, BLACK],
             [440, -10, 15, 550, RED],
             [490, 60, 15, 600, BLACK],
             [540, -10, 15, 550, BLACK],
             [590, 60, 15, 600, RED],
             [640, -10, 15, 550, BLACK],
             [690, 60, 15, 600, BLACK],
             [0, 0, 20, 250, RED],
             [0, 350, 20, 250, RED],
             [780, 0, 20, 250, RED],
             [780, 350, 20, 250, RED],
             [20, 0, 760, 20, RED],
             [20, 580, 760, 20, RED]]

        # Loop through the list. Create the wall, add it to the list

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

#screen = pygame.display.set_mode([800, 600])
#finaly room northing much
class Room10(Room):
    # This creates all the walls in room 5
    def __init__(self):
        Room.__init__(self)
        # Make the walls. (x_pos, y_pos, width, height)
        # This is a list of walls. Each is in the form [x, y, width, height]
        #each letter 50x100 100 gap
        walls = [
            [0, 0, 20, 250, BLUE],  # top lefWWt
            [0, 350, 20, 500, BLUE],  # bottom left
            [780, 0, 20, 900, PURPLE],  # top right
            [780, 350, 20, 900, PURPLE],  # bottom right
            [20, 0, 760, 20, BLACK],  # top
            [20, 580, 760, 20, BLACK],
            #D
            [205, 250, 10, 100, BLACK],
            [255, 290, 10, 20, BLACK],
            
            [215, 250, 10, 10, BLACK], #going down
            [225, 260, 10, 10, BLACK],
            [235, 270, 10, 10, BLACK],
            [245, 280, 10, 10, BLACK],

            [215, 340, 10, 10, BLACK], #going up
            [225, 330, 10, 10, BLACK],
            [235, 320, 10, 10, BLACK],
            [245, 310, 10, 10, BLACK],
            
            #O
            [315, 250, 10, 100, BLACK],
            [365, 250, 10, 100, BLACK],
            [325, 250, 50, 10, BLACK],
            [325, 340, 50, 10, BLACK],
            #N #40 accross, 100 down
            [425, 250, 10, 100, BLACK], 
            [475, 250, 10, 100, BLACK],

            [435, 250, 10, 25, BLACK],
            [445, 275, 10, 25, BLACK],
            [455, 300, 10, 25, BLACK],
            [465, 325, 10, 25, BLACK],
            #E
            [535, 250, 10, 100, BLACK],
            [545, 250, 40, 10, BLACK],
            [545, 295, 40, 10, BLACK],
            [545, 340, 40, 10, BLACK],
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

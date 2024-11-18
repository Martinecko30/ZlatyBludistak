import pygame


class GameObject:
    def __init__(self, position: tuple[int, int], image: pygame.image):
        '''
        Initializes GameObject
        :param position: Coordinates of the object [x, y]
        :param sprite: Sprite of the object
        '''
        self.position = position
        self.image = image
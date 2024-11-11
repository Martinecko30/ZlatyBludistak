class GameObject:
    def __init__(self, position: tuple[int, int]):
        '''
        Initializes GameObject
        :param position:
        '''
        self.x = int(position[0])
        self.y = int(position[1])
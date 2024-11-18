from enum import Enum

class DrawPosition(Enum):
    TOP_LEFT = 0
    MIDDLE = 1

class Difficulty(Enum):
    TUTORIAL = 0
    EASY = 1
    MEDIUM = 2
    HARD = 3
    DARK_SOULS = 4

class LogLevel(Enum):
    HIDDEN = "Hidden"
    INFO = "Info"
    WARNING = "Warning"
    SEVERE = "Severe"
    ERROR = "Error"
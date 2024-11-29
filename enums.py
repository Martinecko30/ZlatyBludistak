from enum import Enum

class DrawPosition(Enum):
    TOP_LEFT = 0
    MIDDLE = 1

class Difficulty(Enum):
    TUTORIAL = 20
    EASY = 40
    MEDIUM = 80
    HARD = 160
    DARK_SOULS = 500

class LogLevel(Enum):
    HIDDEN = "Hidden"
    INFO = "Info"
    WARNING = "Warning"
    SEVERE = "Severe"
    ERROR = "Error"
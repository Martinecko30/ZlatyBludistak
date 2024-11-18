from pathlib import Path
from enums import LogLevel
import inspect
import datetime
import shutil

# Constants
CURRENT_FILE = str()
PATH = str()

def start():
    global CURRENT_FILE, PATH
    PATH = f"{Path(__file__).parent}\\logs\\"
    CURRENT_FILE = f"{Path(__file__).parent}\\logs\\log.txt"
    with open(CURRENT_FILE, "w") as file:
        file.write(f"{datetime.datetime.now().isoformat()}\n")

def log(log_level: LogLevel, text: str) -> None:
    '''
    Logs all information passed
    :param log_level: Log level
    :param text: Text to log
    :return: None
    '''
    global CURRENT_FILE

    stack = inspect.stack()
    caller = stack[1]

    text = f"({caller.filename}, {caller.function}, {caller.lineno}), (Level: {log_level.value}): {text}"

    if log_level is not LogLevel.HIDDEN:
        print(text)

    with open(CURRENT_FILE, "a") as file:
        file.write(f"{text}\n")

def end():
    global CURRENT_FILE, PATH
    print(PATH)
    t = datetime.datetime.now()
    t = f"{PATH}\\{t.strftime("%Y-%m-%d-%H-%M-%S")}.txt"
    shutil.copy2(CURRENT_FILE, t)

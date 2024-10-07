import time
from pynput.keyboard import Controller, Key
from win32gui import GetWindowText, GetForegroundWindow

DELAY = 0.005
FILE_PATH = "cribber/pg103.txt"
DESTINATION = "text.txt"

keyboard = Controller()  # Create the controller
delay = max(DELAY,0.02)
print(delay)
def main() -> None:
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        for line in file.readlines():
            print(line)
            type_string_with_delay(f"{line.strip()} \n")


def type_string_with_delay(string) -> None:
    time.sleep(delay)
    keyboard.press(Key.home)
    keyboard.release(Key.home)
    time.sleep(delay)
    time.sleep(delay)
    keyboard.press(Key.home)
    keyboard.release(Key.home)
    time.sleep(delay)
    for character in string:  # Loop over each character in the string
        check_destination(DESTINATION)
        keyboard.type(character)  # Type the character
        time.sleep(delay)  # Sleep for the amount of seconds generated




def check_destination(destination: str) -> None:
    """check if current forground window is the same as desierd destination
    if not wait a little bit"""
    WAIT = 0.5
    get_destination = lambda: GetWindowText(GetForegroundWindow())
    while destination not in (current := get_destination()):
        print(current, destination)
        time.sleep(WAIT)


if __name__ == "__main__":
    main()

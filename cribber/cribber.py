import time
from pynput.keyboard import Controller, Key
from win32gui import GetWindowText, GetForegroundWindow

DELAY = 0.00  # Delay between each keystroke in seconds
FILE_PATH = "cripper/pg103.txt"
DESTINATION = "mytext.txt"

keyboard = Controller()  # Create the controller
delay = max(DELAY,0.025)

def main() -> None:
    with open(FILE_PATH, "r", encoding="utf-8-sig") as file:
        for line in file:  # Loop over each line in the file
            line = line.encode("utf-8").decode("utf-8-sig")  # Decode the line
            print(repr(line))
            type_string_with_delay(line) 
            got_to_newline()
 
def type_string_with_delay(string) -> None:
    for character in string.strip():  # Loop over each character in the string
        check_destination(DESTINATION)
        keyboard.tap(character)  # Type the character
        time.sleep(delay)  # Sleep for the amount of seconds generated

def got_to_newline () -> None:
    """go to new line"""
    for ele in [" ", Key.enter, Key.home]:
        check_destination(DESTINATION)
        #print(repr(ele))
        keyboard.tap(ele)
        time.sleep(delay)  # Sleep for the amount of seconds generated
   

def check_destination(destination: str) -> None:
    """check if current forground window is the same as desierd destination
    if not wait a little bit"""
    WAIT = 1 
    def get_destination() -> str:
        return GetWindowText(GetForegroundWindow())
    while destination not in (current := get_destination()):
        print(current, destination)
        time.sleep(WAIT)

if __name__ == "__main__":
    main()

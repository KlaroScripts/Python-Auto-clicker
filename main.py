from pynput import mouse
from keyboard import add_hotkey, wait
from time import sleep
from threading import Thread
from os import system


class State:
    CLICKING = False
    CLICKS = 0
    TIMES_STARTED = 0


def forceStopClicking() -> State.CLICKING:
    State.CLICKING = False
    printStats()


def printStats() -> print:
    system('cls')
    print(f'''Click Stats:
Total Clicks: {State.CLICKS}
Times Started: {State.TIMES_STARTED}
''')


def clicker() -> State.CLICKS:
    while State.CLICKING:
        mouse.Controller().click(mouse.Button.left)
        State.CLICKS += 1
        sleep(.01)


def on_mid_click(x, y, button, pressed) -> clicker():
    if button == mouse.Button.middle and pressed:
        if State.CLICKING:
            State.CLICKING = False
            printStats()
        else:
            State.CLICKING = True
            Thread(target=clicker).start()
            State.TIMES_STARTED += 1


def mouse_listener() -> on_mid_click:
    with mouse.Listener(on_click=on_mid_click) as listener:
        listener.join()


if __name__ == '__main__':
    print('Press middle mouse button to start/stop clicking.\nPress ctrl+q to force Stop clicking.')
    system('title Python Auto Clicker')
    add_hotkey('ctrl+q', forceStopClicking)
    mouse_listener()
    wait()

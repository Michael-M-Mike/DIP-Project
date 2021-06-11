from pynput.keyboard import Key, Controller
import enum

Keyboard = Controller()

class Directions(enum.enum):
    UP = 0
    LEFT = 1
    RIGHT = 2
    STOP = 3

def controlling(direction):
    if direction==Directions.UP:
      Keyboard.press(Key.up)
      Keyboard.release(Key.left)
      Keyboard.release(Key.right)
    elif direction==Directions.LEFT:
      Keyboard.press(Key.up)
      Keyboard.press(Key.left)
      Keyboard.release(Key.right)
    elif direction==Directions.RIGHT:
      Keyboard.press(Key.up)
      Keyboard.release(Key.left)
      Keyboard.press(Key.right)
    elif direction==Directions.STOP:
      Keyboard.release(Key.up)
      Keyboard.release(Key.left)
      Keyboard.release(Key.right)
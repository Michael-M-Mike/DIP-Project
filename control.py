from pynput.keyboard import Key, Controller
import enum

Keyboard = Controller()

class Directions(enum.Enum):
    UP = 0
    LEFT = 1
    RIGHT = 2
    STOP = 3
    SPACE = 4

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
    elif direction==Directions.SPACE:
      Keyboard.press(Key.space)
      Keyboard.release(Key.up)
      Keyboard.release(Key.left)
      Keyboard.release(Key.right)

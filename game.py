import subprocess
import psutil
from pynput.keyboard import Key, Controller
Keyboard = Controller()

def game_start():
    Game_Path = './Windows Car Game/Image Processing Project.exe'
    #Game_Path = "./Image Processing Project/Game.x86_64"
    Game_Name = "Image Processing Project.exe" 
    #Game_Name = "Game.x86_64"
    process = subprocess.Popen(Game_Path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    while not process_running(Game_Name):
            print(process_running(Game_Name))
    Keyboard.press(Key.tab) #May not work

def process_running(process_name):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


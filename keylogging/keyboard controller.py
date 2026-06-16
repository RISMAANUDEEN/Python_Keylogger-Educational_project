#left to right, top to botto,
#from toop-lrft of the screen you can imagine the top-left to br (0,0)

from pynput.keyboard import Controller

def controlkeyboard():
    keyboard = Controller()
    keyboard.type("i am freaking awesome")

controlkeyboard()


#controlling your mouse
#listening the mouse
#controlling your keyboard
#listening the keyboard- will be finally used in our keystroke
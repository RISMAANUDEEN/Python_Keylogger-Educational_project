from pynput.mouse import Controller

def controlmouse():
    mouse = Controller()
    mouse.position = (500,200)
    
controlmouse()
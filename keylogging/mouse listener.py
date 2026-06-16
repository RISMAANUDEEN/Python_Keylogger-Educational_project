from pynput.mouse import Listener

def write_to(text):
    with open("mouse_log.txt",'a') as f:
        f.write(text + "\n")
    
def on_click(x,y,button,pressed):
    if pressed:
        write_to(f"click:{button} at ({x} , {y})")

with Listener(on_click = on_click) as l:
    l.join()
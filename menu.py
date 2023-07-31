from pybricks.hubs import PrimeHub
from pybricks.parameters import Side, Color, Button
from pybricks.tools import wait

hub = PrimeHub()

hub.display.orientation(up=Side.BOTTOM)

def selector(fns, selected=0):
    while True:
        print("selected", selected)
        hub.display.number(selected + 1)
        pressed = waitForButton()
        if Button.RIGHT in pressed and Button.LEFT in pressed:
            return selected
        elif Button.RIGHT in pressed:
            selected=(selected-1)%len(fns)
        elif Button.LEFT in pressed:
            selected=(selected+1)%len(fns)
        wait(200)

def menu(fns):
    selected = -1
    
    while True:
        hub.light.on(Color.ORANGE)
        selected = selector(fns, (selected+1)%len(fns))
        hub.light.on(Color.GREEN)
        locals()[fns[selected]]()
    
def waitForButton():
    def concatUnique(a, b):
        for x in b:
            if not x in a:
                a.append(x)
        return a
    pressed = []
    while not any(pressed):
        pressed = concatUnique(pressed, list(hub.buttons.pressed()))
        wait(10)
    while any(hub.buttons.pressed()):
        pressed = concatUnique(pressed, list(hub.buttons.pressed()))
        wait(10)
    return pressed

def fn():
    wait(1000)

menu(['fn', 'fn', 'fn'])

from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Side, Color, Button
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from Tour_mission import tour_mission
from Traverse import traverse
from Studio_mission import studio_mission

hub = PrimeHub()
hub.display.orientation(up=Side.RIGHT)

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
module_motor = Motor(Port.C)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=147)

def selector(fns, selected=0):
    while True:
        print("selected", selected + 1)
        hub.display.number(selected + 1)
        pressed = waitForButton()
        if Button.BLUETOOTH in pressed:
            return selected
        elif Button.LEFT in pressed:
            selected=(selected-1)%len(fns)
        elif Button.RIGHT in pressed:
            selected=(selected+1)%len(fns)
        wait(200)

def menu(fns, drive_base, module_motor):
    selected = -1
    
    while True:
        hub.light.on(Color.ORANGE)
        selected = selector(fns, (selected+1)%len(fns))
        hub.light.on(Color.GREEN)
        locals()[fns[selected]](drive_base, module_motor)
    
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

menu(['studio_mission', 'traverse', 'tour_mission'], drive_base, module_motor)
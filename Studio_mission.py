from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
module_motor = Motor(Port.C)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=147)

drive_base.straight(60)
drive_base.turn(-50)
drive_base.settings(400)
drive_base.straight(580)
drive_base.straight(-150)
drive_base.settings(250)
drive_base.turn(50)
drive_base.straight(430)
drive_base.turn(45)
drive_base.settings(500)
drive_base.straight(200)
drive_base.straight(-200)
drive_base.turn(-90)
drive_base.settings(600)
drive_base.straight(-750)
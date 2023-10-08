def tour_mission(drive_base, module_motor):
    drive_base.straight(40)
    drive_base.turn(74)
    drive_base.settings(400)
    drive_base.straight(845)
    module_motor.run_angle(51000000, 2300)
    drive_base.straight(-900)
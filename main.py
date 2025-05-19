robot.yahboom_tiny_bit.start()

def do_triangle():
    global stopMe, doingTriangle, doingCompass
    if doingCompass:
        all_stop()
    doingTriangle = True
    counter = 1
    stopMe = False
    while not stopMe:
        offset = 1
        if counter % 3:
            offset = -20
        elif counter % 2:
            offset = 20
        else:
            offset = 0
        robot.motor_tank(50, 50, 1000 - offset)
        robot.motor_stop()
        robot.motor_tank(50, -50, 530)
        robot.motor_stop()
        counter += 1
    doingTriangle = False
input.on_button_pressed(Button.A, do_triangle)

def on_button_pressed_b():
    global doingCompass, doingTriangle
    if not doingTriangle and not doingCompass:
        do_compass_90_turn()
    else:
        all_stop()

def all_stop():
    global stopMe
    stopMe = not stopMe
    doingTriangle = False
    doingCompass = False
    robot.motor_stop()
    basic.pause(10)

def do_compass_90_turn():
    global doingTriangle, doingCompass, stopMe
    if doingTriangle:
        all_stop()
    doingCompass = True
    stopMe = False
    heading = input.compass_heading()
    heading += 90
    if heading >= 360:
        heading -= 360
    while input.compass_heading() != heading and not stopMe:
        robot.motor_tank(10, -10)
        basic.pause(10)
    robot.motor_stop()
    doingCompass = False
input.on_button_pressed(Button.B, on_button_pressed_b)

button_b_count = 1
stopMe = False
doingTriangle = False
doingCompass = False
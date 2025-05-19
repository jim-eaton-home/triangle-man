robot.yahboomTinyBit.start()
input.onButtonPressed(Button.A, function do_triangle() {
    let offset: number;
    
    if (doingCompass) {
        all_stop()
    }
    
    doingTriangle = true
    let counter = 1
    stopMe = false
    while (!stopMe) {
        offset = 1
        if (counter % 3) {
            offset = -20
        } else if (counter % 2) {
            offset = 20
        } else {
            offset = 0
        }
        
        robot.motorTank(50, 50, 1000 - offset)
        robot.motorStop()
        robot.motorTank(50, -50, 530)
        robot.motorStop()
        counter += 1
    }
    doingTriangle = false
})
function all_stop() {
    
    stopMe = !stopMe
    let doingTriangle = false
    let doingCompass = false
    robot.motorStop()
    basic.pause(10)
}

function do_compass_90_turn() {
    
    if (doingTriangle) {
        all_stop()
    }
    
    doingCompass = true
    stopMe = false
    let heading = input.compassHeading()
    heading += 90
    if (heading >= 360) {
        heading -= 360
    }
    
    while (input.compassHeading() != heading && !stopMe) {
        robot.motorTank(10, -10)
        basic.pause(10)
    }
    robot.motorStop()
    doingCompass = false
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (!doingTriangle && !doingCompass) {
        do_compass_90_turn()
    } else {
        all_stop()
    }
    
})
let button_b_count = 1
let stopMe = false
let doingTriangle = false
let doingCompass = false

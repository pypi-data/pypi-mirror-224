# Import the robotar package
from pybotarena import RobotAR, PlatformAR
from GameStage002_Templates import move_forward_till_step_on_something, \
                                    check_ground_and_use_it

def convert_angle_to_360(angle):
    return angle % 360

def check_within(number, target, tolerance):
    half_tol = tolerance / 2
    return target - half_tol < number < target + half_tol

def rotate(r, angle):
    destinationOrientation = float(robot.get_orientation()) + angle

    # Correct orientation if outside boundary
    destinationOrientation = convert_angle_to_360(destinationOrientation)

    # Rotate till the rotation value is at the destination rotation but with a 10 degree margin of error
    while not check_within(float(r.get_orientation()), destinationOrientation, 10):
        # Ask the robot to start rotating left
        robot.wheels(0,100)
        # Let the robot rotate for 0.1 seconds
        robot.sleep(0.1)
        # Ask the robot to stop so that the robot can check rotation value
        robot.halt()


if __name__ == "__main__":
    # Create a robot connection which requires 3 parameters found in the game
    # The first parameter is the game ip address, second is port number and third is player id (0 to 3)
    ip_address = "10.19.27.227" 
    port_number = 49161
    robot = RobotAR(ip_address, port_number, 0)

    # Get robot to move and use the item platform
    move_forward_till_step_on_something(robot)
    check_ground_and_use_it(robot, PlatformAR.platform_code['item'])

    # Store the rotation you want to be facing
    # rotate left 55 degrees
    angle = -55
    rotate(robot, angle)

    # Move the robot forward abit because robot is currently stand on a platform
    robot.wheels(100,100)
    robot.sleep(2)
    robot.halt()

    # Get robot to move and use the exit platform
    move_forward_till_step_on_something(robot)
    check_ground_and_use_it(robot, PlatformAR.platform_code['exit'])


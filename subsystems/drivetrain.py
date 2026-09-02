import commands2
import wpilib
import wpilib.drive


class WestCoastDrivetrain(commands2.SubsystemBase):
    def __init__(self, left_motors, right_motors):
        self.left_motors = left_motors
        self.right_motors = right_motors

        # For one motor, positive value means clockwise spin while for other
        # positive value means counterclockwise spin
        self.right_motors.setInverted(True)

        self.drive_train = wpilib.drive.DifferentialDrive(self.left_motors, self.right_motors)

    def tankDrive(self, left_output_perc, right_output_perc):
        return self.drive_train.tankDrive(left_output_perc, right_output_perc)

    def arcadeDrive(self, speed_perc, turn_angle_perc):
        return self.drive_train.arcadeDrive(speed_perc, turn_angle_perc)

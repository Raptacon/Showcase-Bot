import commands2
import wpilib
import wpilib.drive


class WestCoastDrivetrain(commands2.SubsystemBase):
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor

        # For one motor, positive value means clockwise spin while for other
        # positive value means counterclockwise spin
        self.right_motor.setInverted(True)

        self.drive_train = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

    def tankDrive(self, left_output_perc, right_output_perc):
        return self.drive_train.tankDrive(left_output_perc, right_output_perc)

    def arcadeDrive(self, speed_perc, turn_angle_perc):
        self.speed = speed_perc * .5
        self.turn = turn_angle_perc * .5
        return self.drive_train.arcadeDrive(self.speed, self.turn)

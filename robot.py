import commands2
import rev
import wpilib
import wpimath

from commands.arcade_drive import ArcadeDrive
from commands.tank_drive import TankDrive
from subsystems.drivetrain import WestCoastDrivetrain


class WestCoastRobot(commands2.TimedCommandRobot):
    def robotInit(self):
        super().__init__()

        self.left_motor = rev.SparkMax(1 , rev.SparkLowLevel.MotorType.kBrushless)
        self.right_motor = rev.SparkMax(2 , rev.SparkLowLevel.MotorType.kBrushless)

        self.drivetrain = WestCoastDrivetrain(self.left_motor, self.right_motor)

        self.driver_controller = commands2.button.CommandXboxController(0)


    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        if False:
            self.drivetrain.setDefaultCommand(
                TankDrive(
                    lambda: wpimath.applyDeadband(
                        self.driver_controller.getLeftY(),
                        0.1,
                        1
                    ),
                    lambda: wpimath.applyDeadband(
                        self.driver_controller.getRightY(),
                        0.1,
                        1
                    ),
                    self.drivetrain
                )
            )
        else:
            self.drivetrain.setDefaultCommand(
                ArcadeDrive(
                    lambda: wpimath.applyDeadband(
                        self.driver_controller.getLeftY(),
                        0.1,
                        1
                    ),
                    lambda: wpimath.applyDeadband(
                        self.driver_controller.getRightX(),
                        0.1,
                        1
                    ),
                    self.drivetrain
                )
            )

    def teleopPeriodic(self):
        pass
        #print(f"Current status of A button: {self.driver_controller.a()}")

    def testInit(self):
        pass

    def testPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(WestCoastRobot)

import commands2


class ArcadeDrive(commands2.Command):
    def __init__(self, speed_percentage, turn_angle_percentage, drivetrain):
        super().__init__()

        self.speed_percentage = speed_percentage
        self.turn_angle_percentage = turn_angle_percentage
        self.drivetrain = drivetrain

        self.addRequirements(self.drivetrain)     

    def execute(self):
        self.drivetrain.arcadeDrive(self.speed_percentage(), self.turn_angle_percentage())
    
    def end(self, interrupted):
        self.drivetrain.arcadeDrive(0, 0)
    
    def isFinished(self):
        return False

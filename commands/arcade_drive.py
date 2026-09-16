import commands2
from wpimath.filter import SlewRateLimiter
from constats import constats

class ArcadeDrive(commands2.Command):
    def __init__(self, speed_percentage, turn_angle_percentage, drivetrain): # speed_limit,
        super().__init__()

        self.speed_percentage = speed_percentage# * 0.5
        self.turn_angle_percentage = turn_angle_percentage #* 0.5
        # self.speed_limit = speed_limit
        self.drivetrain = drivetrain

        # self.speed_limit = SlewRateLimiter(constats.RAMP_LIMIT)
        # self.rotation_limit = SlewRateLimiter(constats.RAMP_LIMIT)

        self.addRequirements(self.drivetrain)     

    def execute(self):
        # self.speed = self.speed_limit.calculate(self.speed_percentage()) * self.speed_limit
        # self.rotation = self.rotation_limit.calculate(self.turn_angle_percentage)
        self.drivetrain.arcadeDrive(self.speed_percentage(), self.turn_angle_percentage())
    
    def end(self, interrupted):
        self.drivetrain.arcadeDrive(0, 0)
    
    def isFinished(self):
        return False

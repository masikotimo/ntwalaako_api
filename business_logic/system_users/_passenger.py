from business_logic.auth.authentication import PassengerEmailAndPasswordAuthentication
from business_logic.auth import AuthController
from . import _user
User = _user.User


class Passenger(User):
    """
    A controller for Passenger as a system user.
    """

    def __init__(self,):
        super()

    # Mutators

    # Accessors

    # Generic User Operations

    def login(self, login_data):
        self.set_auth_controller(AuthController())
        self.get_auth_controller().set_in_logger(
            PassengerEmailAndPasswordAuthentication())
        InLogger = self.get_auth_controller().get_in_logger()
        return InLogger.login(login_data)

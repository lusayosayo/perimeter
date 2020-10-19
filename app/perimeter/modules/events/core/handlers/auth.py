from events.core import base_handler
from events.core.loggers.auth import LoginEventLogger, RegistrationEventLogger, PermissionEventLogger

class LoginEventHandler(base_handler.EventHandler):
    def get_logger(self):
        logger = LoginEventLogger(
            handler=self,
        )

        return logger

class RegistrationEventHandler(base_handler.EventHandler):
    def get_logger(self):
        logger = RegistrationEventLogger(
            handler=self,
        )

        return logger

class PermissionEventHandler(base_handler.EventHandler):
    def get_logger(self):
        logger = PermissionEventLogger(
            handler=self,
        )

        return logger

from events.core import base
from events.core.handlers.auth import LoginEventHandler, RegistrationEventHandler, PermissionEventHandler

class LoginEvent(base.Event):
    def get_handler(self):
        handler = LoginEventHandler(
            event=self
        )

        return handler

class RegistrationEvent(base.Event):
    def get_handler(self):
        handler = RegistrationEventHandler(
            event=self,
        )

        return handler

class PermissionEvent(base.Event):
    def get_handler(self):
        handler = PermissionEventHandler(
            event=self,
        )

        return self


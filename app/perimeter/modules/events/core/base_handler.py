from events.core import base
from datetime import datetime

class EventHandler:
    """ This class is the only class that other modules should interact
        with within this package. It is meant to provide a clean interface
        to the ugly details of event handling.

        It focuses on gathering session dependent parameters, marrying them
        with the event specification, then deciding how to respond to a
        particular event.

        Needless to say, this package was not made part of the django application
        but separated because it will run as an independent daemon responsible
        for maintaining event logs.
    """
    def __init__(
        self,
        event,
        handle_as=None,
    ):
        assert isinstance(event, base.Event)

        self.event = event
        self.handle_as = handle_as

    def get_logger(self):
        pass

    def log(self):
        time_stamp = datetime.utcnow().strftime("%y-%m-%d-%HH:%MM:%SS")
        class_name = type(self).__name__
        message = self.event.message

        string = '[{time_stamp}] - {class_name}: \n\t{message}'.format(
            time_stamp=time_stamp,
            class_name=class_name,
            message=message,
        )

        logger = self.get_logger()

        logger.write(string)

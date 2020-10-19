from events.core import base
from datetime import datetime

class EventHandler:
    """ This class is the base logger interface. If this class won't do it for you,
        feel free to extend it, override it, and downright re-engineer it.

        However, keep in mind that the API of this class is the standard API for
        logging in this project. If you want to change it, make sure you understand
        exactly what you're doing and how it will affect the rest of the program.
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

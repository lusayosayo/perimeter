class Event:
    """ This is the base event class that is used to define event specifications
        within this package. It is going to be bulky and ugly, but it'll be
        efficient and utilitarian.

        It aims at no clever design per say, but it will get the job done in the
        shortest time I can possibly machinate to achieve.
    """
    def __init__(
        self,
        message=None,
    ):
        self.message = message
    
    def get_handler(self):
        pass


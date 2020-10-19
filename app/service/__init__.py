""" This module is meant to be used to perform routine tasks on the
    perimeter.perimeter_daemon django application.

    It interacts with the daemon solely through HTTP requests,
    therefore it is necessary for the entire perimeter django project
    to be up and running for it to work.

    Ideally, it can also be used to reinvoke the service if it is ever
    down.
"""
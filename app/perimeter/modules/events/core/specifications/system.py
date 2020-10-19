from events.core import base

class AbsurdEvent(base.Event):
    pass

class FatalExceptionEvent(base.Event):
    pass

class GracefulExceptionEvent(base.Event):
    pass

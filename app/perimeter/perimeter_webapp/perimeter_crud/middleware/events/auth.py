from modules.events.core.specifications import auth

class LoginEventMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path == '/accounts/login':
            message = '{user_name} attempted to login through {url}'.format(
                user_name=request.POST.get('user_name'),
                url=request.path,
            )

            event = auth.LoginEvent(
                message=''
            )

        return self.get_response(request)
    
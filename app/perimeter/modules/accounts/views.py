from django.shortcuts import loader, redirect

from django.http import HttpResponse

from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms

from django.contrib.auth.models import User

class RegisterView(auth_views.TemplateView):
    template_name = 'accounts/module_blocks/users/register.dtl.html'

    def get(self, request):
        template = loader.get_template(self.template_name)
        context = {
            'form': auth_forms.UserCreationForm(),
        }

        return HttpResponse(template.render(context, request))

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        return redirect('/perimeter/accounts/login/')

class ListView(auth_views.TemplateView):
    
    def __init__(self,
        template_name='accounts/module_blocks/users/index.dtl.html'):
        super().__init__()
        self.template_name = template_name

    def get(self, request):
        template = loader.get_template(self.template_name)
        users = User.objects.all()

        context = {
            'users': users,
        }

        return HttpResponse(
            template.render(
                context,
                request
            )
        )

    def get_inactive(self, request):
        template = loader.get_template(self.template_name)
        users = User.objects.filter(is_active=False)

        context = {
            'users': users,
        }

        return template.render(context, request)

    def get_active(self, request):
        template = loader.get_template(self.template_name)
        users = User.objects.filter(is_active=True)

        context = {
            'users': users,
        }

        return template.render(context, request)
    

def show(request, user_id):
    template = loader.get_template('accounts/module_blocks/users/show.dtl.html')

    user = User.objects.get(
        id=user_id,
    )

    context = {
        'user': user,
    }

    return HttpResponse(template.render(context, request))

def edit(request, user_id):
    template = loader.get_template('accounts/module_blocks/users/edit.dtl.html')

    user = User.objects.get(
        id=user_id,
    )

    context = {
        'user': user,
    }

    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('accounts/module_blocks/users/index.dtl.html')

    users = User.objects.all()

    users_len = len(users)
    
    context = {
        'users': users,
    }

    return HttpResponse(template.render(context, request))


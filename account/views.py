from django.http import HttpResponseRedirect
from django.template import RequestContext

from account.forms import UserRegisterForm
from account.models import User
from django.contrib import messages
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView


# Create your views here.


class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.filter(is_active=True)
    fields = ("first_name", "last_name",)
    success_url = reverse_lazy("homepage")

    def get_object(self, queryset=None):
        return self.request.user


class SignUpView(CreateView):
    form_class = UserRegisterForm
    template_name = "account/user_signup.html"
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        print(SignUpView)
        return super().form_valid(form)


class ActivateUserView(View):
    """Make User active after email confirmation."""

    def get(self, request, confirmation_token):
        """Get User and make it active."""
        user = get_object_or_404(User, confirmation_token=confirmation_token)
        user.is_active = True
        user.save(update_fields=('is_active',))
        return redirect("homepage")


def change_password(request):
    """Change password for current User."""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            print("Form is valid!")
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль был сохранен!')
            return redirect('homepage')
        else:
            print("Form not valid!")
            messages.error(request, 'Исправльте ошибку.')
    else:
        print("Else")
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })


def login(request):
    email = password = ''
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/index.html/')
            else:
                state = "Your account is not active, please contact the administrator."
        else:
            state = "Your email and/or password were incorrect."

    return redirect("homepage")

def logout(request):
    auth_logout(request)
    return redirect("homepage")
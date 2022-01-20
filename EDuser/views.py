import profile
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views.generic import FormView

from .models import Eduser
from .forms import RegisterForm, ProfileForm, LoginForm

# Create your views here.
def index(request):
    return render(request, "base/home.html", {"email": request.session.get("user")})


class RegisterView(FormView):
    template_name = "EDuser/register.html"
    form_class = RegisterForm
    success_url = "/registerProfile"

    def form_valid(self, form):
        eduser = Eduser(
            username=form.data.get("username"),
            email=form.data.get("email"),
            password=make_password(form.data.get("password")),
        )
        eduser.save()

        return super().form_valid(form)



def RegisterProfileView(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            deathuser = Eduser(
                username = form.username,
                useremail = form.useremail,
                password = make_password(form.password)
            )
            deathuser.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


class LoginView(FormView):
    template_name = "EDuser/login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        self.request.session["user"] = form.data.get("email")
        return super().form_valid(form)


def logout(request):
    if "user" in request.session:
        del request.session["user"]
    return redirect("/")

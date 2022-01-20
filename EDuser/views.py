import profile
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views.generic import FormView

from .models import Eduser
from .forms import RegisterForm, ProfileForm, LoginForm

# Create your views here.

class RegisterView(FormView):
    template_name = "EDuser/register.html"
    form_class = RegisterForm
    success_url = "/"

    def form_valid(self, form):
        eduser = Eduser(
            username=form.data.get("username"),
            email=form.data.get("email"),
            password=make_password(form.data.get("password")),
        )
        eduser.save()
        self.request.session['username'] = form.data.get('username')
        return super().form_valid(form)



def RegisterProfileView(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            eduser = Eduser.objects.get(username= request.session['username'])
            eduser.profile_img.upload_to = ""
            print(request.FILES)
            # eduser.save(profile_img = request.FILES['profile_img'])
            return redirect('/')
    else:
        form = ProfileForm()
    return render(request, 'EDuser/register_profile.html', {'form': form})


class LoginView(FormView):
    template_name = "EDuser/login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        self.request.session["username"] = form.data.get("username")
        return super().form_valid(form)


def logout(request):
    if "username" in request.session:
        del request.session["username"]
    return redirect("/")

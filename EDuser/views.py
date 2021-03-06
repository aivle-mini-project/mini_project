from genericpath import exists
import profile
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views.generic import FormView

from .models import Eduser
from .forms import RegisterForm, ProfileForm, LoginForm

from .decorator import login_required
# Create your views here.

class RegisterView(FormView):
    template_name = "EDuser/register.html"
    form_class = RegisterForm
    success_url = "/toRegisterProfile"

    def form_valid(self, form):
        eduser = Eduser(
            username=form.data.get("username"),
            email=form.data.get("email"),
            password=make_password(form.data.get("password")),
        )
        eduser.save()
        
        self.request.session['userid'] = eduser.id
        self.request.session['username'] = form.data.get('username')
        return super().form_valid(form)


def toRegisterProfile(request):
    return redirect("/registerProfile")


@login_required
def RegisterProfileView(request):
    if request.method == 'POST':
        
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            eduser = Eduser.objects.get(username=request.session['username'])
            if eduser.profile_img:
                eduser.profile_img.delete()
                eduser.save()
            eduser.profile_img = form.cleaned_data['profile_img']
            eduser.save()
            return redirect('/')
    else:
        form = ProfileForm()
        eduser = Eduser.objects.get(username=request.session['username'])

    return render(request, 'EDuser/register_profile.html', {'form': form, 'eduser':eduser})


class LoginView(FormView):
    template_name = "EDuser/login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        eduser = Eduser.objects.get(username=form.data.get("username"))
        self.request.session['userid'] = eduser.id
        self.request.session['username'] = form.data.get('username')

        return super().form_valid(form)


def logout(request):
    if "username" in request.session:
        del request.session['userid']
        del request.session["username"]
    return redirect("/")

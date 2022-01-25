from django.shortcuts import render
from EDuser.models import Eduser
from diary.models import Diary, Expression
# Create your views here.

def mypage(request):
    user=(request.session['username'])
    expressions = Eduser.objects.get(username=request.session.get('username')).expression_set.all()
    return render(request, 'mypage/mypage.html', {'expressions':expressions,'user':user})
from django.shortcuts import render
from diary.models import Diary
from EDuser.models import Eduser

# Create your views here.
def Cal(request):
    user=(request.session['username'])
    emo = Eduser.objects.get(username=request.session.get('username')).diary_set.all()
    return render(request,'calpage/cal.html', {'user':user,'data':emo})
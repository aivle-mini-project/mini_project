from datetime import date
from django.shortcuts import render

from diary.models import DiaryDetail
from diary.views import detail

# Create your views here.
def Cal(request):
    emo = DiaryDetail.objects.all()

    return render(request,'calpage/cal.html', {'data':emo})
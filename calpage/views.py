from datetime import date
from django.shortcuts import render

from diary.models import Diary

# Create your views here.
def Cal(request):
    emo = Diary.objects.all()
    return render(request,'calpage/cal.html', {'data':emo})
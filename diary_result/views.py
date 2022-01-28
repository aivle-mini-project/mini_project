from unittest import removeResult
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests
from .models import Tag
from EDuser.models import Eduser
from diary.models import Diary, DiaryDetail, DiaryDetailHighlight

from EDuser.decorator import login_required

 
 

# Create your views here.
@login_required
def index(request):
    user_id = request.session.get('userid') #세션으로부터 가져옴
    eduser = Eduser.objects.get(pk=user_id) #user_id를 기본키로함
    diary = Diary.objects.filter(writer= eduser)
    last_diary = diary[0]
    diary_list = last_diary.diarydetail_set.all()
    highlight = DiaryDetailHighlight.objects.all()

    if request.method == "POST": 
        tags = request.POST.get('tags_input') 
        tags = tags.split(' ')
        for tag in tags:
            if not Tag.objects.filter(tag = tag):
                Tag.objects.create(diary=last_diary, tag=tag)
        tag_list = Tag.objects.filter(diary=last_diary)
        return render(request,'diary_result/result.html', {'last_diary':last_diary, 'diary_list':diary_list, 'highlight':highlight, 'tag_list':tag_list})
    else:
        tag_list = Tag.objects.filter(diary=last_diary)
        return render(request,'diary_result/result.html', {'last_diary':last_diary, 'diary_list':diary_list, 'highlight':highlight, 'tag_list':tag_list})

def tagBoard(request, tag):
    tags = Tag.objects.filter(tag=tag)
    tag = tags[0]
    print(tag)
    print(tag.diary)
    # diary_detail = DiaryDetail.objects.get(diary = tag.diary)
    print(tag.diary.diarydetail_set.all())

    return render(request, 'diary_result/tagboard.html', {'tags': tags})
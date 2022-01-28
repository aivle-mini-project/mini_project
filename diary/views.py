from csv import writer
import encodings
from encodings import utf_8
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.forms.models import model_to_dict
from django.utils import timezone
from .models import Diary, DiaryDetail, DiaryDetailHighlight
from EDuser.models import Eduser
from EDuser.decorator import login_required
from .forms import DiaryForm
import requests,json
from django.core.exceptions import ValidationError
from html.parser import HTMLParser
import ast,datetime

# Create your views here.
#creae view
@login_required
def create(request):
    #DB제거용
    if request.method =='POST':
        diary_id = Diary.objects.last().id
        diary= Diary.objects.get(id =diary_id)
        diary.delete()
        return render(request, 'diary/create_diary.html')

    return render(request, 'diary/create_diary.html')
#detail view
@login_required
def detail(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            try:
                text = form.cleaned_data['write']
                print(text,"valid")
            #text = request.POST.get('input1') 
                url = "https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze"
                data = {
                "content": text
                }
                id ="j7n6px1uvx"
                pw ="jRa6fHWYxG5qwQC9VqtjpFrXOA4GhsQQoXEEnVEf"
                headers = {"Content-Type":"application/json",
                        "X-NCP-APIGW-API-KEY-ID":id,
                        "X-NCP-APIGW-API-KEY":pw, }
                #print(headers)
                res = requests.post(url ,data = json.dumps(data) , headers= headers)
                res.encoding ='UTF-8'
                result = json.loads(res.text)
                ####실험용 dictionary############
                # result = {
                #         "document": {
                #             "sentiment": "negative",
                #             "confidence": {
                #                 "neutral": 0.14525136640572725,
                #                 "positive": 0.00186876227013191,
                #                 "negative": 0.8528798713241407
                #             }
                #         },
                #         "sentences": [
                #             {
                #                 "content": "싸늘하다.",
                #                 "offset": 0,
                #                 "length": 5,
                #                 "sentiment": "negative",
                #                 "confidence": {
                #                     "negative": 0.9961358904838562,
                #                     "positive": 0.0036366574931889772,
                #                     "neutral": 0.0002274021098855883
                #                 },
                #                 "highlights": [
                #                     {
                #                         "offset": 0,
                #                         "length": 4
                #                     }
                #                 ]
                #             },
                #             {
                #                 "content": " 가슴에 비수가 날아와 꽂힌다.",
                #                 "offset": 5,
                #                 "length": 17,
                #                 "sentiment": "negative",
                #                 "confidence": {
                #                     "negative": 0.927976131439209,
                #                     "positive": 0.07131962478160858,
                #                     "neutral": 0.0007042606011964381
                #                 },
                #                 "highlights": [
                #                     {
                #                         "offset": 1,
                #                         "length": 15
                #                     }
                #                 ]
                #             }
                #         ]
                #     }
                #####제거 부분 (DB저장)
                
                print(res.status_code)
                if res.status_code == 200:
                    #Diary 모델에 넣기
                    user_id = request.session['username']
                    print(timezone.now().strftime("%Y-%m-%d"))
                    writer = Eduser.objects.get(username = user_id)
                    #timezone.now().strftime("%Y-%m-%d")
                    d = Diary(writer = writer, write =text, emotion = result['document']['sentiment'], neutral =result['document']['confidence']['neutral'],positive =result['document']['confidence']['positive'],negative =result['document']['confidence']['negative'],register_date =timezone.now())
                    d.save()
                    diary_id = Diary.objects.last().id
                    diary= Diary.objects.get(id =diary_id)
                    for sentence in result['sentences']:
                        diary_tree = sentence['content']
                        dt = DiaryDetail(diary = diary, write = diary_tree, emotion = sentence['sentiment'],neutral =sentence['confidence']['neutral'],positive =sentence['confidence']['positive'],negative =sentence['confidence']['negative'] )
                        dt.save()
                        diary_detail_id = DiaryDetail.objects.last().id
                        diary_detail = DiaryDetail.objects.get(id =diary_detail_id)
                        for highlight in sentence['highlights']:
                            dth = DiaryDetailHighlight(diary_detail = diary_detail,offset =highlight['offset'],length=highlight['length'])
                            dth.save()
                    return render(request,'diary/diary_detail.html',result)
                else:
                    if res.status_code == 500:
                        return render(request,'diary/500.html',result)
                    elif res.status_code == 401:
                        return render(request,'diary/401.html',result)
                    else:
                        return render(request,'diary/404.html',result)
            except ValidationError as e:
                print("eeeeeerrrrrrrrrrrrrorrrrrrrrrrrrrrrrrrrrr")

        else:
            print("invalid", type(form),request.POST)
        
    else:
        form =DiaryForm()
    return render(request, 'diary/create_diary.html',{'form':form})

#list view
@login_required
def list(request):
    if request.method =='POST':
        if request.POST.get('hidden'):
            ##update 부분
            print('update')
            update_diary = request.POST.get('hidden')
            update_diary = ast.literal_eval(update_diary)
            user_id = request.session['username']
            writer = Eduser.objects.get(username = user_id)
            diary_list = Diary.objects.filter(writer= writer)
            diary = diary_list.filter(register_date__range=[timezone.now().strftime('%Y-%m-%d 0:0'), timezone.now().strftime('%Y-%m-%d 23:59')])
            diary =diary.last()
            format = ''
            if '오후' in update_diary:
                format = '%Y년 %m월 %d일 %H:%M 오후'
            else:
                format = '%Y년 %m월 %d일 %H:%M 오전'
            dt_datetime = datetime.datetime.strptime(update_diary[5],format)
            print(dt_datetime)            
            diary.write = str(update_diary[0])
            diary.emotion = str(update_diary[1])
            diary.neutral = float(update_diary[2])
            diary.positive = float(update_diary[3])
            diary.negative = float(update_diary[4])
            diary.register_date = dt_datetime
            diary.save()
            return HttpResponseRedirect('/mypage/mydiary/')
            
    # user_id = request.session['username']
    # writer = Eduser.objects.get(username = user_id)
    # diary_list = Diary.objects.filter(writer= writer)
    # # diary_list1 = diary_list[1]
    # # diary = diary_list1.diarydetail_set.all()
    # return render(request, 'diary/diary_list.html',{'diary_list':diary_list})

    
@login_required
def edit(request):
    if request.method =='POST':
        print(request)
        #print(diary_date.date,type(diary_date))
        #날짜 지정
        print(timezone.now().year,timezone.now().month,timezone.now().day,"dfsdfsfasfsf")
        user_id = request.session['username']
        writer = Eduser.objects.get(username = user_id)
        diary_list = Diary.objects.filter(writer= writer)
        diary_total= diary_list.filter(register_date__range=[timezone.now().strftime('%Y-%m-%d 0:0'), timezone.now().strftime('%Y-%m-%d 23:59')])
        diary = diary_total.first()
        #print(diary.write,'diaryfirst')#방금 쓴거
        #print(diary_total.last().write,'diarylast')#처음에 쓴거
        if len(diary_total) ==1:
            return HttpResponseRedirect('/diary/list/')
        elif len(diary_total)>1:
            diary_text = diary_total.last()
            print('delte 2over' )
            diary1 =diary_total.filter(pk__lt = diary_total[0].id)
            diary1.delete()
            return render(request, 'diary/edit_diary.html',{'diary':diary,'diary_text':diary_text})




        # diary_text = diary_total[1]
        # print(diary_text,'diayr_text')
        # #2개 이상 삭제 부분
        # if len(diary_total)>1:
        #     

        # if diary:
        #     

            
            # form = '<tr><th><label for="id_write">일기의:</label></th><td><ul class="errorlist"><li>이미 오늘 일기를 작성하셨습니다</li></ul><textarea name="write" cols="40" rows="10" maxlength="100" required id="id_write"></textarea></td></tr> '
            # return render(request, 'diary/create_diary.html',{'form':form})
    
    # user_id = request.session['username']
    # writer = Eduser.objects.get(username = user_id)
    # diary_list = Diary.objects.filter(writer= writer)
    # diary_list1 = diary_list[1]
    # diary = diary_list1.diarydetail_set.all()
    # print(diary)
    # return render(request, 'diary/diary_list.html',{'diary_list':diary_list})

 